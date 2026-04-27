import os
from datetime import datetime, timedelta
from typing import List, Dict, Any

import psycopg2
import psycopg2.extras

FREE_ANALYSES_LIMIT = 15


class Database:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self._init_db()

    def _conn(self):
        return psycopg2.connect(self.database_url)

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
                    SELECT id, food_description, calories, protein, fat, carbs, time
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

    def update_meal_by_id(self, meal_id: int, user_id: int, food_description: str,
                          calories: int, protein: int, fat: int, carbs: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE meals
                    SET food_description = %s, calories = %s, protein = %s, fat = %s, carbs = %s
                    WHERE id = %s AND user_id = %s
                """, (food_description, calories, protein, fat, carbs, meal_id, user_id))
            conn.commit()

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
                    WHERE user_id = %s AND day >= (CURRENT_DATE - INTERVAL '7 days')::TEXT
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
        """Пользователи, зарегистрированные 2+ дня назад, которым ещё не отправлен тип про вес."""
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("""
                    SELECT u.user_id, COALESCE(n.timezone_offset, 3) as timezone_offset
                    FROM users u
                    LEFT JOIN notifications n ON n.user_id = u.user_id
                    WHERE u.terms_accepted = 1
                      AND u.terms_accepted_at <= NOW() - INTERVAL '1 day'
                      AND u.weight_tip_sent = 0
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

    def use_free_analysis(self, user_id: int):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE subscriptions SET free_analyses_used = free_analyses_used + 1 WHERE user_id = %s",
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
        return {"total": total, "paid": paid, "on_trial": on_trial, "expired": expired}

    def get_all_notification_users(self) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("""
                    SELECT * FROM notifications
                    WHERE breakfast_enabled = 1 OR lunch_enabled = 1 OR dinner_enabled = 1
                """)
                return [dict(row) for row in cur.fetchall()]
