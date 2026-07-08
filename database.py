import os
from contextlib import contextmanager
from datetime import datetime, timedelta
from typing import List, Dict, Any

import psycopg2
import psycopg2.extras

FREE_ANALYSES_LIMIT = 15


class Database:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self._init_db()

    @contextmanager
    def _conn(self):
        # psycopg2's own connection context manager only commits/rolls back
        # the transaction on exit, it never closes the socket. Every one of
        # the ~50 call sites below did `with self._conn() as conn:`, so each
        # query leaked a physical Postgres connection — the bot would run
        # fine until the leak hit Postgres's max_connections, at which point
        # every DB call (including the 20:00 evening push) started failing.
        conn = psycopg2.connect(self.database_url)
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def _init_db(self):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS meals (
                        id SERIAL PRIMARY KEY,
                        user_id BIGINT NOT NULL,
                        day TEXT NOT NULL,
                        time TEXT NOT NULL,
                        food_description TEXT NOT NULL,
                        calories INTEGER NOT NULL,
                        protein INTEGER NOT NULL DEFAULT 0,
                        fat INTEGER NOT NULL DEFAULT 0,
                        carbs INTEGER NOT NULL DEFAULT 0,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                cur.execute("""
                    CREATE INDEX IF NOT EXISTS idx_user_day ON meals(user_id, day)
                """)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS goals (
                        user_id BIGINT PRIMARY KEY,
                        calories INTEGER NOT NULL DEFAULT 2000,
                        protein INTEGER NOT NULL DEFAULT 100,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS weight_log (
                        id SERIAL PRIMARY KEY,
                        user_id BIGINT NOT NULL,
                        weight REAL NOT NULL,
                        day TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS weight_goal (
                        user_id BIGINT PRIMARY KEY,
                        target_weight REAL NOT NULL,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS profiles (
                        user_id BIGINT PRIMARY KEY,
                        goal TEXT NOT NULL,
                        sex TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        height INTEGER NOT NULL,
                        weight REAL NOT NULL,
                        activity TEXT NOT NULL DEFAULT 'moderate',
                        daily_calories INTEGER NOT NULL,
                        target_cal_low INTEGER NOT NULL,
                        target_cal_high INTEGER NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS notifications (
                        user_id BIGINT PRIMARY KEY,
                        breakfast_enabled INTEGER NOT NULL DEFAULT 1,
                        breakfast_time TEXT NOT NULL DEFAULT '09:00',
                        lunch_enabled INTEGER NOT NULL DEFAULT 1,
                        lunch_time TEXT NOT NULL DEFAULT '13:00',
                        dinner_enabled INTEGER NOT NULL DEFAULT 1,
                        dinner_time TEXT NOT NULL DEFAULT '19:00',
                        timezone_offset INTEGER NOT NULL DEFAULT 3
                    )
                """)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        user_id BIGINT PRIMARY KEY,
                        terms_accepted INTEGER NOT NULL DEFAULT 0,
                        terms_accepted_at TIMESTAMP,
                        target_weight_warning_level TEXT,
                        target_confirmed INTEGER DEFAULT 0,
                        target_confirmed_at TIMESTAMP
                    )
                """)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS subscriptions (
                        user_id BIGINT PRIMARY KEY,
                        free_analyses_used INTEGER NOT NULL DEFAULT 0,
                        sub_expires_at TIMESTAMP,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                # Safe column additions (idempotent)
                for col_def in [
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS target_weight_warning_level TEXT",
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS target_confirmed INTEGER DEFAULT 0",
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS target_confirmed_at TIMESTAMP",
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS weight_tip_sent INTEGER NOT NULL DEFAULT 0",
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS language TEXT DEFAULT 'auto'",
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS tg_language TEXT",
                    "ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS trial_ended_at TIMESTAMP DEFAULT NULL",
                    "ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS winback_sent_at TIMESTAMP DEFAULT NULL",
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS first_seen_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
                    "ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS photo_analyses INTEGER NOT NULL DEFAULT 0",
                    "ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS profile_prompted BOOLEAN DEFAULT FALSE",
                    "ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS reminders_prompted BOOLEAN DEFAULT FALSE",
                    # Воронка онбординга: до какого экрана дошёл пользователь.
                    # 1=цель, 2=пол, 3=возраст, 4=вес+рост, 5=активность, 6=завершил.
                    "ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS onb_step INTEGER NOT NULL DEFAULT 0",
                    # Отметка «нажал Start» — ставится в начале start(), до онбординга.
                    # NULL у старых юзеров (без отметки). Не связана с onb_step / first_seen_at.
                    "ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS started_at TIMESTAMP DEFAULT NULL",
                    # Источник перехода (deep-link ?start=<src>): ig / site / NULL=direct.
                    # First-touch: пишется вместе со started_at, у вернувшихся не перетирается.
                    "ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS source TEXT DEFAULT NULL",
                    # Сколько раз запись исправляли (✏️ / /edit). Первое исправление
                    # каждой записи бесплатно, дальше списывается скан.
                    "ALTER TABLE meals ADD COLUMN IF NOT EXISTS corrections_used INTEGER NOT NULL DEFAULT 0",
                    # IANA-имя таймзоны (Europe/Kyiv и т.п.) — учитывает DST.
                    # NULL → фолбэк на целочисленный timezone_offset.
                    "ALTER TABLE notifications ADD COLUMN IF NOT EXISTS tz_name TEXT DEFAULT NULL",
                ]:
                    cur.execute(col_def)
            conn.commit()

    def get_profile(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM profiles WHERE user_id = %s", (user_id,))
                row = cur.fetchone()
                return dict(row) if row else None

    def set_profile(self, user_id: int, goal: str, sex: str, age: int,
                    height: int, weight: float, daily_calories: int,
                    target_cal_low: int, target_cal_high: int, activity: str = "moderate"):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO profiles
                        (user_id, goal, sex, age, height, weight, activity, daily_calories, target_cal_low, target_cal_high)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (user_id) DO UPDATE SET
                        goal = EXCLUDED.goal, sex = EXCLUDED.sex, age = EXCLUDED.age,
                        height = EXCLUDED.height, weight = EXCLUDED.weight,
                        activity = EXCLUDED.activity,
                        daily_calories = EXCLUDED.daily_calories,
                        target_cal_low = EXCLUDED.target_cal_low,
                        target_cal_high = EXCLUDED.target_cal_high
                """, (user_id, goal, sex, age, height, weight, activity,
                      daily_calories, target_cal_low, target_cal_high))
            conn.commit()

    def add_meal(self, user_id: int, day: str, time: str, food_description: str,
                 calories: int, protein: int, fat: int, carbs: int) -> int:
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO meals (user_id, day, time, food_description, calories, protein, fat, carbs)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id
                """, (user_id, day, time, food_description, calories, protein, fat, carbs))
                meal_id = cur.fetchone()[0]
            conn.commit()
            return meal_id

    def get_meals_for_day(self, user_id: int, day: str) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("""
                    SELECT food_description, calories, protein, fat, carbs, time
                    FROM meals WHERE user_id = %s AND day = %s
                    ORDER BY created_at ASC
                """, (user_id, day))
                return [dict(row) for row in cur.fetchall()]

    def get_meals_for_day_with_ids(self, user_id: int, day: str) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("""
                    SELECT id, food_description, calories, protein, fat, carbs, time, corrections_used
                    FROM meals WHERE user_id = %s AND day = %s
                    ORDER BY created_at ASC
                """, (user_id, day))
                return [dict(row) for row in cur.fetchall()]

    def get_meal_by_id(self, meal_id: int, user_id: int):
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM meals WHERE id = %s AND user_id = %s", (meal_id, user_id))
                row = cur.fetchone()
                return dict(row) if row else None

    def delete_meal_by_id(self, meal_id: int, user_id: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM meals WHERE id = %s AND user_id = %s", (meal_id, user_id))
            conn.commit()

    def increment_meal_corrections(self, meal_id: int, user_id: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE meals SET corrections_used = corrections_used + 1 "
                    "WHERE id = %s AND user_id = %s",
                    (meal_id, user_id)
                )
            conn.commit()

    def update_meal_by_id(self, meal_id: int, user_id: int, food_description: str,
                          calories: int, protein: int, fat: int, carbs: int) -> bool:
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE meals
                    SET food_description = %s, calories = %s, protein = %s, fat = %s, carbs = %s
                    WHERE id = %s AND user_id = %s
                """, (food_description, calories, protein, fat, carbs, meal_id, user_id))
                updated = cur.rowcount > 0
            conn.commit()
        return updated

    def get_weekly_summary(self, user_id: int) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("""
                    SELECT
                        day,
                        SUM(calories) as total_calories,
                        SUM(protein) as total_protein,
                        SUM(fat) as total_fat,
                        SUM(carbs) as total_carbs,
                        COUNT(*) as meals_count
                    FROM meals
                    WHERE user_id = %s AND day::date >= CURRENT_DATE - INTERVAL '7 days'
                    GROUP BY day ORDER BY day DESC
                """, (user_id,))
                return [dict(row) for row in cur.fetchall()]

    def set_goal(self, user_id: int, calories: int, protein: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO goals (user_id, calories, protein)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (user_id) DO UPDATE SET
                        calories = EXCLUDED.calories,
                        protein = EXCLUDED.protein,
                        updated_at = CURRENT_TIMESTAMP
                """, (user_id, calories, protein))
            conn.commit()

    def get_goal(self, user_id: int) -> Dict[str, Any]:
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT calories, protein FROM goals WHERE user_id = %s", (user_id,))
                row = cur.fetchone()
                return dict(row) if row else None

    def log_weight(self, user_id: int, weight: float):
        today = __import__('datetime').date.today().isoformat()
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO weight_log (user_id, weight, day) VALUES (%s, %s, %s)",
                    (user_id, weight, today)
                )
            conn.commit()

    def get_latest_weight(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(
                    "SELECT weight, day FROM weight_log WHERE user_id = %s ORDER BY created_at DESC LIMIT 1",
                    (user_id,)
                )
                row = cur.fetchone()
                return dict(row) if row else None

    def set_weight_goal(self, user_id: int, target_weight: float):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO weight_goal (user_id, target_weight)
                    VALUES (%s, %s)
                    ON CONFLICT (user_id) DO UPDATE SET
                        target_weight = EXCLUDED.target_weight,
                        updated_at = CURRENT_TIMESTAMP
                """, (user_id, target_weight))
            conn.commit()

    def get_weight_goal(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT target_weight FROM weight_goal WHERE user_id = %s", (user_id,))
                row = cur.fetchone()
                return dict(row) if row else None

    def get_weight_history(self, user_id: int, days: int = 7) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("""
                    SELECT weight, day FROM weight_log
                    WHERE user_id = %s
                    ORDER BY created_at DESC LIMIT %s
                """, (user_id, days))
                rows = cur.fetchall()
                return [dict(r) for r in reversed(rows)]

    def delete_meals_for_day(self, user_id: int, day: str):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM meals WHERE user_id = %s AND day = %s", (user_id, day))
            conn.commit()

    # ── Onboarding tips ───────────────────────────────────────────

    def get_users_for_weight_tip(self) -> list:
        """Пользователи на 2-й день после принятия условий (1+ день назад),
        которым ещё не отправлена подсказка про вес."""
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("""
                    SELECT u.user_id, COALESCE(n.timezone_offset, 3) as timezone_offset,
                           n.tz_name
                    FROM users u
                    LEFT JOIN notifications n ON n.user_id = u.user_id
                    WHERE u.terms_accepted = 1
                      AND u.terms_accepted_at <= NOW() - INTERVAL '1 day'
                      AND u.weight_tip_sent = 0
                """)
                return [dict(row) for row in cur.fetchall()]

    def get_users_for_winback(self) -> list:
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("""
                    SELECT u.user_id
                    FROM subscriptions s
                    JOIN users u ON u.user_id = s.user_id
                    WHERE s.trial_ended_at <= NOW() - INTERVAL '2 days'
                      AND (s.sub_expires_at IS NULL OR s.sub_expires_at <= NOW())
                      AND s.winback_sent_at IS NULL
                      AND u.terms_accepted = 1
                """)
                return [dict(row) for row in cur.fetchall()]

    def mark_winback_sent(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE subscriptions SET winback_sent_at = NOW() WHERE user_id = %s",
                    (user_id,)
                )
            conn.commit()

    def get_users_for_evening_push(self) -> list:
        """Пользователи, логировавшие еду в последние 3 дня — для вечернего пуша.
        Юзеры, выключившие все напоминания, не получают и вечерний итог —
        это единственный способ отписаться от него."""
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("""
                    SELECT u.user_id, COALESCE(n.timezone_offset, 3) as timezone_offset,
                           n.tz_name
                    FROM users u
                    LEFT JOIN notifications n ON n.user_id = u.user_id
                    WHERE u.terms_accepted = 1
                      AND (n.user_id IS NULL
                           OR n.breakfast_enabled = 1
                           OR n.lunch_enabled = 1
                           OR n.dinner_enabled = 1)
                      AND EXISTS (
                          SELECT 1 FROM meals m
                          WHERE m.user_id = u.user_id
                            AND m.day::date >= CURRENT_DATE - INTERVAL '3 days'
                      )
                """)
                return [dict(row) for row in cur.fetchall()]

    def mark_weight_tip_sent(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE users SET weight_tip_sent = 1 WHERE user_id = %s",
                    (user_id,)
                )
            conn.commit()

    # ── Notifications ─────────────────────────────────────────────

    def get_user_tz(self, user_id: int) -> tuple:
        """(tz_name, offset) юзера; (None, 3) если не настраивал.
        tz_name — IANA-имя с учётом DST, offset — целочисленный фолбэк."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT tz_name, timezone_offset FROM notifications WHERE user_id = %s", (user_id,))
                row = cur.fetchone()
                return (row[0], row[1]) if row else (None, 3)

    def set_timezone(self, user_id: int, offset: int, tz_name: str = None):
        """Сохраняет таймзону, не трогая тумблеры напоминаний.
        tz_name=None — юзер задал смещение вручную, IANA-зона сбрасывается."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO notifications (user_id, timezone_offset, tz_name)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (user_id) DO UPDATE SET
                        timezone_offset = EXCLUDED.timezone_offset,
                        tz_name         = EXCLUDED.tz_name
                """, (user_id, offset, tz_name))
            conn.commit()

    def get_notifications(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM notifications WHERE user_id = %s", (user_id,))
                row = cur.fetchone()
                return dict(row) if row else None

    def get_or_create_notifications(self, user_id: int) -> dict:
        notif = self.get_notifications(user_id)
        if not notif:
            with self._conn() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO notifications (user_id) VALUES (%s) ON CONFLICT DO NOTHING",
                        (user_id,)
                    )
                conn.commit()
            notif = self.get_notifications(user_id)
        return notif

    def save_notifications(self, user_id: int, breakfast_enabled: int,
                           lunch_enabled: int, dinner_enabled: int,
                           timezone_offset: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO notifications
                        (user_id, breakfast_enabled, lunch_enabled, dinner_enabled, timezone_offset)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (user_id) DO UPDATE SET
                        breakfast_enabled = EXCLUDED.breakfast_enabled,
                        lunch_enabled     = EXCLUDED.lunch_enabled,
                        dinner_enabled    = EXCLUDED.dinner_enabled,
                        timezone_offset   = EXCLUDED.timezone_offset
                """, (user_id, breakfast_enabled, lunch_enabled, dinner_enabled, timezone_offset))
            conn.commit()

    def save_notification_time(self, user_id: int, meal_type: str, time_str: str):
        allowed = {"breakfast", "lunch", "dinner"}
        if meal_type not in allowed:
            raise ValueError(f"Invalid meal_type: {meal_type}")
        col = f"{meal_type}_time"
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"UPDATE notifications SET {col} = %s WHERE user_id = %s",
                    (time_str, user_id)
                )
            conn.commit()

    def set_target_confirmation(self, user_id: int, warning_level: str):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO users (user_id, target_weight_warning_level, target_confirmed, target_confirmed_at)
                    VALUES (%s, %s, 1, CURRENT_TIMESTAMP)
                    ON CONFLICT (user_id) DO UPDATE SET
                        target_weight_warning_level = EXCLUDED.target_weight_warning_level,
                        target_confirmed = 1,
                        target_confirmed_at = CURRENT_TIMESTAMP
                """, (user_id, warning_level))
            conn.commit()

    def get_terms_accepted(self, user_id: int) -> bool:
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT terms_accepted FROM users WHERE user_id = %s", (user_id,))
                row = cur.fetchone()
                return bool(row[0]) if row else False

    def set_terms_accepted(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO users (user_id, terms_accepted, terms_accepted_at)
                    VALUES (%s, 1, CURRENT_TIMESTAMP)
                    ON CONFLICT (user_id) DO UPDATE SET
                        terms_accepted = 1,
                        terms_accepted_at = CURRENT_TIMESTAMP
                """, (user_id,))
            conn.commit()

    # ── Subscriptions ─────────────────────────────────────────────

    def get_subscription(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM subscriptions WHERE user_id = %s", (user_id,))
                row = cur.fetchone()
                return dict(row) if row else None

    def init_subscription(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO subscriptions (user_id) VALUES (%s) ON CONFLICT DO NOTHING",
                    (user_id,)
                )
            conn.commit()

    def mark_started(self, user_id: int, source: str = None):
        """Отметка «нажал Start» — вызывается в самом начале start(), до онбординга.
        ON CONFLICT DO NOTHING: у вернувшихся юзеров started_at/source не сдвигаем
        (first-touch: остаётся первое значение / NULL у старых). НЕ трогает onb_step
        и first_seen_at. source — deep-link ?start=<src> (ig / site / NULL=direct)."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO subscriptions (user_id, started_at, source) "
                    "VALUES (%s, CURRENT_TIMESTAMP, %s) ON CONFLICT DO NOTHING",
                    (user_id, source)
                )
            conn.commit()

    def get_profile_prompted(self, user_id: int) -> bool:
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT profile_prompted FROM subscriptions WHERE user_id = %s", (user_id,))
                row = cur.fetchone()
                return bool(row[0]) if row else False

    def set_profile_prompted(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO subscriptions (user_id, profile_prompted) VALUES (%s, TRUE) "
                    "ON CONFLICT (user_id) DO UPDATE SET profile_prompted = TRUE",
                    (user_id,)
                )
            conn.commit()

    def get_reminders_prompted(self, user_id: int) -> bool:
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT reminders_prompted FROM subscriptions WHERE user_id = %s", (user_id,))
                row = cur.fetchone()
                return bool(row[0]) if row else False

    def set_reminders_prompted(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO subscriptions (user_id, reminders_prompted) VALUES (%s, TRUE) "
                    "ON CONFLICT (user_id) DO UPDATE SET reminders_prompted = TRUE",
                    (user_id,)
                )
            conn.commit()

    def has_access(self, user_id: int) -> bool:
        sub = self.get_subscription(user_id)
        if not sub:
            self.init_subscription(user_id)
            return True
        if sub["sub_expires_at"]:
            exp = sub["sub_expires_at"]
            if isinstance(exp, str):
                exp = datetime.fromisoformat(exp)
            if exp > datetime.now():
                return True
        return sub["free_analyses_used"] < FREE_ANALYSES_LIMIT

    def is_paid_active(self, user_id: int) -> bool:
        sub = self.get_subscription(user_id)
        if not sub or not sub["sub_expires_at"]:
            return False
        exp = sub["sub_expires_at"]
        if isinstance(exp, str):
            exp = datetime.fromisoformat(exp)
        return exp > datetime.now()

    def reserve_free_analysis(self, user_id: int) -> bool:
        """Атомарно занимает один бесплатный анализ ДО запуска AI.
        False — лимит уже исчерпан. Условие в UPDATE закрывает гонку:
        два параллельных фото при одном оставшемся скане не спишут два."""
        self.init_subscription(user_id)
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE subscriptions SET free_analyses_used = free_analyses_used + 1 "
                    "WHERE user_id = %s AND free_analyses_used < %s",
                    (user_id, FREE_ANALYSES_LIMIT)
                )
                reserved = cur.rowcount > 0
                if reserved:
                    cur.execute(
                        "UPDATE subscriptions SET trial_ended_at = NOW() "
                        "WHERE user_id = %s AND free_analyses_used >= %s AND trial_ended_at IS NULL",
                        (user_id, FREE_ANALYSES_LIMIT)
                    )
            conn.commit()
        return reserved

    def refund_free_analysis(self, user_id: int):
        """Возвращает скан, зарезервированный reserve_free_analysis,
        если анализ не удался. Снимает trial_ended_at, если резерв
        только что довёл счётчик до лимита."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE subscriptions SET "
                    "  free_analyses_used = GREATEST(free_analyses_used - 1, 0), "
                    "  trial_ended_at = CASE WHEN free_analyses_used - 1 < %s "
                    "                        THEN NULL ELSE trial_ended_at END "
                    "WHERE user_id = %s",
                    (FREE_ANALYSES_LIMIT, user_id)
                )
            conn.commit()

    def bump_onb_step(self, user_id: int, step: int):
        """Запоминает самый дальний шаг онбординга (не уменьшается)."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE subscriptions SET onb_step = GREATEST(onb_step, %s) WHERE user_id = %s",
                    (step, user_id)
                )
            conn.commit()

    def increment_photo_analyses(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE subscriptions SET photo_analyses = photo_analyses + 1 WHERE user_id = %s",
                    (user_id,)
                )
            conn.commit()

    def get_free_analyses_left(self, user_id: int) -> int:
        sub = self.get_subscription(user_id)
        if not sub:
            return FREE_ANALYSES_LIMIT
        return max(0, FREE_ANALYSES_LIMIT - sub["free_analyses_used"])

    def activate_subscription(self, user_id: int, months: int):
        sub = self.get_subscription(user_id)
        if sub and sub["sub_expires_at"]:
            try:
                current = sub["sub_expires_at"]
                if isinstance(current, str):
                    current = datetime.fromisoformat(current)
                base = current if current > datetime.now() else datetime.now()
            except (ValueError, TypeError):
                base = datetime.now()
        else:
            base = datetime.now()
        new_expiry = base + timedelta(days=30 * months)
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO subscriptions (user_id, sub_expires_at)
                    VALUES (%s, %s)
                    ON CONFLICT (user_id) DO UPDATE SET sub_expires_at = EXCLUDED.sub_expires_at
                """, (user_id, new_expiry))
            conn.commit()

    def gift_access(self, user_id: int):
        """Выдаёт пользователю бессрочный доступ (до 2099 года)."""
        forever = datetime(2099, 1, 1)
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO subscriptions (user_id, sub_expires_at)
                    VALUES (%s, %s)
                    ON CONFLICT (user_id) DO UPDATE SET sub_expires_at = EXCLUDED.sub_expires_at
                """, (user_id, forever))
            conn.commit()

    def get_subscription_stats(self) -> dict:
        now = datetime.now()
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM subscriptions")
                total = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM subscriptions WHERE sub_expires_at > %s", (now,))
                paid = cur.fetchone()[0]
                cur.execute(
                    "SELECT COUNT(*) FROM subscriptions "
                    "WHERE (sub_expires_at IS NULL OR sub_expires_at <= %s) "
                    "AND free_analyses_used < %s",
                    (now, FREE_ANALYSES_LIMIT)
                )
                on_trial = cur.fetchone()[0]
                cur.execute(
                    "SELECT COUNT(*) FROM subscriptions "
                    "WHERE (sub_expires_at IS NULL OR sub_expires_at <= %s) "
                    "AND free_analyses_used >= %s",
                    (now, FREE_ANALYSES_LIMIT)
                )
                expired = cur.fetchone()[0]
                cur.execute(
                    "SELECT COUNT(*) FROM subscriptions WHERE free_analyses_used >= 10"
                )
                used_10plus = cur.fetchone()[0]

                # Новые за сегодня
                cur.execute(
                    "SELECT COUNT(*) FROM users WHERE first_seen_at >= CURRENT_DATE"
                )
                new_today = cur.fetchone()[0]

                # Новые за 7 дней
                cur.execute(
                    "SELECT COUNT(*) FROM users WHERE first_seen_at >= CURRENT_DATE - INTERVAL '7 days'"
                )
                new_7d = cur.fetchone()[0]

                # Всего пользователей (принявших условия)
                cur.execute("SELECT COUNT(*) FROM users WHERE terms_accepted = 1")
                total_users = cur.fetchone()[0]

                # Активных вчера (для retention)
                cur.execute(
                    "SELECT COUNT(DISTINCT user_id) FROM meals "
                    "WHERE day = TO_CHAR(CURRENT_DATE - INTERVAL '1 day', 'YYYY-MM-DD')"
                )
                active_yesterday = cur.fetchone()[0]

                # Активных сегодня
                cur.execute(
                    "SELECT COUNT(DISTINCT user_id) FROM meals WHERE day = TO_CHAR(CURRENT_DATE, 'YYYY-MM-DD')"
                )
                active_today = cur.fetchone()[0]

                # Всего анализов фото
                cur.execute("SELECT COALESCE(SUM(photo_analyses), 0) FROM subscriptions")
                total_photos = cur.fetchone()[0]

                # Топ языков
                cur.execute(
                    "SELECT COALESCE(NULLIF(language, 'auto'), tg_language, 'auto'), COUNT(*) FROM users "
                    "GROUP BY COALESCE(NULLIF(language, 'auto'), tg_language, 'auto') ORDER BY COUNT(*) DESC LIMIT 5"
                )
                top_langs = cur.fetchall()

                # D1 retention: зарегистрировались 2+ дней назад, вернулись на следующий день
                cur.execute("""
                    SELECT
                        COUNT(DISTINCT u.user_id) FILTER (
                            WHERE EXISTS (
                                SELECT 1 FROM meals m
                                WHERE m.user_id = u.user_id
                                  AND m.day::date >= u.first_seen_at::date + INTERVAL '1 day'
                                  AND m.day::date <= u.first_seen_at::date + INTERVAL '2 days'
                            )
                        ) AS retained,
                        COUNT(DISTINCT u.user_id) AS cohort
                    FROM users u
                    WHERE u.first_seen_at < CURRENT_DATE - INTERVAL '1 day'
                      AND EXISTS (SELECT 1 FROM meals m2 WHERE m2.user_id = u.user_id)
                """)
                row = cur.fetchone()
                retained_d1, cohort_d1 = row[0], row[1]

                # D7 retention: зарегистрировались 7+ дней назад, были активны на 2–7 день
                cur.execute("""
                    SELECT
                        COUNT(DISTINCT u.user_id) FILTER (
                            WHERE EXISTS (
                                SELECT 1 FROM meals m
                                WHERE m.user_id = u.user_id
                                  AND m.day::date >= u.first_seen_at::date + INTERVAL '2 days'
                                  AND m.day::date <= u.first_seen_at::date + INTERVAL '7 days'
                            )
                        ) AS retained,
                        COUNT(DISTINCT u.user_id) AS cohort
                    FROM users u
                    WHERE u.first_seen_at < CURRENT_DATE - INTERVAL '7 days'
                      AND EXISTS (SELECT 1 FROM meals m2 WHERE m2.user_id = u.user_id)
                """)
                row = cur.fetchone()
                retained_d7, cohort_d7 = row[0], row[1]

                # D30 retention: зарегистрировались 30+ дней назад, были активны на 8–30 день
                cur.execute("""
                    SELECT
                        COUNT(DISTINCT u.user_id) FILTER (
                            WHERE EXISTS (
                                SELECT 1 FROM meals m
                                WHERE m.user_id = u.user_id
                                  AND m.day::date >= u.first_seen_at::date + INTERVAL '8 days'
                                  AND m.day::date <= u.first_seen_at::date + INTERVAL '30 days'
                            )
                        ) AS retained,
                        COUNT(DISTINCT u.user_id) AS cohort
                    FROM users u
                    WHERE u.first_seen_at < CURRENT_DATE - INTERVAL '30 days'
                      AND EXISTS (SELECT 1 FROM meals m2 WHERE m2.user_id = u.user_id)
                """)
                row = cur.fetchone()
                retained_d30, cohort_d30 = row[0], row[1]

                retained_7d = retained_d7
                cohort_7d = cohort_d7

                # Пользователей с streak >= 3 дня подряд
                cur.execute("""
                    WITH user_days AS (
                        SELECT user_id, day::date AS d
                        FROM meals
                        GROUP BY user_id, day::date
                    ),
                    streaks AS (
                        SELECT user_id, d,
                               d - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY d)::int AS grp
                        FROM user_days
                    ),
                    streak_lengths AS (
                        SELECT user_id, COUNT(*) AS streak_len
                        FROM streaks
                        GROUP BY user_id, grp
                    )
                    SELECT COUNT(DISTINCT user_id) FROM streak_lengths WHERE streak_len >= 3
                """)
                users_with_streak_3 = cur.fetchone()[0]

                # Среднее кол-во активных дней на пользователя
                cur.execute("""
                    SELECT ROUND(AVG(cnt)::numeric, 1)
                    FROM (
                        SELECT user_id, COUNT(DISTINCT day) AS cnt FROM meals GROUP BY user_id
                    ) t
                """)
                avg_active_days = cur.fetchone()[0] or 0

                # Пиковые часы активности (топ-3)
                cur.execute("""
                    SELECT EXTRACT(HOUR FROM created_at)::int AS hr, COUNT(*) AS cnt
                    FROM meals
                    GROUP BY hr ORDER BY cnt DESC LIMIT 3
                """)
                peak_hours = cur.fetchall()

                # Среднее приёмов еды в день у активных пользователей
                cur.execute("""
                    SELECT ROUND(AVG(daily_meals)::numeric, 1)
                    FROM (
                        SELECT user_id, day, COUNT(*) AS daily_meals
                        FROM meals GROUP BY user_id, day
                    ) t
                """)
                avg_meals_per_day = cur.fetchone()[0] or 0

                # Пользователей активных 3+ дней (зацепило)
                cur.execute("""
                    SELECT COUNT(*) FROM (
                        SELECT user_id FROM meals
                        GROUP BY user_id HAVING COUNT(DISTINCT day) >= 3
                    ) t
                """)
                hooked_users = cur.fetchone()[0]

        return {
            "total": total,
            "paid": paid,
            "on_trial": on_trial,
            "expired": expired,
            "new_today": new_today,
            "new_7d": new_7d,
            "total_users": total_users,
            "active_today": active_today,
            "active_yesterday": active_yesterday,
            "total_photos": total_photos,
            "top_langs": top_langs,
            "retained_7d": retained_7d,
            "cohort_7d": cohort_7d,
            "users_with_streak_3": users_with_streak_3,
            "avg_active_days": avg_active_days,
            "peak_hours": peak_hours,
            "avg_meals_per_day": avg_meals_per_day,
            "hooked_users": hooked_users,
            "used_10plus": used_10plus,
            "retained_d1": retained_d1, "cohort_d1": cohort_d1,
            "retained_d7": retained_d7, "cohort_d7": cohort_d7,
            "retained_d30": retained_d30, "cohort_d30": cohort_d30,
        }

    def get_user_language(self, user_id: int) -> str:
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT language FROM users WHERE user_id = %s", (user_id,))
                row = cur.fetchone()
                return row[0] if row and row[0] else "auto"

    def set_tg_language(self, user_id: int, tg_lang: str):
        # Upsert: у нового юзера строки в users ещё нет (появляется на первом
        # шаге онбординга), UPDATE был бы молчаливым no-op. First-touch:
        # уже записанный tg_language не перетираем.
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO users (user_id, tg_language) VALUES (%s, %s)
                    ON CONFLICT (user_id) DO UPDATE SET
                        tg_language = COALESCE(users.tg_language, EXCLUDED.tg_language)
                """, (user_id, tg_lang))
            conn.commit()

    def set_user_language(self, user_id: int, lang: str):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO users (user_id, language) VALUES (%s, %s)
                    ON CONFLICT (user_id) DO UPDATE SET language = EXCLUDED.language
                """, (user_id, lang))
            conn.commit()

    def get_all_notification_users(self) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("""
                    SELECT * FROM notifications
                    WHERE breakfast_enabled = 1 OR lunch_enabled = 1 OR dinner_enabled = 1
                """)
                return [dict(row) for row in cur.fetchall()]
