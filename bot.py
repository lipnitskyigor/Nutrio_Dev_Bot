import os
import json
import base64
import logging
import asyncio
import sqlite3
from datetime import datetime, date
from io import BytesIO

import anthropic
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, LabeledPrice
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    PreCheckoutQueryHandler,
    filters,
    ContextTypes,
)

from database import Database, FREE_ANALYSES_LIMIT

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
ADMIN_ID = 148160233

PRICE_1M = 99    # Telegram Stars
PRICE_3M = 249   # Telegram Stars

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


def analyze_food_correction(original_description: str, correction: str) -> dict:
    """Re-analyze a meal with user's correction applied, keeping unchanged items intact."""
    response = claude.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""Ты эксперт по питанию. Пользователь ранее записал блюдо:
"{original_description}"

Теперь он хочет уточнить: "{correction}"

Примени уточнение к блюду (измени только то, что пользователь упомянул, остальное оставь как есть) и пересчитай калорийность и КБЖУ для всего блюда целиком.

Ответь СТРОГО в формате JSON (без markdown, без ```json, только чистый JSON):
{{
  "food_description": "полное описание блюда с учётом уточнения (на русском)",
  "calories": число (ккал для всего блюда),
  "protein": число (белки в граммах),
  "fat": число (жиры в граммах),
  "carbs": число (углеводы в граммах),
  "comment": "короткий комментарий (на русском, 1-2 предложения)"
}}

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


def _calc_calories(sex: str, age: int, height: int, weight: float, goal: str, activity: str = "moderate"):
    """Mifflin-St Jeor + activity factor. Returns (tdee, low, high)."""
    activity_factors = {
        "sedentary": 1.2,
        "light":     1.375,
        "moderate":  1.55,
        "active":    1.725,
    }
    factor = activity_factors.get(activity, 1.55)
    if sex == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    tdee = bmr * factor
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


def _calc_bmi(weight: float, height: int) -> float:
    return round(weight / (height / 100) ** 2, 1)


def _calc_min_weight(height: int) -> float:
    return round(18.5 * (height / 100) ** 2, 1)


def _calc_weeks_to_goal(current: float, target: float, daily_deficit: int = 500) -> int:
    diff = current - target
    if diff <= 0:
        return 0
    return round(diff * 7700 / (daily_deficit * 7))


# ── Notifications helpers ──────────────────────────────────────────

sent_reminders: set = set()


def _tz_str(offset: int) -> str:
    return f"UTC+{offset}" if offset >= 0 else f"UTC{offset}"


def _local_time(offset: int) -> str:
    from datetime import timezone, timedelta
    tz = timezone(timedelta(hours=offset))
    return datetime.now(tz).strftime("%H:%M")


def _notify_text(notif: dict) -> str:
    tz = notif["timezone_offset"]
    b = "✅" if notif["breakfast_enabled"] else "❌"
    l = "✅" if notif["lunch_enabled"] else "❌"
    d = "✅" if notif["dinner_enabled"] else "❌"
    return (
        f"⏰ *Настройка напоминаний*\n\n"
        f"🌍 Часовой пояс: {_tz_str(tz)} (сейчас {_local_time(tz)})\n\n"
        f"☕ Завтрак — {notif['breakfast_time']} ({b})\n"
        f"🍲 Обед — {notif['lunch_time']} ({l})\n"
        f"🍽️ Ужин — {notif['dinner_time']} ({d})\n\n"
        f"⚠️ Рекомендуем держать минимум 1 напоминание включённым"
    )


def _notify_keyboard(notif: dict) -> InlineKeyboardMarkup:
    b = f"☕ Завтрак {'✅' if notif['breakfast_enabled'] else '❌'}"
    l = f"🍲 Обед {'✅' if notif['lunch_enabled'] else '❌'}"
    d = f"🍽️ Ужин {'✅' if notif['dinner_enabled'] else '❌'}"
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ Включить все", callback_data="notif_all_on"),
            InlineKeyboardButton("❌ Отключить все", callback_data="notif_all_off"),
        ],
        [
            InlineKeyboardButton(b, callback_data="notif_toggle_breakfast"),
            InlineKeyboardButton(f"🕐 {notif['breakfast_time']}", callback_data="notif_time_breakfast"),
        ],
        [
            InlineKeyboardButton(l, callback_data="notif_toggle_lunch"),
            InlineKeyboardButton(f"🕐 {notif['lunch_time']}", callback_data="notif_time_lunch"),
        ],
        [
            InlineKeyboardButton(d, callback_data="notif_toggle_dinner"),
            InlineKeyboardButton(f"🕐 {notif['dinner_time']}", callback_data="notif_time_dinner"),
        ],
        [InlineKeyboardButton("🌍 Изменить часовой пояс", callback_data="notif_timezone")],
    ])


def _onboarding_timezone_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🇺🇦 Киев",    callback_data="onb_tz_2"),
            InlineKeyboardButton("🇷🇺 Москва",  callback_data="onb_tz_3"),
        ],
        [
            InlineKeyboardButton("🇦🇿 Баку",    callback_data="onb_tz_4"),
            InlineKeyboardButton("🇰🇿 Алматы",  callback_data="onb_tz_5"),
        ],
        [
            InlineKeyboardButton("🇺🇿 Ташкент", callback_data="onb_tz_5"),
            InlineKeyboardButton("Новосибирск", callback_data="onb_tz_7"),
        ],
        [
            InlineKeyboardButton("Иркутск",     callback_data="onb_tz_8"),
            InlineKeyboardButton("Владивосток", callback_data="onb_tz_10"),
        ],
        [InlineKeyboardButton("❌ Пропустить",  callback_data="onb_tz_skip")],
    ])


def _timezone_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🇺🇦 Киев",    callback_data="tz_2"),
            InlineKeyboardButton("🇷🇺 Москва",  callback_data="tz_3"),
        ],
        [
            InlineKeyboardButton("🇦🇿 Баку",    callback_data="tz_4"),
            InlineKeyboardButton("🇰🇿 Алматы",  callback_data="tz_5"),
        ],
        [
            InlineKeyboardButton("🇺🇿 Ташкент", callback_data="tz_5"),
            InlineKeyboardButton("Новосибирск", callback_data="tz_7"),
        ],
        [
            InlineKeyboardButton("Иркутск",     callback_data="tz_8"),
            InlineKeyboardButton("Владивосток", callback_data="tz_10"),
        ],
    ])


MENU_ADD    = "🍽️ Добавить еду"
MENU_DIARY  = "📔 Дневник"
MENU_PROFILE = "👤 Профиль"
MENU_HELP   = "❓ Помощь"


def _main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(MENU_DIARY)],
            [KeyboardButton(MENU_PROFILE), KeyboardButton(MENU_HELP)],
        ],
        resize_keyboard=True,
        input_field_placeholder="Отправь фото или напиши что поел...",
    )


def _terms_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("✅ Принимаю условия", callback_data="accept_terms"),
    ]])


def _subscribe_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(f"1 месяц — {PRICE_1M} ⭐", callback_data="sub_1m"),
        InlineKeyboardButton(f"3 месяца — {PRICE_3M} ⭐", callback_data="sub_3m"),
    ]])


def _paywall_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("💳 Оформить подписку", callback_data="show_subscribe"),
    ]])


def _trial_notice(left: int) -> str:
    if left == 0:
        return (
            "❌ *Бесплатные анализы закончились* (15 из 15)\n\n"
            "Оформи подписку, чтобы продолжить считать калории 👇"
        )
    elif left == 1:
        return f"⚠️ Остался *1 бесплатный анализ* из {FREE_ANALYSES_LIMIT} → /subscribe"
    elif left <= 3:
        return f"⚠️ Осталось *{left} бесплатных анализа* из {FREE_ANALYSES_LIMIT} → /subscribe"
    elif left <= 5:
        return f"🎁 Осталось {left} бесплатных анализов из {FREE_ANALYSES_LIMIT} → /subscribe"
    else:
        return f"🎁 Бесплатных анализов: {left} из {FREE_ANALYSES_LIMIT}"


async def _send_terms(message, name: str):
    await message.reply_text(
        f"👋 Привет, {name}!\n\n"
        "Прежде чем начать, прочитай важное:\n\n"
        "⚠️ MealScan — помощник для подсчёта калорий и КБЖУ.\n"
        "Это не медицинское приложение. Бот не заменяет врача,\n"
        "диетолога или нутрициолога.\n\n"
        "📄 Условия использования: mealscan.org/terms.html\n\n"
        "Нажимая кнопку ниже, ты соглашаешься с условиями использования.",
        reply_markup=_terms_keyboard(),
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or "друг"
    user_id = user.id

    if not db.get_terms_accepted(user_id):
        await _send_terms(update.message, name)
        return

    profile = db.get_profile(user_id)
    meals = db.get_meals_for_day(user_id, date.today().isoformat())

    if profile or meals:
        # Returning user
        await update.message.reply_text(
            f"С возвращением, {name}! 👋\n\n"
            "📸 Отправь фото еды или напиши что поел — посчитаю.",
            parse_mode="Markdown",
            reply_markup=_main_keyboard(),
        )
    else:
        # New user — onboarding
        await update.message.reply_text(
            f"Привет, {name}! 👋\n"
            "Я помогаю следить за питанием — считаю калории и КБЖУ по фото или тексту.\n\n"
            "📸 *Отправь фото любого блюда*\n"
            "✏️ Или напиши что поел\n\n"
            "Попробуй прямо сейчас ↓\n\n"
            "———\n"
            "ℹ️ Nutrio — помощник для контроля питания, не медицинское приложение. При наличии заболеваний или перед сменой рациона проконсультируйтесь с врачом или диетологом.",
            parse_mode="Markdown",
            reply_markup=_main_keyboard(),
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
        "💡 Совет: чем чётче видна еда на фото, тем точнее результат!\n\n"
        "🔔 *Напоминания:*\n"
        "/notify — настроить напоминания о приёмах пищи",
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

    goal = db.get_goal(user_id)
    profile = db.get_profile(user_id)

    if goal:
        goal_cal = goal["calories"]
        goal_protein = goal["protein"]
    elif profile:
        goal_cal = (profile["target_cal_low"] + profile["target_cal_high"]) // 2
        goal_protein = round(profile["daily_calories"] * 0.25 / 4)
    else:
        goal_cal = 2000
        goal_protein = 100

    cal_left = goal_cal - total_cal
    prot_left = max(0, goal_protein - total_protein)

    lines = [f"📊 *Итог за сегодня — {user_name}*\n"]
    for i, meal in enumerate(meals, 1):
        t = meal["time"]
        lines.append(f"{i}. {meal['food_description']} — {meal['calories']} ккал ({t})")

    lines.append(f"\n🔥 *Итого: {total_cal} ккал*")
    lines.append(f"🥩 Белки: {total_protein} г  🧈 Жиры: {total_fat} г  🍞 Углеводы: {total_carbs} г")

    if cal_left > 0:
        lines.append(f"\n🎯 Осталось до цели: *{cal_left} ккал* и *{prot_left} г белка*")
    elif cal_left > -200:
        lines.append(f"\n✅ *Цель по калориям выполнена!*")
    else:
        lines.append(f"\n⚠️ Превышение цели на *{abs(cal_left)} ккал*")

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
        if not (30 <= target_w <= 300):
            raise ValueError
    except ValueError:
        await update.message.reply_text(
            "❌ Неверный формат. Используй: `/target 75`",
            parse_mode="Markdown"
        )
        return

    profile = db.get_profile(user_id)
    if not profile or not all([profile.get('height'), profile.get('age'), profile.get('sex'), profile.get('activity')]):
        await update.message.reply_text(
            "📋 Для проверки безопасности цели нужен профиль (рост, возраст, пол, активность).\n\n"
            "Настрой профиль — и я проверю, насколько цель безопасна.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("👉 Настроить профиль", callback_data="profile_yes")
            ]])
        )
        return

    height = profile['height']
    bmi = _calc_bmi(target_w, height)
    min_weight = _calc_min_weight(height)
    latest = db.get_latest_weight(user_id)
    current_weight = latest['weight'] if latest else profile['weight']
    tdee, _, _ = _calc_calories(profile['sex'], profile['age'], height, current_weight,
                                profile.get('goal', 'maintain'), profile.get('activity', 'moderate'))
    min_cal = 1200 if profile['sex'] == 'female' else 1500
    recommended_cal = max(tdee - 500, min_cal)
    weeks = _calc_weeks_to_goal(current_weight, target_w)

    if bmi >= 18.5:
        db.set_weight_goal(user_id, target_w)
        db.set_target_confirmation(user_id, 'safe')
        text = f"✅ *Цель установлена: {target_w} кг*\n\n"
        text += f"📊 Рекомендуемый калораж: *{recommended_cal} ккал/день*\n"
        if tdee - 500 < min_cal:
            text += f"⚠️ _Минимально безопасный калораж: {min_cal} ккал/день_\n"
        if weeks > 0:
            text += f"⏱ Примерный срок: *{weeks} недель*"
        await update.message.reply_text(text, parse_mode="Markdown")

    elif bmi >= 17:
        await update.message.reply_text(
            f"⚠️ Целевой вес *{target_w} кг* даёт ИМТ *{bmi}* — ниже нормы.\n"
            f"Минимально рекомендуемый вес для твоего роста: *{min_weight} кг*.\n\n"
            f"Проконсультируйся со специалистом перед началом.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✅ Всё равно установить", callback_data=f"target_confirm_{target_w}"),
                InlineKeyboardButton("✏️ Изменить цель", callback_data="target_change"),
            ]])
        )

    elif bmi >= 16:
        await update.message.reply_text(
            f"🚨 Целевой вес *{target_w} кг* — это ИМТ *{bmi}*, опасно низкий показатель.\n"
            f"Рекомендуемый минимум для роста {height} см: *{min_weight} кг*.\n\n"
            f"Настоятельно рекомендуем проконсультироваться с врачом.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("⚠️ Установить (не рекомендуется)", callback_data=f"target_confirm_{target_w}"),
                InlineKeyboardButton("✏️ Изменить цель", callback_data="target_change"),
            ]])
        )

    else:
        await update.message.reply_text(
            f"❌ Установить цель *{target_w} кг* невозможно.\n"
            f"Это ИМТ *{bmi}* — критически низкий показатель, опасный для жизни.\n\n"
            f"Минимально допустимый вес для твоего роста: *{min_weight} кг*.\n"
            f"Пожалуйста, обратись к врачу или диетологу.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✏️ Изменить цель", callback_data="target_change"),
            ]])
        )


def _meal_keyboard(meal_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ Верно", callback_data=f"confirm_{meal_id}"),
            InlineKeyboardButton("✏️ Исправить", callback_data=f"edit_{meal_id}"),
            InlineKeyboardButton("🗑️ Удалить", callback_data=f"delete_{meal_id}"),
        ]
    ])


DEFAULT_CAL  = 2000   # средняя норма без профиля
DEFAULT_PROT = 100    # средний белок без профиля


def _meal_summary(result: dict, total_cal: int, total_protein: int,
                  meals_count: int, goal: dict, profile: dict = None) -> str:
    count = meals_count
    cal   = result['calories']
    prot  = result['protein']

    # Норма и целевой диапазон
    if profile:
        norm     = profile['daily_calories']
        cal_low  = profile['target_cal_low']
        cal_high = profile['target_cal_high']
        prot_target = round(norm * 0.25 / 4)   # ~25% калорий из белка → граммы
    else:
        norm = cal_low = cal_high = DEFAULT_CAL
        prot_target = DEFAULT_PROT

    pct = round(cal / norm * 100)

    text = (
        f"🍽️ *{result['food_description']}*\n\n"
        f"🔥 *{cal} ккал* — ~{pct}% от нормы\n"
        f"🥩 Белки: *{prot} г*\n"
        f"🧈 Жиры: {result['fat']} г\n"
        f"🍞 Углеводы: {result['carbs']} г\n\n"
        f"💬 _{result.get('comment', '')}_\n\n"
        f"📊 *За сегодня:*\n"
        f"🔥 {total_cal} ккал  🥩 белок: *{total_protein} г*"
    )

    if profile:
        cal_left  = cal_high - total_cal
        prot_left = max(0, prot_target - total_protein)
        if cal_left > 0:
            text += (
                f"\n\n🎯 Осталось до ориентира: *~{cal_left} ккал*"
                f" и *~{prot_left} г белка*"
                f"\n_(ориентир: {cal_low}–{cal_high} ккал/день)_"
            )
        elif total_cal <= cal_high + 200:
            text += f"\n\n✅ В рамках ориентира! ({cal_low}–{cal_high} ккал/день)"
        else:
            over = total_cal - cal_high
            text += f"\n\n⚠️ Выше ориентира на ~*{over} ккал*"
    else:
        cal_left  = DEFAULT_CAL  - total_cal
        prot_left = max(0, DEFAULT_PROT - total_protein)
        if cal_left > 0:
            text += (
                f"\n\n🎯 Осталось до средней нормы: *~{cal_left} ккал*"
                f" и *~{prot_left} г белка*"
            )
        elif cal_left > -200:
            text += f"\n\n✅ Средняя норма выполнена!"
        else:
            text += f"\n\n⚠️ Выше средней нормы на *{abs(cal_left)} ккал*"

    return text


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not db.get_terms_accepted(user_id):
        await _send_terms(update.message, update.effective_user.first_name or "друг")
        return
    if not db.has_access(user_id):
        await update.message.reply_text(
            _trial_notice(0),
            parse_mode="Markdown",
            reply_markup=_paywall_keyboard(),
        )
        return
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
        if not db.is_paid_active(user_id):
            db.use_free_analysis(user_id)
            left = db.get_free_analyses_left(user_id)
            notice = _trial_notice(left)
            if notice:
                await update.message.reply_text(
                    notice,
                    parse_mode="Markdown",
                    reply_markup=_paywall_keyboard() if left == 0 else None,
                )
        await _maybe_send_profile_prompt(update.message, user_id, context)

    except json.JSONDecodeError:
        logger.error("Failed to parse Claude response as JSON")
        await msg.edit_text("😔 Не смог разобрать ответ. Попробуй ещё раз или сделай более чёткое фото.")
    except Exception as e:
        logger.error(f"Error processing photo: {e}")
        await msg.edit_text("😔 Произошла ошибка при анализе фото. Попробуй ещё раз!")


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    user_id = update.effective_user.id

    if not db.get_terms_accepted(user_id):
        await _send_terms(update.message, update.effective_user.first_name or "друг")
        return

    # ── Меню-кнопки ───────────────────────────────────────────────
    if text == MENU_ADD:
        await update.message.reply_text(
            "📸 Отправь фото еды или напиши что поел — посчитаю!"
        )
        return

    if text == MENU_DIARY:
        await today_command(update, context)
        return

    if text == MENU_PROFILE:
        profile = db.get_profile(user_id)
        if not profile:
            await update.message.reply_text(
                "📋 Профиль не настроен.\n\nОтправь любое фото еды — и я предложу его настроить!",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("👉 Настроить профиль", callback_data="profile_yes")
                ]])
            )
        else:
            goal_labels = {"lose": "Похудеть 🥦", "maintain": "Держать вес ⚖️", "gain": "Набрать массу 💪"}
            activity_labels = {"sedentary": "Сидячий 🪑", "light": "Лёгкая 🚶", "moderate": "Умеренная 🏃", "active": "Высокая 💪"}
            protein = round(profile['daily_calories'] * 0.25 / 4)
            await update.message.reply_text(
                f"👤 *Твой профиль*\n\n"
                f"🎯 Цель: {goal_labels.get(profile['goal'], profile['goal'])}\n"
                f"⚡ Активность: {activity_labels.get(profile['activity'], profile['activity'])}\n"
                f"📏 Рост: {profile['height']} см\n"
                f"⚖️ Вес: {profile['weight']} кг\n\n"
                f"🔥 Калории: *{profile['target_cal_low']}–{profile['target_cal_high']} ккал/день*\n"
                f"🥩 Белок: *{protein} г/день*",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("✏️ Изменить профиль", callback_data="profile_yes")
                ]])
            )
        return

    if text == MENU_HELP:
        await help_command(update, context)
        return

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
            context.user_data["p_weight"] = weight
            context.user_data["profile_step"] = "target_weight"
            await update.message.reply_text(
                "Есть целевой вес?",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("✏️ Да, укажу", callback_data="ptw_yes"),
                    InlineKeyboardButton("Пропустить", callback_data="ptw_skip"),
                ]])
            )
        except ValueError:
            await update.message.reply_text("Напиши вес числом в кг, например: *75*", parse_mode="Markdown")
        return

    if step == "target_weight":
        try:
            target_w = float(text.replace(",", "."))
            if not (30 <= target_w <= 300):
                raise ValueError

            height = context.user_data.get("p_height")
            if height:
                bmi = _calc_bmi(target_w, height)
                min_weight = _calc_min_weight(height)

                if bmi >= 18.5:
                    db.set_weight_goal(user_id, target_w)
                    db.set_target_confirmation(user_id, 'safe')
                    await _finish_profile(update.message, user_id, context)

                elif bmi >= 17:
                    context.user_data["pending_target_onb"] = target_w
                    context.user_data.pop("profile_step", None)
                    await update.message.reply_text(
                        f"⚠️ Целевой вес *{target_w} кг* даёт ИМТ *{bmi}* — ниже нормы.\n"
                        f"Минимально рекомендуемый вес для твоего роста: *{min_weight} кг*.\n\n"
                        f"Проконсультируйся со специалистом перед началом.",
                        parse_mode="Markdown",
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("✅ Всё равно установить", callback_data=f"target_confirm_onb_{target_w}"),
                            InlineKeyboardButton("✏️ Изменить цель", callback_data="target_change_onb"),
                        ]])
                    )

                elif bmi >= 16:
                    context.user_data["pending_target_onb"] = target_w
                    context.user_data.pop("profile_step", None)
                    await update.message.reply_text(
                        f"🚨 Целевой вес *{target_w} кг* — это ИМТ *{bmi}*, опасно низкий показатель.\n"
                        f"Рекомендуемый минимум для роста {height} см: *{min_weight} кг*.\n\n"
                        f"Настоятельно рекомендуем проконсультироваться с врачом.",
                        parse_mode="Markdown",
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("⚠️ Установить (не рекомендуется)", callback_data=f"target_confirm_onb_{target_w}"),
                            InlineKeyboardButton("✏️ Изменить цель", callback_data="target_change_onb"),
                        ]])
                    )

                else:
                    context.user_data["profile_step"] = "target_weight"
                    await update.message.reply_text(
                        f"❌ Целевой вес *{target_w} кг* — ИМТ *{bmi}*, критически опасный показатель.\n"
                        f"Минимально допустимый вес для роста {height} см: *{min_weight} кг*.\n\n"
                        f"Напиши другой целевой вес:",
                        parse_mode="Markdown"
                    )
            else:
                db.set_weight_goal(user_id, target_w)
                await _finish_profile(update.message, user_id, context)

        except ValueError:
            await update.message.reply_text("Напиши вес числом в кг, например: *70*", parse_mode="Markdown")
        return

    if step == "timezone":
        try:
            parts = text.strip().replace(".", ":").split(":")
            user_hour = int(parts[0])
            if not (0 <= user_hour <= 23):
                raise ValueError
            from datetime import timezone as tz_mod
            utc_hour = datetime.now(tz_mod.utc).hour
            offset = user_hour - utc_hour
            if offset > 12:
                offset -= 24
            elif offset < -12:
                offset += 24
            context.user_data.pop("profile_step", None)
            db.save_notifications(user_id, 1, 1, 1, offset)
            sign = "+" if offset >= 0 else ""
            await update.message.reply_text(
                f"🔔 *Напоминания включены!*\n\n"
                f"🕐 Часовой пояс определён: UTC{sign}{offset}\n"
                f"☕ Завтрак — 9:00\n"
                f"🍲 Обед — 13:00\n"
                f"🍽️ Ужин — 19:00\n\n"
                f"Настроить: /notify",
                parse_mode="Markdown"
            )
        except (ValueError, IndexError):
            await update.message.reply_text(
                "Не понял 🤔 Напиши время в формате *ЧЧ:ММ*, например: *23:15*",
                parse_mode="Markdown"
            )
        return

    # ── Режим исправления — пользователь нажал "Исправить" ───────
    if "editing_meal_id" in context.user_data:
        meal_id = context.user_data.pop("editing_meal_id")
        msg = await update.message.reply_text(f"🔍 Пересчитываю...")
        try:
            original_meal = db.get_meal_by_id(meal_id, user_id)
            if original_meal:
                result = await asyncio.get_running_loop().run_in_executor(
                    None, analyze_food_correction, original_meal["food_description"], text
                )
            else:
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

    # ── Обработка состояния изменения таймзоны через /notify ──────
    if context.user_data.get("setting_timezone"):
        try:
            parts = text.strip().replace(".", ":").split(":")
            user_hour = int(parts[0])
            if not (0 <= user_hour <= 23):
                raise ValueError
            from datetime import timezone as tz_mod
            utc_hour = datetime.now(tz_mod.utc).hour
            offset = user_hour - utc_hour
            if offset > 12:
                offset -= 24
            elif offset < -12:
                offset += 24
            context.user_data.pop("setting_timezone", None)
            notif = db.get_or_create_notifications(user_id)
            db.save_notifications(user_id, notif["breakfast_enabled"],
                                  notif["lunch_enabled"], notif["dinner_enabled"], offset)
            sign = "+" if offset >= 0 else ""
            notif = db.get_notifications(user_id)
            await update.message.reply_text(
                f"✅ Часовой пояс обновлён: UTC{sign}{offset}\n\n" + _notify_text(notif),
                parse_mode="Markdown",
                reply_markup=_notify_keyboard(notif)
            )
        except (ValueError, IndexError):
            await update.message.reply_text(
                "Не понял 🤔 Напиши время в формате *ЧЧ:ММ*, например: *23:15*",
                parse_mode="Markdown"
            )
        return

    # ── Режим изменения времени напоминания ──────────────────────
    if context.user_data.get("setting_notification_time"):
        meal_type = context.user_data.get("setting_notification_time")
        import re
        stripped = text.strip().replace(".", ":").replace("-", ":")
        m = re.match(r'^(\d{1,2}):(\d{2})$', stripped)
        if m:
            h, mn = int(m.group(1)), int(m.group(2))
            if 0 <= h <= 23 and 0 <= mn <= 59:
                time_str = f"{h:02d}:{mn:02d}"
                context.user_data.pop("setting_notification_time", None)
                db.get_or_create_notifications(user_id)
                db.save_notification_time(user_id, meal_type, time_str)
                notif = db.get_notifications(user_id)
                meal_names = {"breakfast": "завтрак", "lunch": "обед", "dinner": "ужин"}
                await update.message.reply_text(
                    f"✅ Время напоминания ({meal_names.get(meal_type, meal_type)}) обновлено: *{time_str}*\n\n"
                    + _notify_text(notif),
                    parse_mode="Markdown",
                    reply_markup=_notify_keyboard(notif),
                )
                return
        await update.message.reply_text(
            "❌ Не понял время. Напиши в формате *ЧЧ:ММ*, например: *08:30*",
            parse_mode="Markdown",
        )
        return

    # Обычный режим — распознавание еды
    if len(text) < 3:
        await update.message.reply_text(
            "📸 Отправь фото еды или напиши что поел — я посчитаю калории!\n\n"
            "Например: *«тарелка борща и хлеб»* или *«2 яйца, кофе с молоком»*",
            parse_mode="Markdown"
        )
        return

    if not db.has_access(user_id):
        await update.message.reply_text(
            _trial_notice(0),
            parse_mode="Markdown",
            reply_markup=_paywall_keyboard(),
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
        if not db.is_paid_active(user_id):
            db.use_free_analysis(user_id)
            left = db.get_free_analyses_left(user_id)
            notice = _trial_notice(left)
            if notice:
                await update.message.reply_text(
                    notice,
                    parse_mode="Markdown",
                    reply_markup=_paywall_keyboard() if left == 0 else None,
                )
        await _maybe_send_profile_prompt(update.message, user_id, context)

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


async def _finish_profile(message, user_id: int, context) -> None:
    """Сохраняет профиль и отправляет финальный результат."""
    goal     = context.user_data.get("p_goal", "maintain")
    sex      = context.user_data.get("p_sex", "male")
    activity = context.user_data.get("p_activity", "moderate")
    age      = context.user_data["p_age"]
    height   = context.user_data["p_height"]
    weight   = context.user_data["p_weight"]

    daily, low, high = _calc_calories(sex, age, height, weight, goal, activity)

    db.set_profile(user_id=user_id, goal=goal, sex=sex, age=age,
                   height=height, weight=weight,
                   daily_calories=daily, target_cal_low=low, target_cal_high=high,
                   activity=activity)
    db.log_weight(user_id, weight)
    # Синхронизируем goals таблицу — используем середину целевого диапазона
    protein = round(daily * 0.25 / 4)  # ~25% калорий из белка
    target_cal = (low + high) // 2
    db.set_goal(user_id, target_cal, protein)

    for k in ("profile_step", "p_goal", "p_sex", "p_activity", "p_age", "p_height", "p_weight"):
        context.user_data.pop(k, None)

    target = db.get_weight_goal(user_id)
    target_line = ""
    if target:
        diff = weight - target["target_weight"]
        if diff > 0:
            target_line = f"\n⚖️ Целевой вес: *{target['target_weight']} кг* (осталось ~{diff:.1f} кг)"
        else:
            target_line = f"\n⚖️ Целевой вес: *{target['target_weight']} кг* — уже достигнут! 🏆"

    goal_label = {
        "lose":     "Похудеть",
        "maintain": "Держать вес",
        "gain":     "Набрать массу",
    }[goal]

    await message.reply_text(
        f"✅ *Всё готово!*\n\n"
        f"🎯 Цель: *{goal_label}*\n"
        f"🔥 Калории: *{low}–{high} ккал/день*\n"
        f"🥩 Белок: *~{protein} г/день*"
        f"{target_line}\n\n"
        f"После каждого приёма пищи буду показывать сколько ккал осталось до цели 🎯",
        parse_mode="Markdown"
    )

    context.user_data["profile_step"] = "timezone"
    await message.reply_text(
        "🔔 *Настроим напоминания для трекинга питания!*\n\n"
        "Я буду напоминать тебе записывать еду — просто скинь фото или напиши, что поел.\n\n"
        "Напиши, сколько сейчас у тебя времени, например: *23:15*",
        parse_mode="Markdown"
    )


async def _maybe_send_profile_prompt(message, user_id: int, context) -> None:
    """Отправляет приглашение настроить профиль — один раз, сразу после первого результата."""
    profile = db.get_profile(user_id)
    if not profile and not context.user_data.get("profile_prompted"):
        context.user_data["profile_prompted"] = True
        await message.reply_text(
            "📊 *Давай настроим калории под тебя и твою цель*\n\n"
            "Ответь на 4 вопроса — и расчёт станет точнее\n"
            "Займёт меньше 30 секунд",
            parse_mode="Markdown",
            reply_markup=_profile_prompt_keyboard(),
        )

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

def _activity_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🪑 Сидячий (офис, без спорта)", callback_data="pa_sedentary")],
        [InlineKeyboardButton("🚶 Лёгкая активность (1–2 раза в неделю)", callback_data="pa_light")],
        [InlineKeyboardButton("🏃 Умеренная (3–5 раз в неделю)", callback_data="pa_moderate")],
        [InlineKeyboardButton("💪 Высокая (каждый день)", callback_data="pa_active")],
    ])


async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    # ── Terms acceptance ──────────────────────────────────────────
    if data == "accept_terms":
        db.set_terms_accepted(user_id)
        db.init_subscription(user_id)
        await query.edit_message_reply_markup(reply_markup=None)
        name = query.from_user.first_name or "друг"
        profile = db.get_profile(user_id)
        meals = db.get_meals_for_day(user_id, date.today().isoformat())
        if profile or meals:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text=(
                    f"С возвращением, {name}! 👋\n\n"
                    "📸 Отправь фото еды или напиши что поел — посчитаю."
                ),
                parse_mode="Markdown",
                reply_markup=_main_keyboard(),
            )
        else:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text=(
                    f"Привет, {name}! 👋\n"
                    "Я помогаю следить за питанием — считаю калории и КБЖУ по фото или тексту.\n\n"
                    "📸 *Отправь фото любого блюда*\n"
                    "✏️ Или напиши что поел\n\n"
                    "Попробуй прямо сейчас ↓\n\n"
                    "———\n"
                    "ℹ️ Nutrio — помощник для контроля питания, не медицинское приложение. "
                    "При наличии заболеваний или перед сменой рациона проконсультируйтесь с врачом или диетологом."
                ),
                parse_mode="Markdown",
                reply_markup=_main_keyboard(),
            )
        return

    # ── Meal actions ──────────────────────────────────────────────
    if data.startswith("confirm_"):
        await query.edit_message_reply_markup(reply_markup=None)

    elif data.startswith("delete_"):
        meal_id = int(data.split("_")[1])
        db.delete_meal_by_id(meal_id, user_id)
        today = date.today().isoformat()
        meals = db.get_meals_for_day(user_id, today)
        total_cal = sum(m["calories"] for m in meals)
        total_protein = sum(m["protein"] for m in meals)
        goal = db.get_goal(user_id)
        profile = db.get_profile(user_id)
        if goal:
            goal_cal = goal["calories"]
            goal_protein = goal["protein"]
        elif profile:
            goal_cal = (profile["target_cal_low"] + profile["target_cal_high"]) // 2
            goal_protein = round(profile["daily_calories"] * 0.25 / 4)
        else:
            goal_cal = 2000
            goal_protein = 100
        cal_left = goal_cal - total_cal
        prot_left = max(0, goal_protein - total_protein)
        if cal_left > 0:
            remaining_line = f"🎯 Осталось до цели: *{cal_left} ккал* и *{prot_left} г белка*"
        elif cal_left > -200:
            remaining_line = "✅ Цель по калориям выполнена!"
        else:
            remaining_line = f"⚠️ Превышение цели на *{abs(cal_left)} ккал*"
        await query.edit_message_text(
            f"🗑️ Запись удалена.\n\n"
            f"📊 Съедено за сегодня: *{total_cal} ккал* / 🥩 *{total_protein} г белка* ({len(meals)} приёмов)\n"
            f"{remaining_line}",
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
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            "Твой образ жизни?",
            reply_markup=_activity_keyboard()
        )

    elif data.startswith("pa_"):  # activity selected
        activity = data[3:]  # sedentary / light / moderate / active
        context.user_data["p_activity"] = activity
        context.user_data["profile_step"] = "age"
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            "Сколько тебе лет?\n\nНапиши число, например: *28*",
            parse_mode="Markdown"
        )

    elif data == "ptw_yes":
        context.user_data["profile_step"] = "target_weight"
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            "Напиши целевой вес в кг, например: *70*",
            parse_mode="Markdown"
        )

    elif data == "ptw_skip":
        await query.edit_message_reply_markup(reply_markup=None)
        await _finish_profile(query.message, user_id, context)

    # ── Notifications ─────────────────────────────────────────────
    elif data in ("notif_all_on", "notif_all_off"):
        notif = db.get_or_create_notifications(user_id)
        val = 1 if data == "notif_all_on" else 0
        db.save_notifications(user_id, val, val, val, notif["timezone_offset"])
        notif = db.get_notifications(user_id)
        await query.edit_message_text(
            _notify_text(notif), parse_mode="Markdown",
            reply_markup=_notify_keyboard(notif)
        )

    elif data.startswith("notif_toggle_"):
        meal = data[len("notif_toggle_"):]   # breakfast / lunch / dinner
        notif = db.get_or_create_notifications(user_id)
        new_val = 0 if notif[f"{meal}_enabled"] else 1
        db.save_notifications(
            user_id,
            new_val if meal == "breakfast" else notif["breakfast_enabled"],
            new_val if meal == "lunch"     else notif["lunch_enabled"],
            new_val if meal == "dinner"    else notif["dinner_enabled"],
            notif["timezone_offset"],
        )
        notif = db.get_notifications(user_id)
        await query.edit_message_text(
            _notify_text(notif), parse_mode="Markdown",
            reply_markup=_notify_keyboard(notif)
        )

    elif data.startswith("notif_time_"):
        meal_type = data[len("notif_time_"):]  # breakfast / lunch / dinner
        context.user_data["setting_notification_time"] = meal_type
        meal_names = {"breakfast": "завтрак", "lunch": "обед", "dinner": "ужин"}
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            f"⏰ Напиши новое время для напоминания про *{meal_names.get(meal_type, meal_type)}*\n\n"
            f"Формат: *ЧЧ:ММ*, например: *08:30*",
            parse_mode="Markdown",
        )

    elif data == "notif_timezone":
        context.user_data["setting_timezone"] = True
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            "🕐 Напиши сколько сейчас у тебя времени, например: *23:15*\n\n"
            "Определю часовой пояс автоматически.",
            parse_mode="Markdown"
        )

    elif data.startswith("tz_"):
        offset = int(data[3:])
        notif = db.get_or_create_notifications(user_id)
        db.save_notifications(
            user_id,
            notif["breakfast_enabled"],
            notif["lunch_enabled"],
            notif["dinner_enabled"],
            offset,
        )
        notif = db.get_notifications(user_id)
        await query.edit_message_text(
            _notify_text(notif), parse_mode="Markdown",
            reply_markup=_notify_keyboard(notif)
        )

    elif data.startswith("onb_tz_"):
        val = data[len("onb_tz_"):]
        if val == "skip":
            await query.edit_message_reply_markup(reply_markup=None)
            await query.message.reply_text(
                "Окей, без напоминаний 👌\n"
                "Включить в любой момент: /notify"
            )
        else:
            offset = int(val)
            db.save_notifications(user_id, 1, 1, 1, offset)
            tz_label = _tz_str(offset)
            await query.edit_message_reply_markup(reply_markup=None)
            await query.message.reply_text(
                f"🔔 *Напоминания включены!*\n\n"
                f"🌍 Часовой пояс: {tz_label}\n"
                f"☕ Завтрак — 9:00\n"
                f"🍲 Обед — 13:00\n"
                f"🍽️ Ужин — 19:00\n\n"
                f"Настроить: /notify",
                parse_mode="Markdown"
            )

    elif data.startswith("target_confirm_onb_"):
        target_w = float(data[len("target_confirm_onb_"):])
        db.set_weight_goal(user_id, target_w)
        db.set_target_confirmation(user_id, 'confirmed_low_bmi')
        context.user_data.pop("pending_target_onb", None)
        await query.edit_message_reply_markup(reply_markup=None)
        await _finish_profile(query.message, user_id, context)

    elif data == "target_change_onb":
        context.user_data["profile_step"] = "target_weight"
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            "Напиши другой целевой вес в кг, например: *70*",
            parse_mode="Markdown"
        )

    elif data.startswith("target_confirm_"):
        target_w = float(data[len("target_confirm_"):])
        db.set_weight_goal(user_id, target_w)
        db.set_target_confirmation(user_id, 'confirmed_low_bmi')
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            f"✅ Целевой вес *{target_w} кг* установлен.\n\n"
            f"⚠️ Помни о рекомендации проконсультироваться со специалистом.",
            parse_mode="Markdown"
        )

    elif data == "target_change":
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            "Введи новый целевой вес: `/target 70`",
            parse_mode="Markdown"
        )

    elif data == "show_subscribe":
        left = db.get_free_analyses_left(user_id)
        if left > 0:
            trial_line = f"🎁 Бесплатных анализов осталось: *{left} из {FREE_ANALYSES_LIMIT}*\n\n"
        else:
            trial_line = "❌ Бесплатные анализы закончились\n\n"
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            f"{trial_line}💳 *Подписка Nutrio*\n\nВыбери тариф:",
            parse_mode="Markdown",
            reply_markup=_subscribe_keyboard(),
        )

    elif data in ("sub_1m", "sub_3m"):
        months = 3 if data == "sub_3m" else 1
        price = PRICE_3M if months == 3 else PRICE_1M
        title = f"Подписка Nutrio — {'3 месяца' if months == 3 else '1 месяц'}"
        await context.bot.send_invoice(
            chat_id=query.message.chat_id,
            title=title,
            description="Неограниченный подсчёт калорий и КБЖУ по фото и тексту",
            payload=data,
            currency="XTR",
            prices=[LabeledPrice(title, price)],
        )

    elif data == "quick_add":
        await query.answer()
        await query.message.reply_text(
            "📸 Отправь фото еды или напиши что поел — посчитаю!"
        )

    elif data.startswith("notif_snooze_"):
        meal = data[len("notif_snooze_"):]  # breakfast / lunch / dinner
        notif = db.get_or_create_notifications(user_id)
        db.save_notifications(
            user_id,
            0 if meal == "breakfast" else notif["breakfast_enabled"],
            0 if meal == "lunch"     else notif["lunch_enabled"],
            0 if meal == "dinner"    else notif["dinner_enabled"],
            notif["timezone_offset"],
        )
        meal_names = {"breakfast": "завтрак", "lunch": "обед", "dinner": "ужин"}
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            f"✅ Напоминание про {meal_names.get(meal, meal)} отключено.\n"
            f"Включить обратно: /notify"
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
    msg = await update.message.reply_text(f"🔍 Пересчитываю...")

    try:
        result = await asyncio.get_running_loop().run_in_executor(
            None, analyze_food_correction, meal["food_description"], new_description
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


async def resetme_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    user_id = update.effective_user.id
    with sqlite3.connect(DB_PATH) as conn:
        for table in ("users", "profiles", "meals", "goals", "weight_log", "weight_goal", "notifications"):
            conn.execute(f"DELETE FROM {table} WHERE user_id = ?", (user_id,))
        conn.commit()
    await update.message.reply_text("✅ Все данные сброшены. Напиши /start чтобы начать заново.")


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    with sqlite3.connect(DB_PATH) as conn:
        active_7d = conn.execute(
            "SELECT COUNT(DISTINCT user_id) FROM meals WHERE day >= date('now', '-7 days')"
        ).fetchone()[0]
        total_meals = conn.execute("SELECT COUNT(*) FROM meals").fetchone()[0]

    stats = db.get_subscription_stats()

    await update.message.reply_text(
        f"📊 *Статистика Nutrio*\n\n"
        f"👥 Всего пользователей: *{stats['total']}*\n"
        f"🔥 Активных за 7 дней: *{active_7d}*\n"
        f"🎁 На пробном периоде: *{stats['on_trial']}*\n"
        f"💳 Платных подписчиков: *{stats['paid']}*\n"
        f"💤 Пробный истёк: *{stats['expired']}*\n\n"
        f"🍽️ Всего записей о еде: *{total_meals}*",
        parse_mode="Markdown"
    )


async def notify_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    notif = db.get_or_create_notifications(user_id)
    await update.message.reply_text(
        _notify_text(notif),
        parse_mode="Markdown",
        reply_markup=_notify_keyboard(notif),
    )


async def subscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if db.is_paid_active(user_id):
        sub = db.get_subscription(user_id)
        expires = datetime.fromisoformat(sub["sub_expires_at"]).strftime("%-d %B %Y")
        await update.message.reply_text(
            f"✅ *Подписка активна до {expires}*\n\n"
            "Можешь продлить заранее — срок добавится к текущему:",
            parse_mode="Markdown",
            reply_markup=_subscribe_keyboard(),
        )
    else:
        left = db.get_free_analyses_left(user_id)
        if left > 0:
            trial_line = f"🎁 Бесплатных анализов осталось: *{left} из {FREE_ANALYSES_LIMIT}*\n\n"
        else:
            trial_line = "❌ Бесплатные анализы закончились\n\n"
        await update.message.reply_text(
            f"{trial_line}"
            "💳 *Подписка Nutrio*\n\n"
            "Неограниченный подсчёт калорий по фото и тексту\n\n"
            "Выбери тариф:",
            parse_mode="Markdown",
            reply_markup=_subscribe_keyboard(),
        )


async def pre_checkout_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.pre_checkout_query.answer(ok=True)


async def successful_payment_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    payload = update.message.successful_payment.invoice_payload
    months = 3 if payload == "sub_3m" else 1
    db.activate_subscription(user_id, months)
    label = "3 месяца" if months == 3 else "1 месяц"
    await update.message.reply_text(
        f"🎉 *Подписка активирована на {label}!*\n\n"
        "Считай калории без ограничений 🍽️\n"
        "Отправь фото или напиши что поел ↓",
        parse_mode="Markdown",
        reply_markup=_main_keyboard(),
    )


async def send_reminders(context: ContextTypes.DEFAULT_TYPE):
    """Джоб запускается каждую минуту — рассылает напоминания о приёмах пищи."""
    from datetime import timezone, timedelta

    users = db.get_all_notification_users()
    for user in users:
        tz_offset = user.get("timezone_offset", 3)
        tz = timezone(timedelta(hours=tz_offset))
        now = datetime.now(tz)
        current_time = now.strftime("%H:%M")
        today = now.strftime("%Y-%m-%d")

        meals_to_check = [
            ("breakfast", user["breakfast_enabled"], user["breakfast_time"], "☕", "завтрак"),
            ("lunch",     user["lunch_enabled"],     user["lunch_time"],     "🍲", "обед"),
            ("dinner",    user["dinner_enabled"],     user["dinner_time"],    "🍽️", "ужин"),
        ]

        for meal_type, enabled, meal_time, emoji, name in meals_to_check:
            if not enabled or meal_time != current_time:
                continue
            key = f"{user['user_id']}:{meal_type}:{today}"
            if key in sent_reminders:
                continue
            sent_reminders.add(key)

            meals = db.get_meals_for_day(user["user_id"], today)
            total_cal = sum(m["calories"] for m in meals)
            goal = db.get_goal(user["user_id"])
            profile = db.get_profile(user["user_id"])
            if goal:
                goal_cal = goal["calories"]
            elif profile:
                goal_cal = (profile["target_cal_low"] + profile["target_cal_high"]) // 2
            else:
                goal_cal = 2000

            try:
                await context.bot.send_message(
                    chat_id=user["user_id"],
                    text=(
                        f"{emoji} Не забудь рассказать мне что съел на {name}!\n"
                        f"Цель: {goal_cal} ккал. За сегодня: {total_cal} ккал\n\n"
                        f"📸 Просто отправь фото или напиши текстом"
                    ),
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(f"🍽️ Добавить еду", callback_data="quick_add")],
                        [InlineKeyboardButton(f"❌ Не напоминать про {name}", callback_data=f"notif_snooze_{meal_type}")],
                    ]),
                )
            except Exception as e:
                logger.error(f"Failed to send reminder to {user['user_id']}: {e}")


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
    app.add_handler(CommandHandler("resetme", resetme_command))
    app.add_handler(CommandHandler("stats", stats_command))
    app.add_handler(CommandHandler("notify", notify_command))
    app.add_handler(CommandHandler("subscribe", subscribe_command))
    app.add_handler(PreCheckoutQueryHandler(pre_checkout_handler))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_handler))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(CallbackQueryHandler(callback_handler))

    # Напоминания — проверка каждую минуту
    app.job_queue.run_repeating(send_reminders, interval=60, first=5)

    logger.info("Bot started!")
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == "__main__":
    main()
