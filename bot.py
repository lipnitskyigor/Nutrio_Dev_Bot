import os
import json
import base64
import logging
import asyncio
from datetime import datetime, date
from io import BytesIO

import anthropic
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, LabeledPrice, BotCommand
from telegram import BotCommandScopeChat
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
from i18n import t, detect_lang

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
ADMIN_ID = 148160233

PRICE_1M = 150   # Telegram Stars (~$2)
PRICE_3M = 375   # Telegram Stars (~$5)

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")
db = Database(DATABASE_URL)
claude = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

COMMANDS_BY_LANG = {
    "ru": [
        BotCommand("start",     "🏠 Главное меню"),
        BotCommand("today",     "📊 Итог за сегодня"),
        BotCommand("history",   "📅 История за 7 дней"),
        BotCommand("goal",      "🎯 Дневная цель"),
        BotCommand("weight",    "⚖️ Записать вес"),
        BotCommand("target",    "🏁 Целевой вес"),
        BotCommand("progress",  "📈 Динамика веса"),
        BotCommand("notify",    "🔔 Напоминания"),
        BotCommand("language",  "🌍 Язык / Language"),
        BotCommand("subscribe", "💳 Подписка"),
        BotCommand("reset",     "🗑 Сбросить сегодня"),
        BotCommand("delete",    "❌ Удалить запись"),
        BotCommand("edit",      "✏️ Исправить запись"),
        BotCommand("help",      "❓ Помощь"),
        BotCommand("support",   "💬 Поддержка"),
    ],
    "en": [
        BotCommand("start",     "🏠 Main menu"),
        BotCommand("today",     "📊 Today's summary"),
        BotCommand("history",   "📅 7-day history"),
        BotCommand("goal",      "🎯 Daily goal"),
        BotCommand("weight",    "⚖️ Log weight"),
        BotCommand("target",    "🏁 Target weight"),
        BotCommand("progress",  "📈 Weight progress"),
        BotCommand("notify",    "🔔 Reminders"),
        BotCommand("language",  "🌍 Language"),
        BotCommand("subscribe", "💳 Subscription"),
        BotCommand("reset",     "🗑 Reset today"),
        BotCommand("delete",    "❌ Delete entry"),
        BotCommand("edit",      "✏️ Edit entry"),
        BotCommand("help",      "❓ Help"),
        BotCommand("support",   "💬 Support"),
    ],
    "uk": [
        BotCommand("start",     "🏠 Головне меню"),
        BotCommand("today",     "📊 Підсумок за сьогодні"),
        BotCommand("history",   "📅 Історія за 7 днів"),
        BotCommand("goal",      "🎯 Денна ціль"),
        BotCommand("weight",    "⚖️ Записати вагу"),
        BotCommand("target",    "🏁 Цільова вага"),
        BotCommand("progress",  "📈 Динаміка ваги"),
        BotCommand("notify",    "🔔 Нагадування"),
        BotCommand("language",  "🌍 Мова / Language"),
        BotCommand("subscribe", "💳 Підписка"),
        BotCommand("reset",     "🗑 Скинути сьогодні"),
        BotCommand("delete",    "❌ Видалити запис"),
        BotCommand("edit",      "✏️ Виправити запис"),
        BotCommand("help",      "❓ Допомога"),
        BotCommand("support",   "💬 Підтримка"),
    ],
    "be": [
        BotCommand("start",     "🏠 Галоўнае меню"),
        BotCommand("today",     "📊 Вынік за сёння"),
        BotCommand("history",   "📅 Гісторыя за 7 дзён"),
        BotCommand("goal",      "🎯 Дзённая мэта"),
        BotCommand("weight",    "⚖️ Запісаць вагу"),
        BotCommand("target",    "🏁 Мэтавая вага"),
        BotCommand("progress",  "📈 Дынаміка вагі"),
        BotCommand("notify",    "🔔 Напаміны"),
        BotCommand("language",  "🌍 Мова / Language"),
        BotCommand("subscribe", "💳 Падпіска"),
        BotCommand("reset",     "🗑 Скінуць сёння"),
        BotCommand("delete",    "❌ Выдаліць запіс"),
        BotCommand("edit",      "✏️ Выправіць запіс"),
        BotCommand("help",      "❓ Дапамога"),
        BotCommand("support",   "💬 Падтрымка"),
    ],
    "de": [
        BotCommand("start",     "🏠 Hauptmenü"),
        BotCommand("today",     "📊 Heutige Zusammenfassung"),
        BotCommand("history",   "📅 7-Tage-Verlauf"),
        BotCommand("goal",      "🎯 Tagesziel"),
        BotCommand("weight",    "⚖️ Gewicht erfassen"),
        BotCommand("target",    "🏁 Zielgewicht"),
        BotCommand("progress",  "📈 Gewichtsverlauf"),
        BotCommand("notify",    "🔔 Erinnerungen"),
        BotCommand("language",  "🌍 Sprache / Language"),
        BotCommand("subscribe", "💳 Abonnement"),
        BotCommand("reset",     "🗑 Heute zurücksetzen"),
        BotCommand("delete",    "❌ Eintrag löschen"),
        BotCommand("edit",      "✏️ Eintrag bearbeiten"),
        BotCommand("help",      "❓ Hilfe"),
        BotCommand("support",   "💬 Support"),
    ],
    "pl": [
        BotCommand("start",     "🏠 Menu główne"),
        BotCommand("today",     "📊 Podsumowanie dnia"),
        BotCommand("history",   "📅 Historia 7 dni"),
        BotCommand("goal",      "🎯 Dzienny cel"),
        BotCommand("weight",    "⚖️ Zapisz wagę"),
        BotCommand("target",    "🏁 Waga docelowa"),
        BotCommand("progress",  "📈 Postęp wagi"),
        BotCommand("notify",    "🔔 Przypomnienia"),
        BotCommand("language",  "🌍 Język / Language"),
        BotCommand("subscribe", "💳 Subskrypcja"),
        BotCommand("reset",     "🗑 Resetuj dziś"),
        BotCommand("delete",    "❌ Usuń wpis"),
        BotCommand("edit",      "✏️ Edytuj wpis"),
        BotCommand("help",      "❓ Pomoc"),
        BotCommand("support",   "💬 Wsparcie"),
    ],
    "es": [
        BotCommand("start",     "🏠 Menú principal"),
        BotCommand("today",     "📊 Resumen de hoy"),
        BotCommand("history",   "📅 Historial 7 días"),
        BotCommand("goal",      "🎯 Objetivo diario"),
        BotCommand("weight",    "⚖️ Registrar peso"),
        BotCommand("target",    "🏁 Peso objetivo"),
        BotCommand("progress",  "📈 Progreso de peso"),
        BotCommand("notify",    "🔔 Recordatorios"),
        BotCommand("language",  "🌍 Idioma / Language"),
        BotCommand("subscribe", "💳 Suscripción"),
        BotCommand("reset",     "🗑 Reiniciar hoy"),
        BotCommand("delete",    "❌ Eliminar entrada"),
        BotCommand("edit",      "✏️ Editar entrada"),
        BotCommand("help",      "❓ Ayuda"),
        BotCommand("support",   "💬 Soporte"),
    ],
    "pt": [
        BotCommand("start",     "🏠 Menu principal"),
        BotCommand("today",     "📊 Resumo de hoje"),
        BotCommand("history",   "📅 Histórico 7 dias"),
        BotCommand("goal",      "🎯 Meta diária"),
        BotCommand("weight",    "⚖️ Registrar peso"),
        BotCommand("target",    "🏁 Peso alvo"),
        BotCommand("progress",  "📈 Progresso de peso"),
        BotCommand("notify",    "🔔 Lembretes"),
        BotCommand("language",  "🌍 Idioma / Language"),
        BotCommand("subscribe", "💳 Assinatura"),
        BotCommand("reset",     "🗑 Resetar hoje"),
        BotCommand("delete",    "❌ Excluir entrada"),
        BotCommand("edit",      "✏️ Editar entrada"),
        BotCommand("help",      "❓ Ajuda"),
        BotCommand("support",   "💬 Suporte"),
    ],
    "ar": [
        BotCommand("start",     "🏠 القائمة الرئيسية"),
        BotCommand("today",     "📊 ملخص اليوم"),
        BotCommand("history",   "📅 سجل 7 أيام"),
        BotCommand("goal",      "🎯 الهدف اليومي"),
        BotCommand("weight",    "⚖️ تسجيل الوزن"),
        BotCommand("target",    "🏁 الوزن المستهدف"),
        BotCommand("progress",  "📈 تقدم الوزن"),
        BotCommand("notify",    "🔔 التذكيرات"),
        BotCommand("language",  "🌍 اللغة / Language"),
        BotCommand("subscribe", "💳 الاشتراك"),
        BotCommand("reset",     "🗑 إعادة تعيين اليوم"),
        BotCommand("delete",    "❌ حذف إدخال"),
        BotCommand("edit",      "✏️ تعديل إدخال"),
        BotCommand("help",      "❓ المساعدة"),
        BotCommand("support",   "💬 الدعم"),
    ],
}


