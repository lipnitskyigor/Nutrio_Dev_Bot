import sqlite3
from datetime import datetime, timedelta
from typing import List, Dict, Any

FREE_ANALYSES_LIMIT = 15


class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS meals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
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
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_user_day ON meals(user_id, day)
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS goals (
                    user_id INTEGER PRIMARY KEY,
                    calories INTEGER NOT NULL DEFAULT 2000,
                    protein INTEGER NOT NULL DEFAULT 100,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS weight_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    weight REAL NOT NULL,
                    day TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS weight_goal (
                    user_id INTEGER PRIMARY KEY,
                    target_weight REAL NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS profiles (
                    user_id INTEGER PRIMARY KEY,
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
            conn.execute("""
                CREATE TABLE IF NOT EXISTS notifications (
                    user_id INTEGER PRIMARY KEY,
                    breakfast_enabled INTEGER NOT NULL DEFAULT 1,
                    breakfast_time TEXT NOT NULL DEFAULT '09:00',
                    lunch_enabled INTEGER NOT NULL DEFAULT 1,
                    lunch_time TEXT NOT NULL DEFAULT '13:00',
                    dinner_enabled INTEGER NOT NULL DEFAULT 1,
                    dinner_time TEXT NOT NULL DEFAULT '19:00',
                    timezone_offset INTEGER NOT NULL DEFAULT 3
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    terms_accepted INTEGER NOT NULL DEFAULT 0,
                    terms_accepted_at TIMESTAMP,
                    target_weight_warning_level TEXT,
                    target_confirmed INTEGER DEFAULT 0,
                    target_confirmed_at TIMESTAMP
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS subscriptions (
                    user_id INTEGER PRIMARY KEY,
                    free_analyses_used INTEGER NOT NULL DEFAULT 0,
                    sub_expires_at TIMESTAMP,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            for col_def in [
                "ALTER TABLE users ADD COLUMN target_weight_warning_level TEXT",
                "ALTER TABLE users ADD COLUMN target_confirmed INTEGER DEFAULT 0",
                "ALTER TABLE users ADD COLUMN target_confirmed_at TIMESTAMP",
            ]:
                try:
                    conn.execute(col_def)
                except sqlite3.OperationalError:
                    pass
            conn.commit()

    def get_profile(self, user_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT * FROM profiles WHERE user_id = ?", (user_id,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    def set_profile(self, user_id: int, goal: str, sex: str, age: int,
                    height: int, weight: float, daily_calories: int,
                    target_cal_low: int, target_cal_high: int, activity: str = "moderate"):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO profiles
                    (user_id, goal, sex, age, height, weight, activity, daily_calories, target_cal_low, target_cal_high)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET
                    goal = excluded.goal, sex = excluded.sex, age = excluded.age,
                    height = excluded.height, weight = excluded.weight,
                    activity = excluded.activity,
                    daily_calories = excluded.daily_calories,
                    target_cal_low = excluded.target_cal_low,
                    target_cal_high = excluded.target_cal_high
            """, (user_id, goal, sex, age, height, weight, activity,
                  daily_calories, target_cal_low, target_cal_high))
            conn.commit()

    def add_meal(
        self,
        user_id: int,
        day: str,
        time: str,
        food_description: str,
        calories: int,
        protein: int,
        fat: int,
        carbs: int,
    ) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                """
                INSERT INTO meals (user_id, day, time, food_description, calories, protein, fat, carbs)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (user_id, day, time, food_description, calories, protein, fat, carbs),
            )
            conn.commit()
            return cursor.lastrowid

    def get_meals_for_day(self, user_id: int, day: str) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                """
                SELECT food_description, calories, protein, fat, carbs, time
                FROM meals
                WHERE user_id = ? AND day = ?
                ORDER BY created_at ASC
                """,
                (user_id, day),
            )
            return [dict(row) for row in cursor.fetchall()]

    def get_meals_for_day_with_ids(self, user_id: int, day: str) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                """
                SELECT id, food_description, calories, protein, fat, carbs, time
                FROM meals
                WHERE user_id = ? AND day = ?
                ORDER BY created_at ASC
                """,
                (user_id, day),
            )
            return [dict(row) for row in cursor.fetchall()]

    def get_meal_by_id(self, meal_id: int, user_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT * FROM meals WHERE id = ? AND user_id = ?",
                (meal_id, user_id),
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    def delete_meal_by_id(self, meal_id: int, user_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "DELETE FROM meals WHERE id = ? AND user_id = ?",
                (meal_id, user_id),
            )
            conn.commit()

    def update_meal_by_id(self, meal_id: int, user_id: int, food_description: str,
                          calories: int, protein: int, fat: int, carbs: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                UPDATE meals
                SET food_description = ?, calories = ?, protein = ?, fat = ?, carbs = ?
                WHERE id = ? AND user_id = ?
                """,
                (food_description, calories, protein, fat, carbs, meal_id, user_id),
            )
            conn.commit()

    def get_weekly_summary(self, user_id: int) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                """
                SELECT
                    day,
                    SUM(calories) as total_calories,
                    SUM(protein) as total_protein,
                    SUM(fat) as total_fat,
                    SUM(carbs) as total_carbs,
                    COUNT(*) as meals_count
                FROM meals
                WHERE user_id = ?
                  AND day >= date('now', '-7 days')
                GROUP BY day
                ORDER BY day DESC
                """,
                (user_id,),
            )
            return [dict(row) for row in cursor.fetchall()]

    def set_goal(self, user_id: int, calories: int, protein: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT INTO goals (user_id, calories, protein)
                VALUES (?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET
                    calories = excluded.calories,
                    protein = excluded.protein,
                    updated_at = CURRENT_TIMESTAMP
                """,
                (user_id, calories, protein),
            )
            conn.commit()

    def get_goal(self, user_id: int) -> Dict[str, Any]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT calories, protein FROM goals WHERE user_id = ?",
                (user_id,),
            )
            row = cursor.fetchone()
            if row:
                return dict(row)
            return None

    def log_weight(self, user_id: int, weight: float):
        today = __import__('datetime').date.today().isoformat()
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO weight_log (user_id, weight, day) VALUES (?, ?, ?)",
                (user_id, weight, today),
            )
            conn.commit()

    def get_latest_weight(self, user_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT weight, day FROM weight_log WHERE user_id = ? ORDER BY created_at DESC LIMIT 1",
                (user_id,),
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    def set_weight_goal(self, user_id: int, target_weight: float):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """INSERT INTO weight_goal (user_id, target_weight)
                   VALUES (?, ?)
                   ON CONFLICT(user_id) DO UPDATE SET target_weight = excluded.target_weight, updated_at = CURRENT_TIMESTAMP""",
                (user_id, target_weight),
            )
            conn.commit()

    def get_weight_goal(self, user_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT target_weight FROM weight_goal WHERE user_id = ?",
                (user_id,),
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    def get_weight_history(self, user_id: int, days: int = 7) -> List[Dict[str, Any]]:
        """Последние N записей веса для отслеживания прогресса."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                """
                SELECT weight, day FROM weight_log
                WHERE user_id = ?
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (user_id, days),
            )
            rows = cursor.fetchall()
            return [dict(r) for r in reversed(rows)]  # от старых к новым

    def delete_meals_for_day(self, user_id: int, day: str):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "DELETE FROM meals WHERE user_id = ? AND day = ?",
                (user_id, day),
            )
            conn.commit()

    # ── Notifications ─────────────────────────────────────────────

    def get_notifications(self, user_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT * FROM notifications WHERE user_id = ?", (user_id,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    def get_or_create_notifications(self, user_id: int) -> dict:
        notif = self.get_notifications(user_id)
        if not notif:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    "INSERT OR IGNORE INTO notifications (user_id) VALUES (?)",
                    (user_id,)
                )
                conn.commit()
            notif = self.get_notifications(user_id)
        return notif

    def save_notifications(self, user_id: int, breakfast_enabled: int,
                           lunch_enabled: int, dinner_enabled: int,
                           timezone_offset: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO notifications
                    (user_id, breakfast_enabled, lunch_enabled, dinner_enabled, timezone_offset)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET
                    breakfast_enabled = excluded.breakfast_enabled,
                    lunch_enabled     = excluded.lunch_enabled,
                    dinner_enabled    = excluded.dinner_enabled,
                    timezone_offset   = excluded.timezone_offset
            """, (user_id, breakfast_enabled, lunch_enabled, dinner_enabled, timezone_offset))
            conn.commit()

    def set_target_confirmation(self, user_id: int, warning_level: str):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO users (user_id, target_weight_warning_level, target_confirmed, target_confirmed_at)
                VALUES (?, ?, 1, CURRENT_TIMESTAMP)
                ON CONFLICT(user_id) DO UPDATE SET
                    target_weight_warning_level = excluded.target_weight_warning_level,
                    target_confirmed = 1,
                    target_confirmed_at = CURRENT_TIMESTAMP
            """, (user_id, warning_level))
            conn.commit()

    def get_terms_accepted(self, user_id: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT terms_accepted FROM users WHERE user_id = ?", (user_id,)
            )
            row = cursor.fetchone()
            return bool(row[0]) if row else False

    def set_terms_accepted(self, user_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO users (user_id, terms_accepted, terms_accepted_at)
                VALUES (?, 1, CURRENT_TIMESTAMP)
                ON CONFLICT(user_id) DO UPDATE SET
                    terms_accepted = 1,
                    terms_accepted_at = CURRENT_TIMESTAMP
            """, (user_id,))
            conn.commit()

    def save_notification_time(self, user_id: int, meal_type: str, time_str: str):
        col = f"{meal_type}_time"
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                f"UPDATE notifications SET {col} = ? WHERE user_id = ?",
                (time_str, user_id)
            )
            conn.commit()

    # ── Subscriptions ─────────────────────────────────────────────

    def get_subscription(self, user_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT * FROM subscriptions WHERE user_id = ?", (user_id,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    def init_subscription(self, user_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR IGNORE INTO subscriptions (user_id) VALUES (?)",
                (user_id,)
            )
            conn.commit()

    def has_access(self, user_id: int) -> bool:
        sub = self.get_subscription(user_id)
        if not sub:
            self.init_subscription(user_id)
            return True
        if sub["sub_expires_at"]:
            if datetime.fromisoformat(sub["sub_expires_at"]) > datetime.now():
                return True
        return sub["free_analyses_used"] < FREE_ANALYSES_LIMIT

    def is_paid_active(self, user_id: int) -> bool:
        sub = self.get_subscription(user_id)
        if not sub or not sub["sub_expires_at"]:
            return False
        return datetime.fromisoformat(sub["sub_expires_at"]) > datetime.now()

    def use_free_analysis(self, user_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "UPDATE subscriptions SET free_analyses_used = free_analyses_used + 1 WHERE user_id = ?",
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
                current = datetime.fromisoformat(sub["sub_expires_at"])
                base = current if current > datetime.now() else datetime.now()
            except (ValueError, TypeError):
                base = datetime.now()
        else:
            base = datetime.now()
        new_expiry = base + timedelta(days=30 * months)
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO subscriptions (user_id, sub_expires_at)
                VALUES (?, ?)
                ON CONFLICT(user_id) DO UPDATE SET sub_expires_at = excluded.sub_expires_at
            """, (user_id, new_expiry.isoformat()))
            conn.commit()

    def get_subscription_stats(self) -> dict:
        now = datetime.now().isoformat()
        with sqlite3.connect(self.db_path) as conn:
            total = conn.execute(
                "SELECT COUNT(*) FROM subscriptions"
            ).fetchone()[0]
            paid = conn.execute(
                "SELECT COUNT(*) FROM subscriptions WHERE sub_expires_at > ?", (now,)
            ).fetchone()[0]
            on_trial = conn.execute(
                "SELECT COUNT(*) FROM subscriptions "
                "WHERE (sub_expires_at IS NULL OR sub_expires_at <= ?) "
                "AND free_analyses_used < ?",
                (now, FREE_ANALYSES_LIMIT)
            ).fetchone()[0]
            expired = conn.execute(
                "SELECT COUNT(*) FROM subscriptions "
                "WHERE (sub_expires_at IS NULL OR sub_expires_at <= ?) "
                "AND free_analyses_used >= ?",
                (now, FREE_ANALYSES_LIMIT)
            ).fetchone()[0]
        return {"total": total, "paid": paid, "on_trial": on_trial, "expired": expired}

    def get_all_notification_users(self) -> List[Dict[str, Any]]:
        """Возвращает всех пользователей с хотя бы одним активным напоминанием."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("""
                SELECT * FROM notifications
                WHERE breakfast_enabled = 1 OR lunch_enabled = 1 OR dinner_enabled = 1
            """)
            return [dict(row) for row in cursor.fetchall()]
