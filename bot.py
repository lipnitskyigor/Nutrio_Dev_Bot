import os
import json
import base64
import logging
import asyncio
import sqlite3
from datetime import datetime, date
from io import BytesIO

import anthropic
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)

from database import Database

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
ADMIN_ID = 148160233

DB_PATH = os.environ.get("DB_PATH", "/app/data/calories.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
db = Database(DB_PATH)
claude = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


def analyze_food_text(text: str) -> dict:
    """Send food description to Claude and get calorie analysis."""
    response = claude.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""Ты эксперт по питанию. Пользователь описал что поел: "{text}"

Рассчитай примерную калорийность и КБЖУ.

Ответь СТРОГО в формате JSON (без markdown, без ```json, только чистый JSON):
{{
  "food_description": "что именно съел (понятное описание на русском)",
  "calories": число (примерное количество ккал),
  "protein": число (белки в граммах),
  "fat": число (жиры в граммах),
  "carbs": число (углеводы в граммах),
  "comment": "короткий комментарий (на русском, 1-2 предложения)"
}}

Если текст не про еду, верни: {{"error": "Не понял что это за еда. Опиши подробнее или пришли фото!"}}
Все числа — целые, без дробей."""
            }
        ],
    )

    raw = response.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())


def analyze_food_image(image_bytes: bytes, caption: str = None) -> dict:
    """Send image to Claude and get calorie analysis."""
    image_b64 = base64.standard_b64encode(image_bytes).decode("utf-8")

    caption_hint = f'\nПользователь также написал: "{caption}"' if caption else ""

    response = claude.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image_b64,
                        },
                    },
                    {
                        "type": "text",
                        "text": f"""Ты эксперт по питанию. Проанализируй еду на фото и дай оценку калорийности.{caption_hint}

Ответь СТРОГО в формате JSON (без markdown, без ```json, только чистый JSON):
{{
  "food_description": "что именно на фото (на русском)",
  "calories": число (примерное количество ккал),
  "protein": число (белки в граммах),
  "fat": число (жиры в граммах),
  "carbs": число (углеводы в граммах),
  "comment": "короткий комментарий о блюде (на русском, 1-2 предложения)"
}}

Если на фото нет еды, верни: {{"error": "На фото нет еды"}}
Все числа — целые, без дробей."""
                    }
                ],
            }
        ],
    )

    raw = response.content[0].text.strip()
    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())


def _calc_calories(sex: str, age: int, height: int, weight: float, goal: str):
    """Mifflin-St Jeor + moderate activity (1.55). Returns (tdee, low, high)."""
    if sex == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    tdee = bmr * 1.55
    if goal == "lose":
        center = tdee * 0.80
    elif goal == "gain":
        center = tdee * 1.15
    else:
        center = tdee
    # Round to nearest 50 for "approximate" feel
    low  = round((center - 100) / 50) * 50
    high = round((center + 100) / 50) * 50
    daily = round(tdee / 50) * 50
    return int(daily), int(low), int(high)


def _goal_label(goal: str) -> str:
    return {"lose": "похудеть", "maintain": "держать вес", "gain": "набрать массу"}.get(goal, goal)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or "друг"
    user_id = user.id

    profile = db.get_profile(user_id)
    meals = db.get_meals_for_day(user_id, date.today().isoformat())

    if profile or meals:
        # Returning user
        await update.message.reply_text(
            f"С возвращением, {name}! 👋\n\n"
            "📸 Отправь фото еды или напиши что поел — посчитаю.\n\n"
            "/today — итог за сегодня\n"
            "/help — все команды",
            parse_mode="Markdown"
        )
    else:
        # New user — onboarding
        await update.message.reply_text(
            f"Привет, {name}! 👋\n\n"
            "Я считаю калории по фото еды — просто, быстро, без ручного ввода.\n\n"
            "📸 *Отправь фото любого блюда*\n"
            "✏️ Или напиши что поел\n\n"
            "Попробуй прямо сейчас ↓",
            parse_mode="Markdown"
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Как пользоваться ботом:*\n\n"
        "📸 Отправь фото еды — посчитаю калории и КБЖУ\n"
        "✏️ Напиши что поел — тоже посчитаю\n"
        "Например: _«гречка с курицей 300г»_\n\n"
        "📊 *Калории и питание:*\n"
        "/today — итог за сегодня (калории, белки, жиры, углеводы)\n"
        "/history — история питания за последние 7 дней\n"
        "/goal 2000 150 — установить дневную цель по ккал и белку\n"
        "/goal — посмотреть текущую цель\n"
        "/reset — сбросить записи за сегодня\n\n"
        "⚖️ *Вес и прогресс:*\n"
        "/weight 80.5 — записать вес (делай каждый день)\n"
        "/weight — посмотреть последний записанный вес\n"
        "/target 75 — установить целевой вес\n"
        "/target — посмотреть целевой вес и сколько осталось\n"
        "/progress — динамика веса за 7 дней с 🟢🔴 изменениями\n\n"
        "💡 Совет: чем чётче видна еда на фото, тем точнее результат!",
        parse_mode="Markdown"
    )


async def today_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_name = update.effective_user.first_name or "Пользователь"
    today = date.today().isoformat()

    meals = db.get_meals_for_day_with_ids(user_id, today)

    if not meals:
        await update.message.reply_text(
            "📭 Сегодня ещё нет записей о еде.\n"
            "Отправь фото блюда, чтобы начать считать!"
        )
        return

    total_cal = sum(m["calories"] for m in meals)
    total_protein = sum(m["protein"] for m in meals)
    total_fat = sum(m["fat"] for m in meals)
    total_carbs = sum(m["carbs"] for m in meals)

    lines = [f"📊 *Итог за сегодня — {user_name}*\n"]
    for i, meal in enumerate(meals, 1):
        t = meal["time"]
        lines.append(f"{i}. {meal['food_description']} — {meal['calories']} ккал ({t})")

    lines.append(f"\n🔥 *Итого: {total_cal} ккал*")
    lines.append(f"🥩 Белки: {total_protein} г  🧈 Жиры: {total_fat} г  🍞 Углеводы: {total_carbs} г")
    lines.append(f"\n✏️ Удалить: `/delete 2` | Изменить: `/edit 2 борщ 400г`")

    await update.message.reply_text("\n".join(lines), parse_mode="Markdown")


async def history_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_name = update.effective_user.first_name or "Пользователь"

    history = db.get_weekly_summary(user_id)

    if not history:
        await update.message.reply_text(
            "📭 Нет данных за последние 7 дней.\n"
            "Отправь фото еды, чтобы начать!"
        )
        return

    lines = [f"📅 *История за 7 дней — {user_name}*\n"]
    for entry in history:
        day = entry["day"]
        cal = entry["total_calories"]
        meals_count = entry["meals_count"]
        # Format date nicely
        try:
            d = datetime.strptime(day, "%Y-%m-%d")
            day_str = d.strftime("%-d %b")
        except Exception:
            day_str = day
        lines.append(f"📆 {day_str}: *{cal} ккал* ({meals_count} приём{'ов' if meals_count != 1 else 'а'} пищи)")

    await update.message.reply_text("\n".join(lines), parse_mode="Markdown")


async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    today = date.today().isoformat()
    db.delete_meals_for_day(user_id, today)
    await update.message.reply_text("🗑️ Данные за сегодня сброшены!")


async def goal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not context.args:
        goal = db.get_goal(user_id)
        if goal:
            await update.message.reply_text(
                f"🎯 *Твоя цель на день:*\n"
                f"🔥 Калории: {goal['calories']} ккал\n"
                f"🥩 Белок: {goal['protein']} г\n\n"
                f"Чтобы изменить: `/goal 2000 150`",
                parse_mode="Markdown"
            )
        else:
            await update.message.reply_text(
                "🎯 Цель не установлена.\n\n"
                "Установи так: `/goal калории белок`\n"
                "Например: `/goal 2000 150`",
                parse_mode="Markdown"
            )
        return

    try:
        calories = int(context.args[0])
        protein = int(context.args[1]) if len(context.args) > 1 else 100
        db.set_goal(user_id, calories, protein)
        await update.message.reply_text(
            f"✅ *Цель установлена!*\n"
            f"🔥 Калории: {calories} ккал/день\n"
            f"🥩 Белок: {protein} г/день",
            parse_mode="Markdown"
        )
    except (ValueError, IndexError):
        await update.message.reply_text(
            "❌ Неверный формат. Используй: `/goal 2000 150`",
            parse_mode="Markdown"
        )


async def weight_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not context.args:
        latest = db.get_latest_weight(user_id)
        if latest:
            await update.message.reply_text(
                f"⚖️ *Последний вес:* {latest['weight']} кг ({latest['day']})\n\n"
                f"Чтобы записать новый: `/weight 80.5`",
                parse_mode="Markdown"
            )
        else:
            await update.message.reply_text(
                "⚖️ Вес ещё не записан.\n\n"
                "Запиши так: `/weight 80.5`",
                parse_mode="Markdown"
            )
        return

    try:
        weight = float(context.args[0].replace(",", "."))
        db.log_weight(user_id, weight)

        response = f"⚖️ *Вес записан:* {weight} кг\n"

        target = db.get_weight_goal(user_id)
        if target:
            target_w = target["target_weight"]
            diff = weight - target_w
            if diff > 0:
                response += f"\n🎯 До цели ({target_w} кг): осталось *{diff:.1f} кг*\n"
                if diff <= 2:
                    response += "💪 Совсем чуть-чуть! Ты почти у цели!"
                elif diff <= 5:
                    response += "🔥 Отличный прогресс, продолжай в том же духе!"
                else:
                    response += "💪 Хороший старт! Каждый день приближает тебя к цели."
            elif diff < 0:
                response += f"\n🏆 Цель достигнута! Ты на {abs(diff):.1f} кг ниже целевого веса!"
            else:
                response += "\n🎯 Ты точно на целевом весе! Отлично!"
        else:
            response += "\n💡 Установи целевой вес командой `/target 75`"

        await update.message.reply_text(response, parse_mode="Markdown")

    except ValueError:
        await update.message.reply_text(
            "❌ Неверный формат. Используй: `/weight 80.5`",
            parse_mode="Markdown"
        )


async def progress_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    history = db.get_weight_history(user_id, days=7)

    if not history:
        await update.message.reply_text(
            "⚖️ Нет данных о весе.\n\n"
            "Записывай вес каждый день командой `/weight 80.5` — буду показывать динамику!",
            parse_mode="Markdown"
        )
        return

    target = db.get_weight_goal(user_id)
    target_w = target["target_weight"] if target else None

    lines = ["📈 *Динамика веса:*\n"]
    for i, entry in enumerate(history):
        w = entry["weight"]
        try:
            d = datetime.strptime(entry["day"], "%Y-%m-%d")
            day_str = d.strftime("%-d %b")
        except Exception:
            day_str = entry["day"]

        if i == 0:
            lines.append(f"📅 {day_str}: *{w} кг*")
        else:
            prev = history[i - 1]["weight"]
            diff = w - prev
            if diff < 0:
                arrow = f"🟢 {diff:.1f} кг"
            elif diff > 0:
                arrow = f"🔴 +{diff:.1f} кг"
            else:
                arrow = "➡️ без изменений"
            lines.append(f"📅 {day_str}: *{w} кг* ({arrow})")

    if len(history) >= 2:
        total_diff = history[-1]["weight"] - history[0]["weight"]
        if total_diff < 0:
            lines.append(f"\n📉 За период: *{total_diff:.1f} кг* — отличный результат!")
        elif total_diff > 0:
            lines.append(f"\n📈 За период: *+{total_diff:.1f} кг*")
        else:
            lines.append("\n➡️ За период: вес стабилен")

    if target_w:
        current = history[-1]["weight"]
        diff_to_goal = current - target_w
        if diff_to_goal > 0:
            lines.append(f"🎯 До цели ({target_w} кг): осталось *{diff_to_goal:.1f} кг*")
        else:
            lines.append(f"🏆 Цель {target_w} кг — *достигнута!*")

    await update.message.reply_text("\n".join(lines), parse_mode="Markdown")


async def target_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not context.args:
        target = db.get_weight_goal(user_id)
        if target:
            latest = db.get_latest_weight(user_id)
            msg = f"🎯 *Целевой вес:* {target['target_weight']} кг\n"
            if latest:
                diff = latest["weight"] - target["target_weight"]
                if diff > 0:
                    msg += f"📍 Текущий вес: {latest['weight']} кг — осталось *{diff:.1f} кг*"
                else:
                    msg += f"🏆 Текущий вес: {latest['weight']} кг — цель достигнута!"
            msg += f"\n\nИзменить: `/target 70`"
            await update.message.reply_text(msg, parse_mode="Markdown")
        else:
            await update.message.reply_text(
                "🎯 Целевой вес не установлен.\n\n"
                "Установи так: `/target 75`",
                parse_mode="Markdown"
            )
        return

    try:
        target_w = float(context.args[0].replace(",", "."))
        db.set_weight_goal(user_id, target_w)

        latest = db.get_latest_weight(user_id)
        response = f"✅ *Цель установлена:* {target_w} кг\n"
        if latest:
            diff = latest["weight"] - target_w
            if diff > 0:
                response += f"📍 Сейчас: {latest['weight']} кг — осталось *{diff:.1f} кг*\n"
                response += "💪 Ты на правильном пути, продолжай!"
            elif diff < 0:
                response += f"🏆 Сейчас: {latest['weight']} кг — ты уже ниже цели!"
            else:
                response += "🎯 Ты уже на целевом весе!"
        else:
            response += "⚖️ Записывай вес командой `/weight 80` — буду следить за прогрессом!"

        await update.message.reply_text(response, parse_mode="Markdown")

    except ValueError:
        await update.message.reply_text(
            "❌ Неверный формат. Используй: `/target 75`",
            parse_mode="Markdown"
        )


def _meal_keyboard(meal_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ Верно", callback_data=f"confirm_{meal_id}"),
            InlineKeyboardButton("✏️ Исправить", callback_data=f"edit_{meal_id}"),
            InlineKeyboardButton("🗑️ Удалить", callback_data=f"delete_{meal_id}"),
        ]
    ])


def _meal_summary(result: dict, total_cal: int, total_protein: int,
                  meals_count: int, goal: dict, profile: dict = None) -> str:
    count = meals_count
    cal = result['calories']

    # % от нормы — если есть профиль берём его норму, иначе стандарт 2000
    norm = profile['daily_calories'] if profile else 2000
    pct = round(cal / norm * 100)

    text = (
        f"🍽️ *{result['food_description']}*\n\n"
        f"🔥 *{cal} ккал* — ~{pct}% от дневной нормы\n"
        f"🥩 Белки: {result['protein']} г  "
        f"🧈 Жиры: {result['fat']} г  "
        f"🍞 Углеводы: {result['carbs']} г\n\n"
        f"💬 _{result.get('comment', '')}_\n\n"
        f"📊 За сегодня: *{total_cal} ккал* "
        f"({count} {'приём' if count == 1 else 'приёма' if count < 5 else 'приёмов'} пищи)"
    )

    if profile:
        low  = profile['target_cal_low']
        high = profile['target_cal_high']
        left = high - total_cal
        if left > 0:
            text += f"\n🎯 До ориентира: ещё ~*{left} ккал* (цель {low}–{high})"
        elif total_cal <= high + 200:
            text += f"\n✅ В рамках ориентира! ({low}–{high} ккал/день)"
        else:
            over = total_cal - high
            text += f"\n⚠️ Выше ориентира на ~*{over} ккал*"
    elif goal:
        cal_left = goal['calories'] - total_cal
        prot_left = goal['protein'] - total_protein
        if cal_left > 0:
            text += f"\n🎯 До цели: *{cal_left} ккал* и *{prot_left} г белка*"
        elif cal_left > -200:
            text += f"\n✅ Цель выполнена! ({total_cal}/{goal['calories']} ккал)"
        else:
            text += f"\n⚠️ Цель превышена на *{abs(cal_left)} ккал*"
    else:
        text += f"\n\n💡 Напиши что поел или отправь ещё фото"
    return text


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    msg = await update.message.reply_text("🔍 Анализирую фото...")

    try:
        photo = update.message.photo[-1]
        photo_file = await photo.get_file()
        buf = BytesIO()
        await photo_file.download_to_memory(buf)
        image_bytes = buf.getvalue()
        caption = update.message.caption.strip() if update.message.caption else None

        result = await asyncio.get_running_loop().run_in_executor(
            None, analyze_food_image, image_bytes, caption
        )

        if "error" in result:
            await msg.edit_text(f"❌ {result['error']}")
            return

        today = date.today().isoformat()
        now_time = datetime.now().strftime("%H:%M")
        meal_id = db.add_meal(
            user_id=user_id, day=today, time=now_time,
            food_description=result["food_description"],
            calories=result["calories"], protein=result["protein"],
            fat=result["fat"], carbs=result["carbs"],
        )

        meals = db.get_meals_for_day(user_id, today)
        total_cal = sum(m["calories"] for m in meals)
        total_protein = sum(m["protein"] for m in meals)
        goal = db.get_goal(user_id)
        profile = db.get_profile(user_id)

        await msg.edit_text(
            _meal_summary(result, total_cal, total_protein, len(meals), goal, profile),
            parse_mode="Markdown",
            reply_markup=_meal_keyboard(meal_id),
        )

    except json.JSONDecodeError:
        logger.error("Failed to parse Claude response as JSON")
        await msg.edit_text("😔 Не смог разобрать ответ. Попробуй ещё раз или сделай более чёткое фото.")
    except Exception as e:
        logger.error(f"Error processing photo: {e}")
        await msg.edit_text("😔 Произошла ошибка при анализе фото. Попробуй ещё раз!")


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    user_id = update.effective_user.id

    # ── Profile step: возраст / рост / вес ───────────────────────
    step = context.user_data.get("profile_step")

    if step == "age":
        try:
            age = int(text)
            if not (10 <= age <= 100):
                raise ValueError
            context.user_data["p_age"] = age
            context.user_data["profile_step"] = "height"
            await update.message.reply_text(
                "Твой рост?\n\nНапиши в сантиметрах, например: *178*",
                parse_mode="Markdown"
            )
        except ValueError:
            await update.message.reply_text("Напиши возраст числом, например: *28*", parse_mode="Markdown")
        return

    if step == "height":
        try:
            height = int(text)
            if not (100 <= height <= 250):
                raise ValueError
            context.user_data["p_height"] = height
            context.user_data["profile_step"] = "weight"
            await update.message.reply_text(
                "Твой текущий вес?\n\nНапиши в килограммах, например: *75*",
                parse_mode="Markdown"
            )
        except ValueError:
            await update.message.reply_text("Напиши рост числом в см, например: *178*", parse_mode="Markdown")
        return

    if step == "weight":
        try:
            weight = float(text.replace(",", "."))
            if not (30 <= weight <= 300):
                raise ValueError
            goal   = context.user_data.get("p_goal", "maintain")
            sex    = context.user_data.get("p_sex", "male")
            age    = context.user_data["p_age"]
            height = context.user_data["p_height"]

            daily, low, high = _calc_calories(sex, age, height, weight, goal)

            db.set_profile(user_id=user_id, goal=goal, sex=sex, age=age,
                           height=height, weight=weight,
                           daily_calories=daily, target_cal_low=low, target_cal_high=high)
            db.log_weight(user_id, weight)

            # Очищаем шаги
            for k in ("profile_step", "p_goal", "p_sex", "p_age", "p_height"):
                context.user_data.pop(k, None)

            goal_text = {
                "lose":     f"🎯 Для похудения: *{low}–{high} ккал/день*",
                "maintain": f"🎯 Для поддержания веса: *{low}–{high} ккал/день*",
                "gain":     f"🎯 Для набора массы: *{low}–{high} ккал/день*",
            }[goal]

            await update.message.reply_text(
                f"✅ *Всё готово!*\n\n"
                f"Твоя норма: *~{daily} ккал/день*\n"
                f"{goal_text}\n\n"
                f"Теперь после каждого приёма пищи буду показывать сколько осталось до ориентира 🎯",
                parse_mode="Markdown"
            )
        except ValueError:
            await update.message.reply_text("Напиши вес числом в кг, например: *75*", parse_mode="Markdown")
        return

    # ── Режим исправления — пользователь нажал "Исправить" ───────
    if "editing_meal_id" in context.user_data:
        meal_id = context.user_data.pop("editing_meal_id")
        msg = await update.message.reply_text(f"🔍 Пересчитываю «{text}»...")
        try:
            result = await asyncio.get_running_loop().run_in_executor(
                None, analyze_food_text, text
            )
            if "error" in result:
                await msg.edit_text(f"❌ {result['error']}")
                return

            db.update_meal_by_id(
                meal_id=meal_id, user_id=user_id,
                food_description=result["food_description"],
                calories=result["calories"], protein=result["protein"],
                fat=result["fat"], carbs=result["carbs"],
            )

            today = date.today().isoformat()
            meals = db.get_meals_for_day(user_id, today)
            total_cal = sum(m["calories"] for m in meals)
            total_protein = sum(m["protein"] for m in meals)
            goal = db.get_goal(user_id)
            profile = db.get_profile(user_id)

            await msg.edit_text(
                "✅ *Исправлено!*\n\n" + _meal_summary(result, total_cal, total_protein, len(meals), goal, profile),
                parse_mode="Markdown",
                reply_markup=_meal_keyboard(meal_id),
            )
        except Exception as e:
            logger.error(f"Error in editing flow: {e}")
            await msg.edit_text("😔 Не смог пересчитать. Попробуй описать подробнее!")
        return

    # Обычный режим — распознавание еды
    if len(text) < 3:
        await update.message.reply_text(
            "📸 Отправь фото еды или напиши что поел — я посчитаю калории!\n\n"
            "Например: *«тарелка борща и хлеб»* или *«2 яйца, кофе с молоком»*",
            parse_mode="Markdown"
        )
        return

    msg = await update.message.reply_text("🔍 Считаю калории...")

    try:
        result = await asyncio.get_running_loop().run_in_executor(
            None, analyze_food_text, text
        )

        if "error" in result:
            await msg.edit_text(f"❌ {result['error']}")
            return

        today = date.today().isoformat()
        now_time = datetime.now().strftime("%H:%M")
        meal_id = db.add_meal(
            user_id=user_id, day=today, time=now_time,
            food_description=result["food_description"],
            calories=result["calories"], protein=result["protein"],
            fat=result["fat"], carbs=result["carbs"],
        )

        meals = db.get_meals_for_day(user_id, today)
        total_cal = sum(m["calories"] for m in meals)
        total_protein = sum(m["protein"] for m in meals)
        goal = db.get_goal(user_id)
        profile = db.get_profile(user_id)

        await msg.edit_text(
            _meal_summary(result, total_cal, total_protein, len(meals), goal, profile),
            parse_mode="Markdown",
            reply_markup=_meal_keyboard(meal_id),
        )

    except json.JSONDecodeError:
        await msg.edit_text("😔 Не смог разобрать. Попробуй описать подробнее!")
    except Exception as e:
        logger.error(f"Error processing text: {e}")
        await msg.edit_text("😔 Произошла ошибка. Попробуй ещё раз!")


def _profile_prompt_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("👉 Да, давай", callback_data="profile_yes"),
        InlineKeyboardButton("Пропустить", callback_data="profile_skip"),
    ]])

def _goal_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("📉 Похудеть", callback_data="pg_lose"),
        InlineKeyboardButton("⚖️ Держать вес", callback_data="pg_maintain"),
        InlineKeyboardButton("📈 Набрать массу", callback_data="pg_gain"),
    ]])

def _sex_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("👨 Мужской", callback_data="ps_male"),
        InlineKeyboardButton("👩 Женский", callback_data="ps_female"),
    ]])


async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    # ── Meal actions ──────────────────────────────────────────────
    if data.startswith("confirm_"):
        await query.edit_message_reply_markup(reply_markup=None)
        # Показываем prompt профиля если профиля ещё нет и ещё не показывали
        profile = db.get_profile(user_id)
        if not profile and not context.user_data.get("profile_prompted"):
            context.user_data["profile_prompted"] = True
            await query.message.reply_text(
                "💡 *Хочешь точную норму калорий?*\n\n"
                "Отвечу на 4 вопроса — посчитаю лично для тебя.\n"
                "Займёт 30 секунд.",
                parse_mode="Markdown",
                reply_markup=_profile_prompt_keyboard(),
            )

    elif data.startswith("delete_"):
        meal_id = int(data.split("_")[1])
        db.delete_meal_by_id(meal_id, user_id)
        today = date.today().isoformat()
        meals = db.get_meals_for_day(user_id, today)
        total_cal = sum(m["calories"] for m in meals)
        await query.edit_message_text(
            f"🗑️ Запись удалена.\n\n📊 За сегодня осталось: *{total_cal} ккал* ({len(meals)} приёмов)",
            parse_mode="Markdown"
        )

    elif data.startswith("edit_"):
        meal_id = int(data.split("_")[1])
        context.user_data["editing_meal_id"] = meal_id
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text("✏️ Напиши как правильно — я пересчитаю:")

    # ── Profile flow ──────────────────────────────────────────────
    elif data == "profile_yes":
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            "Какая у тебя цель?",
            reply_markup=_goal_keyboard()
        )

    elif data == "profile_skip":
        await query.edit_message_reply_markup(reply_markup=None)

    elif data.startswith("pg_"):  # goal selected
        goal = data[3:]  # lose / maintain / gain
        context.user_data["p_goal"] = goal
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text("Твой пол?", reply_markup=_sex_keyboard())

    elif data.startswith("ps_"):  # sex selected
        sex = data[3:]  # male / female
        context.user_data["p_sex"] = sex
        context.user_data["profile_step"] = "age"
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            "Сколько тебе лет?\n\nНапиши число, например: *28*",
            parse_mode="Markdown"
        )


async def delete_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    today = date.today().isoformat()

    if not context.args:
        await update.message.reply_text(
            "❌ Укажи номер приёма пищи.\nПример: `/delete 2`\n\nСписок за сегодня: /today",
            parse_mode="Markdown"
        )
        return

    try:
        num = int(context.args[0])
    except ValueError:
        await update.message.reply_text("❌ Номер должен быть числом. Например: `/delete 2`", parse_mode="Markdown")
        return

    meals = db.get_meals_for_day_with_ids(user_id, today)

    if not meals:
        await update.message.reply_text("📭 Сегодня нет записей о еде.")
        return

    if num < 1 or num > len(meals):
        await update.message.reply_text(
            f"❌ Нет приёма #{num}. Сегодня записей: {len(meals)}.\n\nПосмотреть список: /today",
            parse_mode="Markdown"
        )
        return

    meal = meals[num - 1]
    db.delete_meal_by_id(meal["id"], user_id)

    remaining = db.get_meals_for_day_with_ids(user_id, today)
    total_cal = sum(m["calories"] for m in remaining)

    await update.message.reply_text(
        f"🗑️ Удалено: *{meal['food_description']}* ({meal['calories']} ккал)\n\n"
        f"📊 За сегодня осталось: *{total_cal} ккал* ({len(remaining)} приёмов)",
        parse_mode="Markdown"
    )


async def edit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    today = date.today().isoformat()

    if not context.args or len(context.args) < 2:
        await update.message.reply_text(
            "✏️ Формат: `/edit номер новое описание`\n"
            "Пример: `/edit 2 борщ с говядиной 400г`\n\n"
            "Список за сегодня: /today",
            parse_mode="Markdown"
        )
        return

    try:
        num = int(context.args[0])
    except ValueError:
        await update.message.reply_text("❌ Первым укажи номер. Например: `/edit 2 борщ 400г`", parse_mode="Markdown")
        return

    new_description = " ".join(context.args[1:])
    meals = db.get_meals_for_day_with_ids(user_id, today)

    if not meals:
        await update.message.reply_text("📭 Сегодня нет записей о еде.")
        return

    if num < 1 or num > len(meals):
        await update.message.reply_text(
            f"❌ Нет приёма #{num}. Сегодня записей: {len(meals)}.",
            parse_mode="Markdown"
        )
        return

    meal = meals[num - 1]
    msg = await update.message.reply_text(f"🔍 Пересчитываю «{new_description}»...")

    try:
        result = await asyncio.get_running_loop().run_in_executor(
            None, analyze_food_text, new_description
        )

        if "error" in result:
            await msg.edit_text(f"❌ {result['error']}")
            return

        db.update_meal_by_id(
            meal_id=meal["id"],
            user_id=user_id,
            food_description=result["food_description"],
            calories=result["calories"],
            protein=result["protein"],
            fat=result["fat"],
            carbs=result["carbs"],
        )

        updated = db.get_meals_for_day_with_ids(user_id, today)
        total_cal = sum(m["calories"] for m in updated)
        total_protein = sum(m["protein"] for m in updated)

        await msg.edit_text(
            f"✅ *Приём #{num} обновлён*\n\n"
            f"🍽️ {result['food_description']}\n"
            f"🔥 {result['calories']} ккал | 🥩 {result['protein']} г | "
            f"🧈 {result['fat']} г | 🍞 {result['carbs']} г\n\n"
            f"📊 За сегодня: *{total_cal} ккал* / 🥩 *{total_protein} г белка*",
            parse_mode="Markdown"
        )

    except Exception as e:
        logger.error(f"Error in edit_command: {e}")
        await msg.edit_text("😔 Не смог пересчитать. Попробуй описать подробнее!")


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    with sqlite3.connect(DB_PATH) as conn:
        users = conn.execute("SELECT COUNT(DISTINCT user_id) FROM meals").fetchone()[0]
        active_7d = conn.execute(
            "SELECT COUNT(DISTINCT user_id) FROM meals WHERE day >= date('now', '-7 days')"
        ).fetchone()[0]
        total_meals = conn.execute("SELECT COUNT(*) FROM meals").fetchone()[0]

    await update.message.reply_text(
        f"📊 *Статистика Nutrio*\n\n"
        f"👥 Всего пользователей: *{users}*\n"
        f"🔥 Активных за 7 дней: *{active_7d}*\n"
        f"🍽️ Всего записей о еде: *{total_meals}*",
        parse_mode="Markdown"
    )


def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("today", today_command))
    app.add_handler(CommandHandler("history", history_command))
    app.add_handler(CommandHandler("reset", reset_command))
    app.add_handler(CommandHandler("goal", goal_command))
    app.add_handler(CommandHandler("weight", weight_command))
    app.add_handler(CommandHandler("target", target_command))
    app.add_handler(CommandHandler("progress", progress_command))
    app.add_handler(CommandHandler("delete", delete_command))
    app.add_handler(CommandHandler("edit", edit_command))
    app.add_handler(CommandHandler("stats", stats_command))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(CallbackQueryHandler(callback_handler))

    logger.info("Bot started!")
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == "__main__":
    main()
