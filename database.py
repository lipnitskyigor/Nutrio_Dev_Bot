import sqlite3
from typing import List, Dict, Any


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