def _lang(user_id: int, tg_lang_code: str | None) -> str:
    saved = db.get_user_language(user_id)
    if saved != "auto":
        return saved
    return detect_lang(tg_lang_code)


def _is_menu(text: str, key: str) -> bool:
    from locales import SUPPORTED
    return any(v.get(key) == text for v in SUPPORTED.values())


def analyze_food_text(text: str, lang: str = "ru") -> dict:
    """Send food description to Claude and get calorie analysis."""
    claude_lang = t(lang, "claude_lang")
    response = claude.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a nutrition expert. The user described what they ate: "{text}"

Calculate the approximate calorie content and macros (KBJU).

Reply STRICTLY in JSON format (no markdown, no ```json, just plain JSON):
{{
  "food_description": "what exactly was eaten (clear description {claude_lang})",
  "calories": number (approximate kcal),
  "protein": number (protein in grams),
  "fat": number (fat in grams),
  "carbs": number (carbs in grams),
  "comment": "short comment ({claude_lang}, 1-2 sentences)"
}}

If the text is not about food, return: {{"error": "Not sure what food this is. Please describe in more detail or send a photo!"}}
All numbers must be integers, no fractions."""
            }
        ],
    )

    raw = response.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())


def analyze_food_correction(original_description: str, correction: str, lang: str = "ru") -> dict:
    """Re-analyze a meal with user's correction applied, keeping unchanged items intact."""
    claude_lang = t(lang, "claude_lang")
    response = claude.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a nutrition expert. The user previously logged a dish:
"{original_description}"

Now they want to clarify: "{correction}"

Apply the clarification to the dish (change only what the user mentioned, keep the rest as is) and recalculate the calorie content and macros for the whole dish.

Reply STRICTLY in JSON format (no markdown, no ```json, just plain JSON):
{{
  "food_description": "full description of the dish including the clarification ({claude_lang})",
  "calories": number (kcal for the whole dish),
  "protein": number (protein in grams),
  "fat": number (fat in grams),
  "carbs": number (carbs in grams),
  "comment": "short comment ({claude_lang}, 1-2 sentences)"
}}

All numbers must be integers, no fractions."""
            }
        ],
    )

    raw = response.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())


def analyze_food_image(image_bytes: bytes, caption: str = None, lang: str = "ru") -> dict:
    """Send image to Claude and get calorie analysis."""
    image_b64 = base64.standard_b64encode(image_bytes).decode("utf-8")
    claude_lang = t(lang, "claude_lang")

    caption_hint = f'\nThe user also wrote: "{caption}"' if caption else ""

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
                        "text": f"""You are a nutrition expert. Analyze the food in the photo and estimate the calorie content.{caption_hint}

