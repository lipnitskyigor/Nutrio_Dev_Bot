texts = {
    # ── Menu buttons ──────────────────────────────────────────────
    "menu_diary": "📔 Diary",
    "menu_profile": "👤 Profile",
    "menu_help": "❓ Help",
    "menu_add": "🍽️ Add meal",
    "input_placeholder": "Send a photo or type what you ate...",

    # ── Language switching ────────────────────────────────────────
    "choose_language": "Choose language:",
    "language_changed_ru": "✅ Язык изменён на русский 🇷🇺",
    "language_changed_en": "✅ Language changed to English 🇬🇧",
    "btn_lang_ru": "🇷🇺 Русский",
    "btn_lang_en": "🇬🇧 English",
    "btn_lang_de": "🇩🇪 Deutsch",
    "btn_lang_pl": "🇵🇱 Polski",
    "btn_lang_es": "🇪🇸 Español",
    "btn_lang_pt": "🇧🇷 Português",
    "btn_lang_ar": "🇸🇦 العربية",

    # ── Claude API instruction ────────────────────────────────────
    "claude_lang": "in English",

    # ── Terms ─────────────────────────────────────────────────────
    "terms_greeting": "👋 Hi, {name}!\n\nBefore we start, please read this:\n\n⚠️ Meal Scan is a calorie and nutrition tracking assistant.\nThis is not a medical app. The bot does not replace a doctor,\ndietitian or nutritionist.\n\n📄 Terms of use: mealscan.org/terms.html\n\nBy tapping the button below you agree to the terms of use.",
    "btn_accept_terms": "✅ Accept terms",

    # ── Start / Welcome ───────────────────────────────────────────
    "welcome_back": "Welcome back, {name}! 👋\n\n📸 Send a photo of your food or type what you ate — I'll calculate.",
    "welcome_new": "I help you track your nutrition — I count calories and macros from photos or text.\n\n📸 *Send a photo of any dish*\n✏️ Or type what you ate\n\nTry it right now ↓\n\n———\nℹ️ Meal Scan is a nutrition tracking assistant, not a medical app. If you have any health conditions or are about to change your diet, consult a doctor or dietitian first.",
    "default_friend": "friend",

    # ── Help ──────────────────────────────────────────────────────
    "help_text": (
        "🤖 *How to use the bot:*\n\n"
        "📸 Send a food photo — I'll calculate calories and macros\n"
        "✏️ Type what you ate — I'll calculate that too\n"
        "For example: _«buckwheat with chicken 300g»_\n\n"
        "📊 *Calories & nutrition:*\n"
        "/today — today's total (calories, protein, fat, carbs)\n"
        "/history — nutrition history for the past 7 days\n"
        "/goal 2000 150 — set a daily calorie & protein goal\n"
        "/goal — view your current goal\n"
        "/reset — clear today's entries\n\n"
        "⚖️ *Weight & progress:*\n"
        "/weight 80.5 — log your weight (do it every day)\n"
        "/weight — view your last logged weight\n"
        "/target 75 — set your target weight\n"
        "/target — view target weight and how far you are\n"
        "/progress — weight dynamics for 7 days with 🟢🔴 changes\n\n"
        "💡 Tip: the clearer the food in the photo, the more accurate the result!\n\n"
        "🔔 *Reminders:*\n"
        "/notify — configure meal reminders\n\n"
        "💬 *Support:*\n"
        "/support — contact support"
    ),

    # ── Support ───────────────────────────────────────────────────
    "support_text": "💬 *Meal Scan Support*\n\nIf you have a question or problem — write to us:\n\n👉 @MealScanSupport",

    # ── Today ─────────────────────────────────────────────────────
    "today_empty": "📭 No food entries for today yet.\nSend a photo of a dish to start counting!",
    "today_header": "📊 *Today's total — {name}*\n",
    "today_meal_line": "{i}. {food} — {cal} kcal ({time})",
    "today_total_cal": "\n🔥 *Total: {cal} kcal*",
    "today_macros": "🥩 Protein: {protein} g  🧈 Fat: {fat} g  🍞 Carbs: {carbs} g",
    "today_cal_left": "\n🎯 Remaining to goal: *{cal_left} kcal* and *{prot_left} g protein*",
    "today_cal_done": "\n✅ *Calorie goal reached!*",
    "today_cal_over": "\n⚠️ Goal exceeded by *{over} kcal*",

    # ── History ───────────────────────────────────────────────────
    "history_empty": "📭 No data for the past 7 days.\nSend a food photo to start!",
    "history_header": "📅 *7-day history — {name}*\n",
    "history_entry": "📆 {day}: *{cal} kcal* ({n} meal{suffix})",
    "history_meals_suffix_1": "",
    "history_meals_suffix_other": "s",

    # ── Reset ─────────────────────────────────────────────────────
    "reset_done": "🗑️ Today's data has been cleared!",

    # ── Goal ──────────────────────────────────────────────────────
    "goal_current": "🎯 *Your daily goal:*\n🔥 Calories: {cal} kcal\n🥩 Protein: {protein} g\n\nTo change: `/goal 2000 150`",
    "goal_not_set": "🎯 Goal not set.\n\nSet it like this: `/goal calories protein`\nFor example: `/goal 2000 150`",
    "goal_saved": "✅ *Goal set!*\n🔥 Calories: {cal} kcal/day\n🥩 Protein: {protein} g/day",
    "goal_bad_format": "❌ Wrong format. Use: `/goal 2000 150`",

    # ── Weight ────────────────────────────────────────────────────
    "weight_last": "⚖️ *Last weight:* {weight} kg ({day})\n\nTo log a new one: `/weight 80.5`",
    "weight_not_set": "⚖️ No weight logged yet.\n\nLog it like this: `/weight 80.5`",
    "weight_saved": "⚖️ *Weight logged:* {weight} kg\n",
    "weight_to_goal": "\n🎯 To goal ({target} kg): *{diff} kg* remaining\n",
    "weight_almost": "💪 Almost there! You're so close to your goal!",
    "weight_great_progress": "🔥 Great progress, keep it up!",
    "weight_good_start": "💪 Good start! Every day brings you closer to your goal.",
    "weight_goal_reached": "\n🏆 Goal reached! You're {diff} kg below your target weight!",
    "weight_on_goal": "\n🎯 You're exactly at your target weight! Excellent!",
    "weight_set_target_hint": "\n💡 Set your target weight with `/target 75`",
    "weight_bad_format": "❌ Wrong format. Use: `/weight 80.5`",

    # ── Progress ──────────────────────────────────────────────────
    "progress_empty": "⚖️ No weight data.\n\nLog your weight every day with `/weight 80.5` — I'll show you the dynamics!",
    "progress_header": "📈 *Weight dynamics:*\n",
    "progress_entry_first": "📅 {day}: *{w} kg*",
    "progress_entry_down": "📅 {day}: *{w} kg* (🟢 {diff} kg)",
    "progress_entry_up": "📅 {day}: *{w} kg* (🔴 +{diff} kg)",
    "progress_entry_same": "📅 {day}: *{w} kg* (➡️ no change)",
    "progress_total_down": "\n📉 For the period: *{diff} kg* — great result!",
    "progress_total_up": "\n📈 For the period: *+{diff} kg*",
    "progress_total_stable": "\n➡️ For the period: weight is stable",
    "progress_to_goal": "🎯 To goal ({target} kg): *{diff} kg* remaining",
    "progress_goal_reached": "🏆 Goal {target} kg — *reached!*",

    # ── Target ────────────────────────────────────────────────────
    "target_current": "🎯 *Target weight:* {target} kg\n",
    "target_remaining": "📍 Current weight: {current} kg — *{diff} kg* remaining",
    "target_reached": "🏆 Current weight: {current} kg — goal reached!",
    "target_change_hint": "\n\nChange: `/target 70`",
    "target_not_set": "🎯 Target weight not set.\n\nSet it like this: `/target 75`",
    "target_bad_format": "❌ Wrong format. Use: `/target 75`",
    "target_need_profile": "📋 To check the safety of the goal, a profile is needed (height, age, sex, activity).\n\nSet up your profile — and I'll check how safe your goal is.",
    "btn_setup_profile": "👉 Set up profile",
    "target_safe_set": "✅ *Goal set: {target} kg*\n\n📊 Recommended calories: *{cal} kcal/day*\n",
    "target_min_cal_warn": "⚠️ _Minimum safe calories: {min_cal} kcal/day_\n",
    "target_weeks": "⏱ Estimated time: *{weeks} weeks*",
    "target_warn_low_bmi": "⚠️ Target weight *{target} kg* gives a BMI of *{bmi}* — below normal.\nMinimum recommended weight for your height: *{min_weight} kg*.\n\nPlease consult a specialist before starting.",
    "target_danger_bmi": "🚨 Target weight *{target} kg* — BMI *{bmi}*, dangerously low.\nRecommended minimum for height {height} cm: *{min_weight} kg*.\n\nWe strongly recommend consulting a doctor.",
    "target_critical_bmi": "❌ Cannot set goal *{target} kg*.\nBMI *{bmi}* is critically low and life-threatening.\n\nMinimum safe weight for your height: *{min_weight} kg*.\nPlease see a doctor or dietitian.",
    "btn_target_confirm": "✅ Set anyway",
    "btn_target_confirm_warn": "⚠️ Set anyway (not recommended)",
    "btn_target_change": "✏️ Change goal",
    "target_confirmed_msg": "✅ Target weight *{target} kg* set.\n\n⚠️ Remember the recommendation to consult a specialist.",
    "target_change_prompt": "Enter a new target weight: `/target 70`",

    # ── Meal analysis ─────────────────────────────────────────────
    "analyzing_photo": "🔍 Analyzing photo...",
    "counting_calories": "🔍 Counting calories...",
    "recalculating": "🔍 Recalculating...",
    "analysis_error_parse": "😔 Couldn't parse the response. Try again or take a clearer photo.",
    "analysis_error_photo": "😔 An error occurred while analyzing the photo. Try again!",
    "analysis_error_text": "😔 Couldn't parse that. Try describing it in more detail!",
    "analysis_error_generic": "😔 An error occurred. Try again!",
    "correction_error": "😔 Couldn't recalculate. Try describing it in more detail!",
    "corrected_prefix": "✅ *Corrected!*\n\n",

    # ── Meal summary ──────────────────────────────────────────────
    "meal_summary_header": "🍽️ *{food}*\n\n🔥 *{cal} kcal*\n🥩 Protein: *{protein} g*\n🧈 Fat: {fat} g\n🍞 Carbs: {carbs} g\n\n💬 _{comment}_\n\n📊 *Today's total:*\n🔥 {total_cal} kcal (~{day_pct}% of daily norm)  🥩 protein: *{total_protein} g*",
    "meal_remaining_profile": "\n\n🎯 Remaining to target: *~{cal_left} kcal* and *~{prot_left} g protein*\n_(target: {cal_low}–{cal_high} kcal/day)_",
    "meal_on_target_profile": "\n\n✅ Within target! ({cal_low}–{cal_high} kcal/day)",
    "meal_over_target_profile": "\n\n⚠️ Above target by ~*{over} kcal*",
    "meal_remaining_default": "\n\n🎯 Remaining to average norm: *~{cal_left} kcal* and *~{prot_left} g protein*",
    "meal_on_target_default": "\n\n✅ Average norm reached!",
    "meal_over_target_default": "\n\n⚠️ Above average norm by *{over} kcal*",

    # ── Meal keyboard ─────────────────────────────────────────────
    "btn_meal_confirm": "✅ Correct",
    "btn_meal_edit": "✏️ Edit",
    "btn_meal_delete": "🗑️ Delete",
    "edit_prompt": "✏️ Type the correction — I'll recalculate:",
    "quick_add_prompt": "📸 Send a photo of your food or type what you ate — I'll calculate!",
    "menu_add_prompt": "📸 Send a photo of your food or type what you ate — I'll calculate!",

    # ── Short input hint ──────────────────────────────────────────
    "short_input_hint": "📸 Send a food photo or type what you ate — I'll count the calories!\n\nFor example: *«a bowl of soup and bread»* or *«2 eggs, coffee with milk»*",

    # ── Profile ───────────────────────────────────────────────────
    "profile_not_set": "📋 *Profile not set up*\n\nFill in your profile — and I'll calculate your calorie norm and progress more accurately.",
    "btn_edit_profile": "✏️ Edit profile",
    "profile_goal_lose": "Lose weight 🥦",
    "profile_goal_maintain": "Maintain weight ⚖️",
    "profile_goal_gain": "Gain muscle 💪",
    "profile_activity_sedentary": "Sedentary 🪑",
    "profile_activity_light": "Light 🚶",
    "profile_activity_moderate": "Moderate 🏃",
    "profile_activity_active": "Active 💪",
    "profile_view": "👤 *Your profile*\n\n🎯 Goal: {goal}\n⚡ Activity: {activity}\n📏 Height: {height} cm\n⚖️ Weight: {weight} kg\n",
    "profile_last_weight": "📅 Last weight: *{w} kg* ({day})\n",
    "profile_weight_goal_reached": "🏁 Weight goal: *{target} kg* — reached! 🎉\n",
    "profile_weight_to_goal": "🏁 To goal ({target} kg): *{diff} kg*\n",
    "profile_norm": "\n🔥 Norm: *{low}–{high} kcal/day*\n🥩 Protein: *{protein} g/day*\n📊 Eaten today: *{today_cal} kcal*",

    # ── Onboarding / Profile flow ─────────────────────────────────
    "profile_prompt_title": "📊 *Let's set up calories for you and your goal*\n\nAnswer 4 questions — and the calculation will be more accurate\nTakes less than 30 seconds",
    "btn_profile_yes": "👉 Let's go",
    "btn_profile_skip": "Skip",
    "ask_goal": "What is your goal?",
    "ask_sex": "Your sex?",
    "ask_activity": "Your lifestyle?",
    "ask_age": "How old are you?\n\nType a number, for example: *28*",
    "ask_height": "Your height?\n\nType in centimetres, for example: *178*",
    "ask_weight": "Your current weight?\n\nType in kilograms, for example: *75*",
    "ask_target_weight": "Do you have a target weight?",
    "btn_set_target_yes": "✏️ Yes, I'll set it",
    "btn_skip": "Skip",
    "ask_target_weight_enter": "Type your target weight in kg, for example: *70*",
    "age_bad": "Type your age as a number, for example: *28*",
    "height_bad": "Type your height as a number in cm, for example: *178*",
    "weight_bad": "Type your weight as a number in kg, for example: *75*",
    "target_weight_bad": "Type weight as a number in kg, for example: *70*",
    "target_weight_critical_onb": "❌ Target weight *{target} kg* — BMI *{bmi}*, critically dangerous.\nMinimum safe weight for height {height} cm: *{min_weight} kg*.\n\nType a different target weight:",
    "btn_target_confirm_onb": "✅ Set anyway",
    "btn_target_change_onb": "✏️ Change goal",
    "target_change_onb_prompt": "Type a different target weight in kg, for example: *70*",

    # goal labels (used in _finish_profile)
    "goal_label_lose": "Lose weight",
    "goal_label_maintain": "Maintain weight",
    "goal_label_gain": "Gain muscle",

    # ── Profile goal buttons ──────────────────────────────────────
    "btn_goal_lose": "📉 Lose weight",
    "btn_goal_maintain": "⚖️ Maintain weight",
    "btn_goal_gain": "📈 Gain muscle",
    "btn_sex_male": "👨 Male",
    "btn_sex_female": "👩 Female",
    "btn_activity_sedentary": "🪑 Sedentary (office, no sport)",
    "btn_activity_light": "🚶 Light activity (1–2 times a week)",
    "btn_activity_moderate": "🏃 Moderate (3–5 times a week)",
    "btn_activity_active": "💪 Active (every day)",

    # ── Finish profile ────────────────────────────────────────────
    "profile_done": "✅ *All set!*\n\n🎯 Goal: *{goal}*\n🔥 Calories: *{low}–{high} kcal/day*\n🥩 Protein: *~{protein} g/day*{target_line}\n\nAfter each meal I'll show how many kcal are left to your goal 🎯",
    "profile_target_line_remaining": "\n⚖️ Target weight: *{target} kg* (~{diff} kg remaining)",
    "profile_target_line_reached": "\n⚖️ Target weight: *{target} kg* — already reached! 🏆",
    "ask_timezone": "🔔 *Let's set up reminders for nutrition tracking!*\n\nI'll remind you to log your food — just send a photo or type what you ate.\n\nType the current time for you, for example: *23:15*",

    # ── Notifications ─────────────────────────────────────────────
    "notify_header": "⏰ *Reminder settings*\n\n🌍 Timezone: {tz} (now {time})\n\n☕ Breakfast — {b_time} ({b})\n🍲 Lunch — {l_time} ({l})\n🍽️ Dinner — {d_time} ({d})\n\n⚠️ We recommend keeping at least 1 reminder enabled",
    "btn_notif_all_on": "✅ Enable all",
    "btn_notif_all_off": "❌ Disable all",
    "btn_notif_change_tz": "🌍 Change timezone",
    "notif_enabled": "✅",
    "notif_disabled": "❌",
    "notif_breakfast": "☕ Breakfast",
    "notif_lunch": "🍲 Lunch",
    "notif_dinner": "🍽️ Dinner",
    "notif_time_prompt": "⏰ Type the new reminder time for *{meal}*\n\nFormat: *HH:MM*, for example: *08:30*",
    "notif_timezone_prompt": "🕐 Type the current time for you, for example: *23:15*\n\nI'll determine your timezone automatically.",
    "notif_timezone_updated": "✅ Timezone updated: UTC{sign}{offset}\n\n",
    "notif_time_updated": "✅ Reminder time ({meal}) updated: *{time}*\n\n",
    "notif_time_bad": "❌ Didn't understand the time. Type it in *HH:MM* format, for example: *08:30*",
    "timezone_bad": "Didn't understand 🤔 Type the time in *HH:MM* format, for example: *23:15*",
    "meal_name_breakfast": "breakfast",
    "meal_name_lunch": "lunch",
    "meal_name_dinner": "dinner",
    "notif_tz_saved": "🔔 *Reminders enabled!*\n\n🌍 Timezone: {tz}\n☕ Breakfast — 9:00\n🍲 Lunch — 13:00\n🍽️ Dinner — 19:00\n\nConfigure: /notify",
    "onb_tz_saved": "🔔 *Reminders enabled!*\n\n🌍 Timezone: {tz}\n☕ Breakfast — 9:00\n🍲 Lunch — 13:00\n🍽️ Dinner — 19:00\n\nConfigure: /notify",
    "onb_tz_skip": "OK, no reminders 👌\nEnable anytime: /notify",
    "notif_snooze_done": "✅ Reminder for {meal} disabled.\nEnable again: /notify",

    # ── Timezone city names ───────────────────────────────────────
    "tz_kyiv": "🇺🇦 Kyiv",
    "tz_moscow": "🇷🇺 Moscow",
    "tz_baku": "🇦🇿 Baku",
    "tz_almaty": "🇰🇿 Almaty",
    "tz_tashkent": "🇺🇿 Tashkent",
    "tz_novosibirsk": "Novosibirsk",
    "tz_irkutsk": "Irkutsk",
    "tz_vladivostok": "Vladivostok",
    "tz_skip": "❌ Skip",

    # ── Trial / Paywall ───────────────────────────────────────────
    "trial_exhausted": "❌ *Free analyses used up* (15 of 15)\n\nGet a subscription to continue counting calories 👇",
    "trial_last_1": "⚠️ *1 free analysis* left of {limit} → /subscribe",
    "trial_last_few": "⚠️ *{left} free analyses* left of {limit} → /subscribe",
    "trial_some_left": "🎁 {left} free analyses left of {limit} → /subscribe",
    "trial_many_left": "🎁 Free analyses: {left} of {limit}",
    "btn_subscribe": "💳 Get subscription",
    "subscribe_remaining": "🎁 Free analyses remaining: *{left} of {limit}*\n\n",
    "subscribe_exhausted": "❌ Free analyses used up\n\n",
    "subscribe_header": "💳 *Meal Scan Subscription*\n\nChoose a plan:",
    "subscribe_header_full": "💳 *Meal Scan Subscription*\n\nUnlimited calorie counting from photos and text\n\nChoose a plan:",
    "subscribe_active": "✅ *Subscription active until {expires}*\n\nYou can renew early — time will be added to the current period:",
    "payment_success": "🎉 *Subscription activated for {label}!*\n\nCount calories without limits 🍽️\nSend a photo or type what you ate ↓",
    "sub_1m_label": "1 month",
    "sub_3m_label": "3 months",
    "sub_invoice_title_1m": "Meal Scan Subscription — 1 month",
    "sub_invoice_title_3m": "Meal Scan Subscription — 3 months",
    "sub_invoice_desc": "Unlimited calorie and macro counting from photos and text",
    "sub_invoice_error": "❌ Invoice creation error: {e}",

    # ── Delete command ────────────────────────────────────────────
    "delete_no_num": "❌ Specify a meal number.\nExample: `/delete 2`\n\nToday's list: /today",
    "delete_bad_num": "❌ The number must be an integer. For example: `/delete 2`",
    "delete_no_meals": "📭 No food entries for today.",
    "delete_out_of_range": "❌ No meal #{num}. Today's entries: {total}.\n\nView list: /today",
    "delete_done": "🗑️ Deleted: *{food}* ({cal} kcal)\n\n📊 Today's remaining: *{total_cal} kcal* ({n} meals)",

    # ── Edit command ──────────────────────────────────────────────
    "edit_no_args": "✏️ Format: `/edit number new description`\nExample: `/edit 2 beef borscht 400g`\n\nToday's list: /today",
    "edit_bad_num": "❌ Specify a number first. For example: `/edit 2 borscht 400g`",
    "edit_no_meals": "📭 No food entries for today.",
    "edit_out_of_range": "❌ No meal #{num}. Today's entries: {total}.",
    "edit_done": "✅ *Meal #{num} updated*\n\n🍽️ {food}\n🔥 {cal} kcal | 🥩 {protein} g | 🧈 {fat} g | 🍞 {carbs} g\n\n📊 Today: *{total_cal} kcal* / 🥩 *{total_protein} g protein*",

    # ── Delete from diary (callback) ──────────────────────────────
    "diary_deleted": "🗑️ Entry deleted.\n\n📊 Eaten today: *{cal} kcal* / 🥩 *{protein} g protein* ({n} meals)\n{remaining}",
    "diary_cal_left": "🎯 Remaining to goal: *{cal_left} kcal* and *{prot_left} g protein*",
    "diary_cal_done": "✅ Calorie goal reached!",
    "diary_cal_over": "⚠️ Goal exceeded by *{over} kcal*",

    # ── Reminders ─────────────────────────────────────────────────
    "reminder_text": "{emoji} Don't forget to tell me what you had for {meal}!\nGoal: {goal_cal} kcal. Today: {total_cal} kcal\n\n📸 Just send a photo or type it",
    "btn_reminder_add": "🍽️ Add meal",
    "btn_reminder_snooze": "❌ Stop reminding about {meal}",

    # ── Weight tip ────────────────────────────────────────────────
    "weight_tip": "⚖️ *Tip: track your weight*\n\nYou can log your weight every morning — the bot will show you dynamics and progress towards your goal.\n\nJust type /weight and enter your current weight.\nProgress chart: /progress",

    # ── Admin ─────────────────────────────────────────────────────
    "resetme_done": "✅ All data cleared. Type /start to begin again.",
    "gift_usage": "Usage: /gift <user_id>",
    "gift_bad_id": "❌ user_id must be a number",
    "gift_done": "✅ User {uid} granted permanent access.",
    "error_terms": "❌ Error: {e}",
    "error_invoice": "❌ Invoice creation error: {e}",
}