Reply STRICTLY in JSON format (no markdown, no ```json, just plain JSON):
{{
  "food_description": "what is in the photo ({claude_lang})",
  "calories": number (approximate kcal),
  "protein": number (protein in grams),
  "fat": number (fat in grams),
  "carbs": number (carbs in grams),
  "comment": "short comment about the dish ({claude_lang}, 1-2 sentences)"
}}

If there is no food in the photo, return: {{"error": "No food in the photo"}}
All numbers must be integers, no fractions."""
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


def _goal_label(goal: str, lang: str) -> str:
    return t(lang, f"goal_label_{goal}")


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


def _notify_text(notif: dict, lang: str = "ru") -> str:
    tz = notif["timezone_offset"]
    b = t(lang, "notif_enabled") if notif["breakfast_enabled"] else t(lang, "notif_disabled")
    l = t(lang, "notif_enabled") if notif["lunch_enabled"] else t(lang, "notif_disabled")
    d = t(lang, "notif_enabled") if notif["dinner_enabled"] else t(lang, "notif_disabled")
    return t(lang, "notify_header",
             tz=_tz_str(tz), time=_local_time(tz),
             b_time=notif["breakfast_time"], b=b,
             l_time=notif["lunch_time"], l=l,
             d_time=notif["dinner_time"], d=d)


def _notify_keyboard(notif: dict, lang: str = "ru") -> InlineKeyboardMarkup:
    b_label = f"{t(lang, 'notif_breakfast')} {t(lang, 'notif_enabled') if notif['breakfast_enabled'] else t(lang, 'notif_disabled')}"
    l_label = f"{t(lang, 'notif_lunch')} {t(lang, 'notif_enabled') if notif['lunch_enabled'] else t(lang, 'notif_disabled')}"
    d_label = f"{t(lang, 'notif_dinner')} {t(lang, 'notif_enabled') if notif['dinner_enabled'] else t(lang, 'notif_disabled')}"
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "btn_notif_all_on"), callback_data="notif_all_on"),
            InlineKeyboardButton(t(lang, "btn_notif_all_off"), callback_data="notif_all_off"),
        ],
        [
            InlineKeyboardButton(b_label, callback_data="notif_toggle_breakfast"),
            InlineKeyboardButton(f"🕐 {notif['breakfast_time']}", callback_data="notif_time_breakfast"),
        ],
        [
            InlineKeyboardButton(l_label, callback_data="notif_toggle_lunch"),
            InlineKeyboardButton(f"🕐 {notif['lunch_time']}", callback_data="notif_time_lunch"),
        ],
        [
            InlineKeyboardButton(d_label, callback_data="notif_toggle_dinner"),
            InlineKeyboardButton(f"🕐 {notif['dinner_time']}", callback_data="notif_time_dinner"),
        ],
        [InlineKeyboardButton(t(lang, "btn_notif_change_tz"), callback_data="notif_timezone")],
    ])


def _onboarding_timezone_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "tz_kyiv"),    callback_data="onb_tz_2"),
            InlineKeyboardButton(t(lang, "tz_moscow"),  callback_data="onb_tz_3"),
        ],
        [
            InlineKeyboardButton(t(lang, "tz_baku"),    callback_data="onb_tz_4"),
            InlineKeyboardButton(t(lang, "tz_almaty"),  callback_data="onb_tz_5"),
        ],
        [
            InlineKeyboardButton(t(lang, "tz_tashkent"), callback_data="onb_tz_5"),
            InlineKeyboardButton(t(lang, "tz_novosibirsk"), callback_data="onb_tz_7"),
        ],
        [
            InlineKeyboardButton(t(lang, "tz_irkutsk"),     callback_data="onb_tz_8"),
            InlineKeyboardButton(t(lang, "tz_vladivostok"), callback_data="onb_tz_10"),
        ],
        [InlineKeyboardButton(t(lang, "tz_skip"),  callback_data="onb_tz_skip")],
    ])


def _timezone_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "tz_kyiv"),    callback_data="tz_2"),
            InlineKeyboardButton(t(lang, "tz_moscow"),  callback_data="tz_3"),
        ],
        [
            InlineKeyboardButton(t(lang, "tz_baku"),    callback_data="tz_4"),
            InlineKeyboardButton(t(lang, "tz_almaty"),  callback_data="tz_5"),
        ],
        [
            InlineKeyboardButton(t(lang, "tz_tashkent"), callback_data="tz_5"),
            InlineKeyboardButton(t(lang, "tz_novosibirsk"), callback_data="tz_7"),
        ],
        [
            InlineKeyboardButton(t(lang, "tz_irkutsk"),     callback_data="tz_8"),
            InlineKeyboardButton(t(lang, "tz_vladivostok"), callback_data="tz_10"),
        ],
    ])


def _main_keyboard(lang: str = "ru") -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(t(lang, "menu_diary"))],
            [KeyboardButton(t(lang, "menu_profile")), KeyboardButton(t(lang, "menu_help"))],
        ],
        resize_keyboard=True,
        input_field_placeholder=t(lang, "input_placeholder"),
    )


def _terms_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(t(lang, "btn_accept_terms"), callback_data="accept_terms"),
    ]])


def _subscribe_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(f"1 месяц — {PRICE_1M} ⭐", callback_data="sub_1m"),
        InlineKeyboardButton(f"3 месяца — {PRICE_3M} ⭐", callback_data="sub_3m"),
    ]])


def _paywall_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(t(lang, "btn_subscribe"), callback_data="show_subscribe"),
    ]])


def _trial_notice(left: int, lang: str = "ru") -> str:
    if left == 0:
        return t(lang, "trial_exhausted")
    elif left == 1:
        return t(lang, "trial_last_1", limit=FREE_ANALYSES_LIMIT)
    elif left <= 3:
        return t(lang, "trial_last_few", left=left, limit=FREE_ANALYSES_LIMIT)
    elif left <= 5:
        return t(lang, "trial_some_left", left=left, limit=FREE_ANALYSES_LIMIT)
    else:
        return t(lang, "trial_many_left", left=left, limit=FREE_ANALYSES_LIMIT)


async def _send_terms(message, name: str, lang: str = "ru"):
    await message.reply_text(
        t(lang, "terms_greeting", name=name),
        reply_markup=_terms_keyboard(lang),
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or t("ru", "default_friend")
    user_id = user.id
    lang = _lang(user_id, user.language_code)

    if not db.get_terms_accepted(user_id):
        await _send_terms(update.message, name, lang)
        return

    profile = db.get_profile(user_id)
    meals = db.get_meals_for_day(user_id, date.today().isoformat())

    if profile or meals:
        # Returning user
        await update.message.reply_text(
            t(lang, "welcome_back", name=name),
            parse_mode="Markdown",
            reply_markup=_main_keyboard(lang),
        )
    else:
        # New user — onboarding
        await update.message.reply_text(
            t(lang, "welcome_new"),
            parse_mode="Markdown",
            reply_markup=_main_keyboard(lang),
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = _lang(update.effective_user.id, update.effective_user.language_code)
    await update.message.reply_text(
        t(lang, "help_text"),
        parse_mode="Markdown"
    )


async def support_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = _lang(update.effective_user.id, update.effective_user.language_code)
    await update.message.reply_text(
        t(lang, "support_text"),
        parse_mode="Markdown"
    )


async def today_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)
    user_name = update.effective_user.first_name or t(lang, "default_friend")
    today = date.today().isoformat()

    meals = db.get_meals_for_day_with_ids(user_id, today)

    if not meals:
        await update.message.reply_text(t(lang, "today_empty"))
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

    lines = [t(lang, "today_header", name=user_name)]
    for i, meal in enumerate(meals, 1):
        tm = meal["time"]
        lines.append(t(lang, "today_meal_line", i=i, food=meal['food_description'], cal=meal['calories'], time=tm))

    lines.append(t(lang, "today_total_cal", cal=total_cal))
    lines.append(t(lang, "today_macros", protein=total_protein, fat=total_fat, carbs=total_carbs))

    if cal_left > 0:
        lines.append(t(lang, "today_cal_left", cal_left=cal_left, prot_left=prot_left))
    elif cal_left > -200:
        lines.append(t(lang, "today_cal_done"))
    else:
        lines.append(t(lang, "today_cal_over", over=abs(cal_left)))

    await update.message.reply_text("\n".join(lines), parse_mode="Markdown")


async def history_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)
    user_name = update.effective_user.first_name or t(lang, "default_friend")

    history = db.get_weekly_summary(user_id)

    if not history:
        await update.message.reply_text(t(lang, "history_empty"))
        return

    lines = [t(lang, "history_header", name=user_name)]
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
        if lang == "ru":
            suffix = t(lang, "history_meals_suffix_other") if meals_count >= 5 else t(lang, "history_meals_suffix_1")
        else:
            suffix = t(lang, "history_meals_suffix_1") if meals_count == 1 else t(lang, "history_meals_suffix_other")
        lines.append(t(lang, "history_entry", day=day_str, cal=cal, n=meals_count, suffix=suffix))

    await update.message.reply_text("\n".join(lines), parse_mode="Markdown")


async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)
    today = date.today().isoformat()
    db.delete_meals_for_day(user_id, today)
    await update.message.reply_text(t(lang, "reset_done"))


async def goal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)

    if not context.args:
        goal = db.get_goal(user_id)
        if goal:
            await update.message.reply_text(
                t(lang, "goal_current", cal=goal['calories'], protein=goal['protein']),
                parse_mode="Markdown"
            )
        else:
            await update.message.reply_text(
                t(lang, "goal_not_set"),
                parse_mode="Markdown"
            )
        return

    try:
        calories = int(context.args[0])
        protein = int(context.args[1]) if len(context.args) > 1 else 100
        db.set_goal(user_id, calories, protein)
        await update.message.reply_text(
            t(lang, "goal_saved", cal=calories, protein=protein),
            parse_mode="Markdown"
        )
    except (ValueError, IndexError):
        await update.message.reply_text(
            t(lang, "goal_bad_format"),
            parse_mode="Markdown"
        )


async def weight_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)

    if not context.args:
        latest = db.get_latest_weight(user_id)
        if latest:
            await update.message.reply_text(
                t(lang, "weight_last", weight=latest['weight'], day=latest['day']),
                parse_mode="Markdown"
            )
        else:
            await update.message.reply_text(
                t(lang, "weight_not_set"),
                parse_mode="Markdown"
            )
        return

    try:
        weight = float(context.args[0].replace(",", "."))
        db.log_weight(user_id, weight)

        response = t(lang, "weight_saved", weight=weight)

        target = db.get_weight_goal(user_id)
        if target:
            target_w = target["target_weight"]
            diff = weight - target_w
            if diff > 0:
                response += t(lang, "weight_to_goal", target=target_w, diff=f"{diff:.1f}")
                if diff <= 2:
                    response += t(lang, "weight_almost")
                elif diff <= 5:
                    response += t(lang, "weight_great_progress")
                else:
                    response += t(lang, "weight_good_start")
            elif diff < 0:
                response += t(lang, "weight_goal_reached", diff=f"{abs(diff):.1f}")
            else:
                response += t(lang, "weight_on_goal")
        else:
            response += t(lang, "weight_set_target_hint")

        await update.message.reply_text(response, parse_mode="Markdown")

    except ValueError:
        await update.message.reply_text(
            t(lang, "weight_bad_format"),
            parse_mode="Markdown"
        )


async def progress_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)
    history = db.get_weight_history(user_id, days=7)

    if not history:
        await update.message.reply_text(
            t(lang, "progress_empty"),
            parse_mode="Markdown"
        )
        return

    target = db.get_weight_goal(user_id)
    target_w = target["target_weight"] if target else None

    lines = [t(lang, "progress_header")]
    for i, entry in enumerate(history):
        w = entry["weight"]
        try:
            d = datetime.strptime(entry["day"], "%Y-%m-%d")
            day_str = d.strftime("%-d %b")
        except Exception:
            day_str = entry["day"]

        if i == 0:
            lines.append(t(lang, "progress_entry_first", day=day_str, w=w))
        else:
            prev = history[i - 1]["weight"]
            diff = w - prev
            if diff < 0:
                lines.append(t(lang, "progress_entry_down", day=day_str, w=w, diff=f"{diff:.1f}"))
            elif diff > 0:
                lines.append(t(lang, "progress_entry_up", day=day_str, w=w, diff=f"{diff:.1f}"))
            else:
                lines.append(t(lang, "progress_entry_same", day=day_str, w=w))

    if len(history) >= 2:
        total_diff = history[-1]["weight"] - history[0]["weight"]
        if total_diff < 0:
            lines.append(t(lang, "progress_total_down", diff=f"{total_diff:.1f}"))
        elif total_diff > 0:
            lines.append(t(lang, "progress_total_up", diff=f"{total_diff:.1f}"))
        else:
            lines.append(t(lang, "progress_total_stable"))

    if target_w:
        current = history[-1]["weight"]
        diff_to_goal = current - target_w
        if diff_to_goal > 0:
            lines.append(t(lang, "progress_to_goal", target=target_w, diff=f"{diff_to_goal:.1f}"))
        else:
            lines.append(t(lang, "progress_goal_reached", target=target_w))

    await update.message.reply_text("\n".join(lines), parse_mode="Markdown")


async def target_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)

    if not context.args:
        target = db.get_weight_goal(user_id)
        if target:
            latest = db.get_latest_weight(user_id)
            msg = t(lang, "target_current", target=target['target_weight'])
            if latest:
                diff = latest["weight"] - target["target_weight"]
                if diff > 0:
                    msg += t(lang, "target_remaining", current=latest['weight'], diff=f"{diff:.1f}")
                else:
                    msg += t(lang, "target_reached", current=latest['weight'])
            msg += t(lang, "target_change_hint")
            await update.message.reply_text(msg, parse_mode="Markdown")
        else:
            await update.message.reply_text(
                t(lang, "target_not_set"),
                parse_mode="Markdown"
            )
        return

    try:
        target_w = float(context.args[0].replace(",", "."))
        if not (30 <= target_w <= 300):
            raise ValueError
    except ValueError:
        await update.message.reply_text(
            t(lang, "target_bad_format"),
            parse_mode="Markdown"
        )
        return

    profile = db.get_profile(user_id)
    if not profile or not all([profile.get('height'), profile.get('age'), profile.get('sex'), profile.get('activity')]):
        await update.message.reply_text(
            t(lang, "target_need_profile"),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(t(lang, "btn_setup_profile"), callback_data="profile_yes")
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
        text = t(lang, "target_safe_set", target=target_w, cal=recommended_cal)
        if tdee - 500 < min_cal:
            text += t(lang, "target_min_cal_warn", min_cal=min_cal)
        if weeks > 0:
            text += t(lang, "target_weeks", weeks=weeks)
        await update.message.reply_text(text, parse_mode="Markdown")

    elif bmi >= 17:
        await update.message.reply_text(
            t(lang, "target_warn_low_bmi", target=target_w, bmi=bmi, min_weight=min_weight),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(t(lang, "btn_target_confirm"), callback_data=f"target_confirm_{target_w}"),
                InlineKeyboardButton(t(lang, "btn_target_change"), callback_data="target_change"),
            ]])
        )

    elif bmi >= 16:
        await update.message.reply_text(
            t(lang, "target_danger_bmi", target=target_w, bmi=bmi, height=height, min_weight=min_weight),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(t(lang, "btn_target_confirm_warn"), callback_data=f"target_confirm_{target_w}"),
                InlineKeyboardButton(t(lang, "btn_target_change"), callback_data="target_change"),
            ]])
        )

    else:
        await update.message.reply_text(
            t(lang, "target_critical_bmi", target=target_w, bmi=bmi, min_weight=min_weight),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(t(lang, "btn_target_change"), callback_data="target_change"),
            ]])
        )


def _meal_keyboard(meal_id: int, lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "btn_meal_confirm"), callback_data=f"confirm_{meal_id}"),
            InlineKeyboardButton(t(lang, "btn_meal_edit"), callback_data=f"edit_{meal_id}"),
            InlineKeyboardButton(t(lang, "btn_meal_delete"), callback_data=f"delete_{meal_id}"),
        ]
    ])


DEFAULT_CAL  = 2000   # средняя норма без профиля
DEFAULT_PROT = 100    # средний белок без профиля


def _meal_summary(result: dict, total_cal: int, total_protein: int,
                  meals_count: int, goal: dict, profile: dict = None, lang: str = "ru") -> str:
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

    day_pct = round(total_cal / norm * 100)

    text = t(lang, "meal_summary_header",
             food=result['food_description'],
             cal=cal, protein=prot,
             fat=result['fat'], carbs=result['carbs'],
             comment=result.get('comment', ''),
             total_cal=total_cal, day_pct=day_pct, total_protein=total_protein)

    if profile:
        cal_left  = cal_high - total_cal
        prot_left = max(0, prot_target - total_protein)
        if cal_left > 0:
            text += t(lang, "meal_remaining_profile",
                      cal_left=cal_left, prot_left=prot_left,
                      cal_low=cal_low, cal_high=cal_high)
        elif total_cal <= cal_high + 200:
            text += t(lang, "meal_on_target_profile", cal_low=cal_low, cal_high=cal_high)
        else:
            over = total_cal - cal_high
            text += t(lang, "meal_over_target_profile", over=over)
    else:
        cal_left  = DEFAULT_CAL  - total_cal
        prot_left = max(0, DEFAULT_PROT - total_protein)
        if cal_left > 0:
            text += t(lang, "meal_remaining_default", cal_left=cal_left, prot_left=prot_left)
        elif cal_left > -200:
            text += t(lang, "meal_on_target_default")
        else:
            text += t(lang, "meal_over_target_default", over=abs(cal_left))

    return text


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)
    if not db.get_terms_accepted(user_id):
        await _send_terms(update.message, update.effective_user.first_name or t(lang, "default_friend"), lang)
        return
    if not db.has_access(user_id):
        await update.message.reply_text(
            _trial_notice(0, lang),
            parse_mode="Markdown",
            reply_markup=_paywall_keyboard(lang),
        )
        return
    msg = await update.message.reply_text(t(lang, "analyzing_photo"))

    try:
        photo = update.message.photo[-1]
        photo_file = await photo.get_file()
        buf = BytesIO()
        await photo_file.download_to_memory(buf)
        image_bytes = buf.getvalue()
        caption = update.message.caption.strip() if update.message.caption else None

        result = await asyncio.get_running_loop().run_in_executor(
            None, analyze_food_image, image_bytes, caption, lang
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
            _meal_summary(result, total_cal, total_protein, len(meals), goal, profile, lang),
            parse_mode="Markdown",
            reply_markup=_meal_keyboard(meal_id, lang),
        )
        if not db.is_paid_active(user_id):
            db.use_free_analysis(user_id)
            left = db.get_free_analyses_left(user_id)
            notice = _trial_notice(left, lang)
            if notice:
                await update.message.reply_text(
                    notice,
                    parse_mode="Markdown",
                    reply_markup=_paywall_keyboard(lang) if left == 0 else None,
                )
        await _maybe_send_profile_prompt(update.message, user_id, context, lang)

    except json.JSONDecodeError:
        logger.error("Failed to parse Claude response as JSON")
        await msg.edit_text(t(lang, "analysis_error_parse"))
    except Exception as e:
        logger.error(f"Error processing photo: {e}")
        await msg.edit_text(t(lang, "analysis_error_photo"))


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)

    if not db.get_terms_accepted(user_id):
        await _send_terms(update.message, update.effective_user.first_name or t(lang, "default_friend"), lang)
        return

    # ── Меню-кнопки ───────────────────────────────────────────────
    if _is_menu(text, "menu_add"):
        await update.message.reply_text(t(lang, "menu_add_prompt"))
        return

    if _is_menu(text, "menu_diary"):
        await today_command(update, context)
        return

    if _is_menu(text, "menu_profile"):
        profile = db.get_profile(user_id)
        if not profile:
            await update.message.reply_text(
                t(lang, "profile_not_set"),
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(t(lang, "btn_setup_profile"), callback_data="profile_yes")
                ]])
            )
        else:
            goal_labels = {
                "lose": t(lang, "profile_goal_lose"),
                "maintain": t(lang, "profile_goal_maintain"),
                "gain": t(lang, "profile_goal_gain"),
            }
            activity_labels = {
                "sedentary": t(lang, "profile_activity_sedentary"),
                "light": t(lang, "profile_activity_light"),
                "moderate": t(lang, "profile_activity_moderate"),
                "active": t(lang, "profile_activity_active"),
            }
            protein = round(profile['daily_calories'] * 0.25 / 4)

            latest_weight = db.get_latest_weight(user_id)
            weight_goal = db.get_weight_goal(user_id)
            today = date.today().isoformat()
            meals = db.get_meals_for_day(user_id, today)
            today_cal = sum(m["calories"] for m in meals)

            text_lines = t(lang, "profile_view",
                           goal=goal_labels.get(profile['goal'], profile['goal']),
                           activity=activity_labels.get(profile['activity'], profile['activity']),
                           height=profile['height'], weight=profile['weight'])

            if latest_weight:
                current_w = latest_weight['weight']
                text_lines += t(lang, "profile_last_weight", w=current_w, day=latest_weight['day'])
                if weight_goal:
                    target_w = weight_goal['target_weight']
                    diff = round(current_w - target_w, 1)
                    if abs(diff) < 0.5:
                        text_lines += t(lang, "profile_weight_goal_reached", target=target_w)
                    elif diff > 0:
                        text_lines += t(lang, "profile_weight_to_goal", target=target_w, diff=diff)
                    else:
                        text_lines += t(lang, "profile_weight_to_goal", target=target_w, diff=abs(diff))

            text_lines += t(lang, "profile_norm",
                            low=profile['target_cal_low'], high=profile['target_cal_high'],
                            protein=protein, today_cal=today_cal)

            await update.message.reply_text(
                text_lines,
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(t(lang, "btn_edit_profile"), callback_data="profile_yes")],
                    [InlineKeyboardButton("🌍 Язык / Language", callback_data="open_language")],
                ])
            )
        return

    if _is_menu(text, "menu_help"):
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
                t(lang, "ask_height"),
                parse_mode="Markdown"
            )
        except ValueError:
            await update.message.reply_text(t(lang, "age_bad"), parse_mode="Markdown")
        return

    if step == "height":
        try:
            height = int(text)
            if not (100 <= height <= 250):
                raise ValueError
            context.user_data["p_height"] = height
            context.user_data["profile_step"] = "weight"
            await update.message.reply_text(
                t(lang, "ask_weight"),
                parse_mode="Markdown"
            )
        except ValueError:
            await update.message.reply_text(t(lang, "height_bad"), parse_mode="Markdown")
        return

    if step == "weight":
        try:
            weight = float(text.replace(",", "."))
            if not (30 <= weight <= 300):
                raise ValueError
            context.user_data["p_weight"] = weight
            context.user_data["profile_step"] = "target_weight"
            await update.message.reply_text(
                t(lang, "ask_target_weight"),
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(t(lang, "btn_set_target_yes"), callback_data="ptw_yes"),
                    InlineKeyboardButton(t(lang, "btn_skip"), callback_data="ptw_skip"),
                ]])
            )
        except ValueError:
            await update.message.reply_text(t(lang, "weight_bad"), parse_mode="Markdown")
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
                    await _finish_profile(update.message, user_id, context, lang)

                elif bmi >= 17:
                    context.user_data["pending_target_onb"] = target_w
                    context.user_data.pop("profile_step", None)
                    await update.message.reply_text(
                        t(lang, "target_warn_low_bmi", target=target_w, bmi=bmi, min_weight=min_weight),
                        parse_mode="Markdown",
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton(t(lang, "btn_target_confirm_onb"), callback_data=f"target_confirm_onb_{target_w}"),
                            InlineKeyboardButton(t(lang, "btn_target_change_onb"), callback_data="target_change_onb"),
                        ]])
                    )

                elif bmi >= 16:
                    context.user_data["pending_target_onb"] = target_w
                    context.user_data.pop("profile_step", None)
                    await update.message.reply_text(
                        t(lang, "target_danger_bmi", target=target_w, bmi=bmi, height=height, min_weight=min_weight),
                        parse_mode="Markdown",
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton(t(lang, "btn_target_confirm_onb"), callback_data=f"target_confirm_onb_{target_w}"),
                            InlineKeyboardButton(t(lang, "btn_target_change_onb"), callback_data="target_change_onb"),
                        ]])
                    )

                else:
                    context.user_data["profile_step"] = "target_weight"
                    await update.message.reply_text(
                        t(lang, "target_weight_critical_onb", target=target_w, bmi=bmi, height=height, min_weight=min_weight),
                        parse_mode="Markdown"
                    )
            else:
                db.set_weight_goal(user_id, target_w)
                await _finish_profile(update.message, user_id, context, lang)

        except ValueError:
            await update.message.reply_text(t(lang, "target_weight_bad"), parse_mode="Markdown")
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
                t(lang, "notif_tz_saved", tz=f"UTC{sign}{offset}"),
                parse_mode="Markdown"
            )
        except (ValueError, IndexError):
            await update.message.reply_text(
                t(lang, "timezone_bad"),
                parse_mode="Markdown"
            )
        return

    # ── Режим исправления — пользователь нажал "Исправить" ───────
    if "editing_meal_id" in context.user_data:
        meal_id = context.user_data.pop("editing_meal_id")
        msg = await update.message.reply_text(t(lang, "recalculating"))
        try:
            original_meal = db.get_meal_by_id(meal_id, user_id)
            if original_meal:
                result = await asyncio.get_running_loop().run_in_executor(
                    None, analyze_food_correction, original_meal["food_description"], text, lang
                )
            else:
                result = await asyncio.get_running_loop().run_in_executor(
                    None, analyze_food_text, text, lang
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
                t(lang, "corrected_prefix") + _meal_summary(result, total_cal, total_protein, len(meals), goal, profile, lang),
                parse_mode="Markdown",
                reply_markup=_meal_keyboard(meal_id, lang),
            )
        except Exception as e:
            logger.error(f"Error in editing flow: {e}")
            await msg.edit_text(t(lang, "correction_error"))
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
                t(lang, "notif_timezone_updated", sign=sign, offset=offset) + _notify_text(notif, lang),
                parse_mode="Markdown",
                reply_markup=_notify_keyboard(notif, lang)
            )
        except (ValueError, IndexError):
            await update.message.reply_text(
                t(lang, "timezone_bad"),
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
                meal_name = t(lang, f"meal_name_{meal_type}")
                await update.message.reply_text(
                    t(lang, "notif_time_updated", meal=meal_name, time=time_str)
                    + _notify_text(notif, lang),
                    parse_mode="Markdown",
                    reply_markup=_notify_keyboard(notif, lang),
                )
                return
        await update.message.reply_text(
            t(lang, "notif_time_bad"),
            parse_mode="Markdown",
        )
        return

    # Обычный режим — распознавание еды
    if len(text) < 3:
        await update.message.reply_text(
            t(lang, "short_input_hint"),
            parse_mode="Markdown"
        )
        return

    if not db.has_access(user_id):
        await update.message.reply_text(
            _trial_notice(0, lang),
            parse_mode="Markdown",
            reply_markup=_paywall_keyboard(lang),
        )
        return

    msg = await update.message.reply_text(t(lang, "counting_calories"))

    try:
        result = await asyncio.get_running_loop().run_in_executor(
            None, analyze_food_text, text, lang
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
            _meal_summary(result, total_cal, total_protein, len(meals), goal, profile, lang),
            parse_mode="Markdown",
            reply_markup=_meal_keyboard(meal_id, lang),
        )
        if not db.is_paid_active(user_id):
            db.use_free_analysis(user_id)
            left = db.get_free_analyses_left(user_id)
            notice = _trial_notice(left, lang)
            if notice:
                await update.message.reply_text(
                    notice,
                    parse_mode="Markdown",
                    reply_markup=_paywall_keyboard(lang) if left == 0 else None,
                )
        await _maybe_send_profile_prompt(update.message, user_id, context, lang)

    except json.JSONDecodeError:
        await msg.edit_text(t(lang, "analysis_error_text"))
    except Exception as e:
        logger.error(f"Error processing text: {e}")
        await msg.edit_text(t(lang, "analysis_error_generic"))


def _profile_prompt_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(t(lang, "btn_profile_yes"), callback_data="profile_yes"),
        InlineKeyboardButton(t(lang, "btn_profile_skip"), callback_data="profile_skip"),
    ]])


async def _finish_profile(message, user_id: int, context, lang: str = "ru") -> None:
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
            target_line = t(lang, "profile_target_line_remaining", target=target['target_weight'], diff=f"{diff:.1f}")
        else:
            target_line = t(lang, "profile_target_line_reached", target=target['target_weight'])

    goal_label = t(lang, f"goal_label_{goal}")

    await message.reply_text(
        t(lang, "profile_done",
          goal=goal_label, low=low, high=high, protein=protein, target_line=target_line),
        parse_mode="Markdown"
    )

    context.user_data["profile_step"] = "timezone"
    await message.reply_text(
        t(lang, "ask_timezone"),
        parse_mode="Markdown"
    )


async def _maybe_send_profile_prompt(message, user_id: int, context, lang: str = "ru") -> None:
    """Отправляет приглашение настроить профиль — один раз, сразу после первого результата."""
    profile = db.get_profile(user_id)
    if not profile and not context.user_data.get("profile_prompted"):
        context.user_data["profile_prompted"] = True
        await message.reply_text(
            t(lang, "profile_prompt_title"),
            parse_mode="Markdown",
            reply_markup=_profile_prompt_keyboard(lang),
        )

def _goal_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(t(lang, "btn_goal_lose"), callback_data="pg_lose"),
        InlineKeyboardButton(t(lang, "btn_goal_maintain"), callback_data="pg_maintain"),
        InlineKeyboardButton(t(lang, "btn_goal_gain"), callback_data="pg_gain"),
    ]])

def _sex_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(t(lang, "btn_sex_male"), callback_data="ps_male"),
        InlineKeyboardButton(t(lang, "btn_sex_female"), callback_data="ps_female"),
    ]])

def _activity_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(t(lang, "btn_activity_sedentary"), callback_data="pa_sedentary")],
        [InlineKeyboardButton(t(lang, "btn_activity_light"), callback_data="pa_light")],
        [InlineKeyboardButton(t(lang, "btn_activity_moderate"), callback_data="pa_moderate")],
        [InlineKeyboardButton(t(lang, "btn_activity_active"), callback_data="pa_active")],
    ])


async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)
    await update.message.reply_text(
        t(lang, "choose_language"),
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(t(lang, "btn_lang_ru"), callback_data="set_lang:ru"),
                InlineKeyboardButton(t(lang, "btn_lang_en"), callback_data="set_lang:en"),
            ],
            [
                InlineKeyboardButton(t(lang, "btn_lang_uk"), callback_data="set_lang:uk"),
                InlineKeyboardButton(t(lang, "btn_lang_be"), callback_data="set_lang:be"),
            ],
            [
                InlineKeyboardButton(t(lang, "btn_lang_de"), callback_data="set_lang:de"),
                InlineKeyboardButton(t(lang, "btn_lang_pl"), callback_data="set_lang:pl"),
            ],
            [
                InlineKeyboardButton(t(lang, "btn_lang_es"), callback_data="set_lang:es"),
                InlineKeyboardButton(t(lang, "btn_lang_pt"), callback_data="set_lang:pt"),
            ],
            [
                InlineKeyboardButton(t(lang, "btn_lang_ar"), callback_data="set_lang:ar"),
            ],
        ])
    )


async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data
    lang = _lang(user_id, query.from_user.language_code)

    # ── Language selection ─────────────────────────────────────────
    if data.startswith("set_lang:"):
        chosen = data.split(":")[1]
        db.set_user_language(user_id, chosen)
        confirm_key = {
            "ru": "language_changed_ru",
            "en": "language_changed_en",
            "uk": "language_changed_uk",
            "be": "language_changed_be",
            "de": "language_changed_de",
            "pl": "language_changed_pl",
            "es": "language_changed_es",
            "pt": "language_changed_pt",
            "ar": "language_changed_ar",
        }.get(chosen, "language_changed_en")
        commands = COMMANDS_BY_LANG.get(chosen, COMMANDS_BY_LANG["en"])
        await context.bot.set_my_commands(
            commands,
            scope=BotCommandScopeChat(chat_id=user_id),
        )
        await query.edit_message_text(t(chosen, confirm_key))
        await query.message.reply_text(
            t(chosen, "menu_add_prompt"),
            reply_markup=_main_keyboard(chosen),
        )
        return

    elif data == "open_language":
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            t(lang, "choose_language"),
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(t(lang, "btn_lang_ru"), callback_data="set_lang:ru"),
                    InlineKeyboardButton(t(lang, "btn_lang_en"), callback_data="set_lang:en"),
                ],
                [
                    InlineKeyboardButton(t(lang, "btn_lang_uk"), callback_data="set_lang:uk"),
                    InlineKeyboardButton(t(lang, "btn_lang_be"), callback_data="set_lang:be"),
                ],
                [
                    InlineKeyboardButton(t(lang, "btn_lang_de"), callback_data="set_lang:de"),
                    InlineKeyboardButton(t(lang, "btn_lang_pl"), callback_data="set_lang:pl"),
                ],
                [
                    InlineKeyboardButton(t(lang, "btn_lang_es"), callback_data="set_lang:es"),
                    InlineKeyboardButton(t(lang, "btn_lang_pt"), callback_data="set_lang:pt"),
                ],
                [
                    InlineKeyboardButton(t(lang, "btn_lang_ar"), callback_data="set_lang:ar"),
                ],
            ])
        )
        return

    # ── Terms acceptance ──────────────────────────────────────────
    if data == "accept_terms":
        try:
            db.set_terms_accepted(user_id)
            db.init_subscription(user_id)
            logger.info(f"Terms accepted by {user_id}")
        except Exception as e:
            logger.error(f"Error accepting terms for {user_id}: {e}")
            await query.message.reply_text(t(lang, "error_terms", e=e))
            return
        await query.edit_message_reply_markup(reply_markup=None)
        name = query.from_user.first_name or t(lang, "default_friend")
        profile = db.get_profile(user_id)
        meals = db.get_meals_for_day(user_id, date.today().isoformat())
        if profile or meals:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text=t(lang, "welcome_back", name=name),
                parse_mode="Markdown",
                reply_markup=_main_keyboard(lang),
            )
        else:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text=t(lang, "welcome_new"),
                parse_mode="Markdown",
                reply_markup=_main_keyboard(lang),
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
            remaining_line = t(lang, "diary_cal_left", cal_left=cal_left, prot_left=prot_left)
        elif cal_left > -200:
            remaining_line = t(lang, "diary_cal_done")
        else:
            remaining_line = t(lang, "diary_cal_over", over=abs(cal_left))
        await query.edit_message_text(
            t(lang, "diary_deleted",
              cal=total_cal, protein=total_protein, n=len(meals), remaining=remaining_line),
            parse_mode="Markdown"
        )

    elif data.startswith("edit_"):
        meal_id = int(data.split("_")[1])
        context.user_data["editing_meal_id"] = meal_id
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(t(lang, "edit_prompt"))

    # ── Profile flow ──────────────────────────────────────────────
    elif data == "profile_yes":
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            t(lang, "ask_goal"),
            reply_markup=_goal_keyboard(lang)
        )

    elif data == "profile_skip":
        await query.edit_message_reply_markup(reply_markup=None)

    elif data.startswith("pg_"):  # goal selected
        goal = data[3:]  # lose / maintain / gain
        context.user_data["p_goal"] = goal
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(t(lang, "ask_sex"), reply_markup=_sex_keyboard(lang))

    elif data.startswith("ps_"):  # sex selected
        sex = data[3:]  # male / female
        context.user_data["p_sex"] = sex
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            t(lang, "ask_activity"),
            reply_markup=_activity_keyboard(lang)
        )

    elif data.startswith("pa_"):  # activity selected
        activity = data[3:]  # sedentary / light / moderate / active
        context.user_data["p_activity"] = activity
        context.user_data["profile_step"] = "age"
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            t(lang, "ask_age"),
            parse_mode="Markdown"
        )

    elif data == "ptw_yes":
        context.user_data["profile_step"] = "target_weight"
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            t(lang, "ask_target_weight_enter"),
            parse_mode="Markdown"
        )

    elif data == "ptw_skip":
        await query.edit_message_reply_markup(reply_markup=None)
        await _finish_profile(query.message, user_id, context, lang)

    # ── Notifications ─────────────────────────────────────────────
    elif data in ("notif_all_on", "notif_all_off"):
        notif = db.get_or_create_notifications(user_id)
        val = 1 if data == "notif_all_on" else 0
        db.save_notifications(user_id, val, val, val, notif["timezone_offset"])
        notif = db.get_notifications(user_id)
        await query.edit_message_text(
            _notify_text(notif, lang), parse_mode="Markdown",
            reply_markup=_notify_keyboard(notif, lang)
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
            _notify_text(notif, lang), parse_mode="Markdown",
            reply_markup=_notify_keyboard(notif, lang)
        )

    elif data.startswith("notif_time_"):
        meal_type = data[len("notif_time_"):]  # breakfast / lunch / dinner
        context.user_data["setting_notification_time"] = meal_type
        meal_name = t(lang, f"meal_name_{meal_type}")
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            t(lang, "notif_time_prompt", meal=meal_name),
            parse_mode="Markdown",
        )

    elif data == "notif_timezone":
        context.user_data["setting_timezone"] = True
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            t(lang, "notif_timezone_prompt"),
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
            _notify_text(notif, lang), parse_mode="Markdown",
            reply_markup=_notify_keyboard(notif, lang)
        )

    elif data.startswith("onb_tz_"):
        val = data[len("onb_tz_"):]
        if val == "skip":
            await query.edit_message_reply_markup(reply_markup=None)
            await query.message.reply_text(t(lang, "onb_tz_skip"))
        else:
            offset = int(val)
            db.save_notifications(user_id, 1, 1, 1, offset)
            tz_label = _tz_str(offset)
            await query.edit_message_reply_markup(reply_markup=None)
            await query.message.reply_text(
                t(lang, "onb_tz_saved", tz=tz_label),
                parse_mode="Markdown"
            )

    elif data.startswith("target_confirm_onb_"):
        target_w = float(data[len("target_confirm_onb_"):])
        db.set_weight_goal(user_id, target_w)
        db.set_target_confirmation(user_id, 'confirmed_low_bmi')
        context.user_data.pop("pending_target_onb", None)
        await query.edit_message_reply_markup(reply_markup=None)
        await _finish_profile(query.message, user_id, context, lang)

    elif data == "target_change_onb":
        context.user_data["profile_step"] = "target_weight"
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            t(lang, "target_change_onb_prompt"),
            parse_mode="Markdown"
        )

    elif data.startswith("target_confirm_"):
        target_w = float(data[len("target_confirm_"):])
        db.set_weight_goal(user_id, target_w)
        db.set_target_confirmation(user_id, 'confirmed_low_bmi')
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            t(lang, "target_confirmed_msg", target=target_w),
            parse_mode="Markdown"
        )

    elif data == "target_change":
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            t(lang, "target_change_prompt"),
            parse_mode="Markdown"
        )

    elif data == "show_subscribe":
        left = db.get_free_analyses_left(user_id)
        if left > 0:
            trial_line = t(lang, "subscribe_remaining", left=left, limit=FREE_ANALYSES_LIMIT)
        else:
            trial_line = t(lang, "subscribe_exhausted")
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            trial_line + t(lang, "subscribe_header"),
            parse_mode="Markdown",
            reply_markup=_subscribe_keyboard(),
        )

    elif data in ("sub_1m", "sub_3m"):
        months = 3 if data == "sub_3m" else 1
        price = PRICE_3M if months == 3 else PRICE_1M
        title_key = "sub_invoice_title_3m" if months == 3 else "sub_invoice_title_1m"
        title = t(lang, title_key)
        try:
            await context.bot.send_invoice(
                chat_id=query.message.chat_id,
                title=title,
                description=t(lang, "sub_invoice_desc"),
                payload=data,
                provider_token="",
                currency="XTR",
                prices=[LabeledPrice(title, price)],
            )
        except Exception as e:
            logger.error(f"send_invoice error: {e}")
            await query.message.reply_text(t(lang, "sub_invoice_error", e=e))

    elif data == "quick_add":
        await query.answer()
        await query.message.reply_text(t(lang, "quick_add_prompt"))

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
        meal_name = t(lang, f"meal_name_{meal}")
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text(
            t(lang, "notif_snooze_done", meal=meal_name)
        )


async def delete_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)
    today = date.today().isoformat()

    if not context.args:
        await update.message.reply_text(
            t(lang, "delete_no_num"),
            parse_mode="Markdown"
        )
        return

    try:
        num = int(context.args[0])
    except ValueError:
        await update.message.reply_text(t(lang, "delete_bad_num"), parse_mode="Markdown")
        return

    meals = db.get_meals_for_day_with_ids(user_id, today)

    if not meals:
        await update.message.reply_text(t(lang, "delete_no_meals"))
        return

    if num < 1 or num > len(meals):
        await update.message.reply_text(
            t(lang, "delete_out_of_range", num=num, total=len(meals)),
            parse_mode="Markdown"
        )
        return

    meal = meals[num - 1]
    db.delete_meal_by_id(meal["id"], user_id)

    remaining = db.get_meals_for_day_with_ids(user_id, today)
    total_cal = sum(m["calories"] for m in remaining)

    await update.message.reply_text(
        t(lang, "delete_done",
          food=meal['food_description'], cal=meal['calories'],
          total_cal=total_cal, n=len(remaining)),
        parse_mode="Markdown"
    )


async def edit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)
    today = date.today().isoformat()

    if not context.args or len(context.args) < 2:
        await update.message.reply_text(
            t(lang, "edit_no_args"),
            parse_mode="Markdown"
        )
        return

    try:
        num = int(context.args[0])
    except ValueError:
        await update.message.reply_text(t(lang, "edit_bad_num"), parse_mode="Markdown")
        return

    new_description = " ".join(context.args[1:])
    meals = db.get_meals_for_day_with_ids(user_id, today)

    if not meals:
        await update.message.reply_text(t(lang, "edit_no_meals"))
        return

    if num < 1 or num > len(meals):
        await update.message.reply_text(
            t(lang, "edit_out_of_range", num=num, total=len(meals)),
            parse_mode="Markdown"
        )
        return

    meal = meals[num - 1]
    msg = await update.message.reply_text(t(lang, "recalculating"))

    try:
        result = await asyncio.get_running_loop().run_in_executor(
            None, analyze_food_correction, meal["food_description"], new_description, lang
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
            t(lang, "edit_done",
              num=num,
              food=result['food_description'],
              cal=result['calories'], protein=result['protein'],
              fat=result['fat'], carbs=result['carbs'],
              total_cal=total_cal, total_protein=total_protein),
            parse_mode="Markdown"
        )

    except Exception as e:
        logger.error(f"Error in edit_command: {e}")
        await msg.edit_text(t(lang, "correction_error"))


async def resetme_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    user_id = update.effective_user.id
    import psycopg2
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            for table in ("users", "profiles", "meals", "goals", "weight_log", "weight_goal", "notifications"):
                cur.execute(f"DELETE FROM {table} WHERE user_id = %s", (user_id,))
        conn.commit()
    await update.message.reply_text(t("ru", "resetme_done"))


async def gift_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    if not context.args:
        await update.message.reply_text(t("ru", "gift_usage"))
        return
    try:
        target_id = int(context.args[0])
    except ValueError:
        await update.message.reply_text(t("ru", "gift_bad_id"))
        return
    db.gift_access(target_id)
    await update.message.reply_text(t("ru", "gift_done", uid=target_id))


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    import psycopg2
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(DISTINCT user_id) FROM meals WHERE day >= (CURRENT_DATE - INTERVAL '7 days')::TEXT")
            active_7d = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM meals")
            total_meals = cur.fetchone()[0]

    stats = db.get_subscription_stats()

    await update.message.reply_text(
        f"📊 *Статистика Meal Scan*\n\n"
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
    lang = _lang(user_id, update.effective_user.language_code)
    notif = db.get_or_create_notifications(user_id)
    await update.message.reply_text(
        _notify_text(notif, lang),
        parse_mode="Markdown",
        reply_markup=_notify_keyboard(notif, lang),
    )


async def subscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)
    if db.is_paid_active(user_id):
        sub = db.get_subscription(user_id)
        expires = datetime.fromisoformat(sub["sub_expires_at"]).strftime("%-d %B %Y")
        await update.message.reply_text(
            t(lang, "subscribe_active", expires=expires),
            parse_mode="Markdown",
            reply_markup=_subscribe_keyboard(),
        )
    else:
        left = db.get_free_analyses_left(user_id)
        if left > 0:
            trial_line = t(lang, "subscribe_remaining", left=left, limit=FREE_ANALYSES_LIMIT)
        else:
            trial_line = t(lang, "subscribe_exhausted")
        await update.message.reply_text(
            trial_line + t(lang, "subscribe_header_full"),
            parse_mode="Markdown",
            reply_markup=_subscribe_keyboard(),
        )


async def pre_checkout_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.pre_checkout_query.answer(ok=True)


async def successful_payment_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = _lang(user_id, update.effective_user.language_code)
    payload = update.message.successful_payment.invoice_payload
    months = 3 if payload == "sub_3m" else 1
    db.activate_subscription(user_id, months)
    label = t(lang, "sub_3m_label") if months == 3 else t(lang, "sub_1m_label")
    await update.message.reply_text(
        t(lang, "payment_success", label=label),
        parse_mode="Markdown",
        reply_markup=_main_keyboard(lang),
    )


async def send_reminders(context: ContextTypes.DEFAULT_TYPE):
    """Джоб запускается каждую минуту — рассылает напоминания о приёмах пищи."""
    from datetime import timezone, timedelta

    # Чистим старые ключи (старше сегодня) чтобы set не рос бесконечно
    cutoff = datetime.utcnow().strftime("%Y-%m-%d")
    stale = {k for k in sent_reminders if k.split(":")[-1] < cutoff}
    sent_reminders.difference_update(stale)

    users = db.get_all_notification_users()
    for user in users:
        tz_offset = user.get("timezone_offset", 3)
        tz = timezone(timedelta(hours=tz_offset))
        now = datetime.now(tz)
        current_time = now.strftime("%H:%M")
        today = now.strftime("%Y-%m-%d")

        meals_to_check = [
            ("breakfast", user["breakfast_enabled"], user["breakfast_time"], "☕"),
            ("lunch",     user["lunch_enabled"],     user["lunch_time"],     "🍲"),
            ("dinner",    user["dinner_enabled"],     user["dinner_time"],    "🍽️"),
        ]

        for meal_type, enabled, meal_time, emoji in meals_to_check:
            if not enabled or meal_time != current_time:
                continue
            key = f"{user['user_id']}:{meal_type}:{today}"
            if key in sent_reminders:
                continue

            try:
                user_lang = db.get_user_language(user["user_id"])
                if user_lang == "auto":
                    user_lang = "ru"  # default for reminders
                meal_name = t(user_lang, f"meal_name_{meal_type}")
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

                await context.bot.send_message(
                    chat_id=user["user_id"],
                    text=t(user_lang, "reminder_text",
                           emoji=emoji, meal=meal_name,
                           goal_cal=goal_cal, total_cal=total_cal),
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(t(user_lang, "btn_reminder_add"), callback_data="quick_add")],
                        [InlineKeyboardButton(t(user_lang, "btn_reminder_snooze", meal=meal_name), callback_data=f"notif_snooze_{meal_type}")],
                    ]),
                )
                sent_reminders.add(key)
            except Exception as e:
                logger.error(f"Failed to send reminder to {user['user_id']}: {e}")

    # Онбординг-подсказка про вес — на 2й день в 09:00
    try:
        tip_users = db.get_users_for_weight_tip()
        for user in tip_users:
            tz_offset = user.get("timezone_offset", 3)
            tz = timezone(timedelta(hours=tz_offset))
            now = datetime.now(tz)
            if now.strftime("%H:%M") != "09:00":
                continue
            try:
                user_lang = db.get_user_language(user["user_id"])
                if user_lang == "auto":
                    user_lang = "ru"
                await context.bot.send_message(
                    chat_id=user["user_id"],
                    text=t(user_lang, "weight_tip"),
                    parse_mode="Markdown",
                )
                db.mark_weight_tip_sent(user["user_id"])
            except Exception as e:
                logger.error(f"Failed to send weight tip to {user['user_id']}: {e}")
    except Exception as e:
        logger.error(f"Weight tip job error: {e}")


def main():
    async def post_init(application):
        bot = application.bot

        # ── 1. Команды по языкам ──────────────────────────────────────

        for lang_code, commands in COMMANDS_BY_LANG.items():
            await bot.set_my_commands(commands, language_code=lang_code)

        await bot.set_my_commands(COMMANDS_BY_LANG["en"])

        # ── 2. Короткое описание (about, до 120 символов) ─────────────

        short_descriptions = {
            "ru": "AI-сканер КБЖУ + дневник питания и веса 🍎",
            "en": "AI calorie scanner + nutrition & weight diary 🍎",
            "uk": "AI-сканер КБЖУ + щоденник харчування і ваги 🍎",
            "be": "AI-сканер БЖВ + дзённік харчавання і вагі 🍎",
            "de": "KI-Kalorien-Scanner + Ernährungs- & Gewichtstagebuch 🍎",
            "pl": "Skaner kalorii AI + dziennik żywienia i wagi 🍎",
            "es": "Escáner de calorías IA + diario de nutrición y peso 🍎",
            "pt": "Scanner de calorias IA + diário de nutrição e peso 🍎",
            "ar": "ماسح سعرات AI + يوميات التغذية والوزن 🍎",
        }

        # ── 3. Полное описание (до /start, до 512 символов) ───────────

        full_descriptions = {
            "ru": (
                "Отправь фото еды — получи калории и КБЖУ за секунды.\n\n"
                "📸 Анализ по фото и тексту\n"
                "📔 Дневник питания с историей\n"
                "⚖️ Трекер веса и прогресса\n"
                "🔔 Напоминания о приёмах пищи\n"
                "🎯 Персональные цели по калориям"
            ),
            "en": (
                "Send a food photo — get calories and macros in seconds.\n\n"
                "📸 Analysis from photo and text\n"
                "📔 Nutrition diary with history\n"
                "⚖️ Weight and progress tracker\n"
                "🔔 Meal reminders\n"
                "🎯 Personal calorie goals"
            ),
            "uk": (
                "Надішли фото їжі — отримай калорії та КБЖБ за секунди.\n\n"
                "📸 Аналіз за фото і текстом\n"
                "📔 Щоденник харчування з історією\n"
                "⚖️ Трекер ваги і прогресу\n"
                "🔔 Нагадування про прийоми їжі\n"
                "🎯 Персональні цілі за калоріями"
            ),
            "be": (
                "Дашлі фота ежы — атрымай калорыі і БЖВ за секунды.\n\n"
                "📸 Аналіз па фота і тэксце\n"
                "📔 Дзённік харчавання з гісторыяй\n"
                "⚖️ Трэкер вагі і прагрэсу\n"
                "🔔 Напаміны аб прыёмах ежы\n"
                "🎯 Персанальныя мэты па калорыях"
            ),
            "de": (
                "Sende ein Foto — erhalte Kalorien und Makros in Sekunden.\n\n"
                "📸 Analyse per Foto und Text\n"
                "📔 Ernährungstagebuch mit Verlauf\n"
                "⚖️ Gewichts- und Fortschritts-Tracker\n"
                "🔔 Mahlzeit-Erinnerungen\n"
                "🎯 Persönliche Kalorienziele"
            ),
            "pl": (
                "Wyślij zdjęcie jedzenia — otrzymaj kalorie i makro w sekundy.\n\n"
                "📸 Analiza ze zdjęcia i tekstu\n"
                "📔 Dziennik żywienia z historią\n"
                "⚖️ Tracker wagi i postępu\n"
                "🔔 Przypomnienia o posiłkach\n"
                "🎯 Osobiste cele kaloryczne"
            ),
            "es": (
                "Envía una foto — obtén calorías y macros en segundos.\n\n"
                "📸 Análisis por foto y texto\n"
                "📔 Diario nutricional con historial\n"
                "⚖️ Tracker de peso y progreso\n"
                "🔔 Recordatorios de comidas\n"
                "🎯 Objetivos calóricos personales"
            ),
            "pt": (
                "Envie uma foto — obtenha calorias e macros em segundos.\n\n"
                "📸 Análise por foto e texto\n"
                "📔 Diário nutricional com histórico\n"
                "⚖️ Tracker de peso e progresso\n"
                "🔔 Lembretes de refeições\n"
                "🎯 Metas calóricas pessoais"
            ),
            "ar": (
                "أرسل صورة طعام — احصل على السعرات والمغذيات في ثوانٍ.\n\n"
                "📸 تحليل من الصور والنص\n"
                "📔 يوميات التغذية مع السجل\n"
                "⚖️ متتبع الوزن والتقدم\n"
                "🔔 تذكيرات الوجبات\n"
                "🎯 أهداف السعرات الشخصية"
            ),
        }

        for lang_code, text in short_descriptions.items():
            await bot.set_my_short_description(text, language_code=lang_code)

        for lang_code, text in full_descriptions.items():
            await bot.set_my_description(text, language_code=lang_code)

        await bot.set_my_short_description(short_descriptions["en"])
        await bot.set_my_description(full_descriptions["en"])

    app = Application.builder().token(TELEGRAM_TOKEN).post_init(post_init).build()

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
    app.add_handler(CommandHandler("gift", gift_command))
    app.add_handler(CommandHandler("resetme", resetme_command))
    app.add_handler(CommandHandler("stats", stats_command))
    app.add_handler(CommandHandler("notify", notify_command))
    app.add_handler(CommandHandler("subscribe", subscribe_command))
    app.add_handler(CommandHandler("support", support_command))
    app.add_handler(CommandHandler("language", language_command))
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
