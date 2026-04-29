texts = {
    # ── Menu buttons ──────────────────────────────────────────────
    "menu_diary": "📔 السجل",
    "menu_profile": "👤 الملف الشخصي",
    "menu_help": "❓ المساعدة",
    "menu_add": "🍽️ إضافة وجبة",
    "input_placeholder": "أرسل صورة أو اكتب ما أكلته...",

    # ── Language switching ────────────────────────────────────────
    "choose_language": "اختر اللغة:",
    "language_changed_ru": "✅ Язык изменён на русский 🇷🇺",
    "language_changed_en": "✅ Language changed to English 🇬🇧",
    "language_changed_de": "✅ Sprache auf Deutsch geändert 🇩🇪",
    "language_changed_pl": "✅ Język zmieniony na polski 🇵🇱",
    "language_changed_es": "✅ Idioma cambiado a español 🇪🇸",
    "language_changed_pt": "✅ Idioma alterado para português 🇧🇷",
    "language_changed_ar": "✅ تم تغيير اللغة إلى العربية 🇸🇦",
    "btn_lang_ru": "🇷🇺 Русский",
    "btn_lang_en": "🇬🇧 English",
    "btn_lang_de": "🇩🇪 Deutsch",
    "btn_lang_pl": "🇵🇱 Polski",
    "btn_lang_es": "🇪🇸 Español",
    "btn_lang_pt": "🇧🇷 Português",
    "btn_lang_ar": "🇸🇦 العربية",

    # ── Claude API instruction ────────────────────────────────────
    "claude_lang": "باللغة العربية",

    # ── Terms ─────────────────────────────────────────────────────
    "terms_greeting": "👋 مرحباً، {name}!\n\nقبل البدء، يرجى قراءة هذا:\n\n⚠️ Meal Scan مساعد لحساب السعرات الحرارية والمغذيات.\nهذا ليس تطبيقاً طبياً. البوت لا يغني عن الطبيب\nأو أخصائي التغذية.\n\n📄 شروط الاستخدام: mealscan.org/terms.html\n\nبالنقر على الزر أدناه توافق على شروط الاستخدام.",
    "btn_accept_terms": "✅ أوافق على الشروط",

    # ── Start / Welcome ───────────────────────────────────────────
    "welcome_back": "مرحباً بعودتك، {name}! 👋\n\n📸 أرسل صورة وجبتك أو اكتب ما أكلته — سأحسب السعرات.",
    "welcome_new": "أساعدك في تتبع تغذيتك — أحسب السعرات الحرارية والمغذيات من الصور أو النص.\n\n📸 *أرسل صورة أي وجبة*\n✏️ أو اكتب ما أكلته\n\nجرّب الآن ↓\n\n———\nℹ️ Meal Scan مساعد غذائي، وليس تطبيقاً طبياً. إذا كانت لديك مشاكل صحية، استشر طبيباً أو أخصائي تغذية.",
    "default_friend": "صديق",

    # ── Help ──────────────────────────────────────────────────────
    "help_text": (
        "🤖 *كيفية استخدام البوت:*\n\n"
        "📸 أرسل صورة طعام — سأحسب السعرات والمغذيات\n"
        "✏️ اكتب ما أكلته — سأحسب ذلك أيضاً\n"
        "مثال: _«دجاج مع أرز 300 غرام»_\n\n"
        "📊 *السعرات والتغذية:*\n"
        "/today — ملخص اليوم (سعرات، بروتين، دهون، كربوهيدرات)\n"
        "/history — سجل الأيام السبعة الماضية\n"
        "/goal 2000 150 — تحديد الهدف اليومي للسعرات والبروتين\n"
        "/goal — عرض الهدف الحالي\n"
        "/reset — حذف سجلات اليوم\n\n"
        "⚖️ *الوزن والتقدم:*\n"
        "/weight 80.5 — تسجيل الوزن (افعل ذلك يومياً)\n"
        "/weight — عرض آخر وزن مسجل\n"
        "/target 75 — تحديد الوزن المستهدف\n"
        "/target — عرض الوزن المستهدف والمتبقي\n"
        "/progress — تطور الوزن لـ 7 أيام مع 🟢🔴\n\n"
        "💡 نصيحة: كلما كانت الصورة أوضح، كانت النتيجة أدق!\n\n"
        "🔔 *التذكيرات:*\n"
        "/notify — ضبط تذكيرات الوجبات\n\n"
        "💬 *الدعم:*\n"
        "/support — التواصل مع الدعم"
    ),

    # ── Support ───────────────────────────────────────────────────
    "support_text": "💬 *دعم Meal Scan*\n\nلديك سؤال أو مشكلة؟ راسلنا:\n\n👉 @MealScanSupport",

    # ── Today ─────────────────────────────────────────────────────
    "today_empty": "📭 لا توجد وجبات مسجلة اليوم.\nأرسل صورة طبق للبدء في الحساب!",
    "today_header": "📊 *ملخص اليوم — {name}*\n",
    "today_meal_line": "{i}. {food} — {cal} سعرة ({time})",
    "today_total_cal": "\n🔥 *الإجمالي: {cal} سعرة*",
    "today_macros": "🥩 بروتين: {protein} غ  🧈 دهون: {fat} غ  🍞 كربوهيدرات: {carbs} غ",
    "today_cal_left": "\n🎯 المتبقي للهدف: *{cal_left} سعرة* و*{prot_left} غ بروتين*",
    "today_cal_done": "\n✅ *تم تحقيق هدف السعرات اليومي!*",
    "today_cal_over": "\n⚠️ تجاوزت الهدف بـ *{over} سعرة*",

    # ── History ───────────────────────────────────────────────────
    "history_empty": "📭 لا توجد بيانات للأيام السبعة الماضية.\nأرسل صورة للبدء!",
    "history_header": "📅 *سجل 7 أيام — {name}*\n",
    "history_entry": "📆 {day}: *{cal} سعرة* ({n} وجبة{suffix})",
    "history_meals_suffix_1": "",
    "history_meals_suffix_other": "ات",

    # ── Reset ─────────────────────────────────────────────────────
    "reset_done": "🗑️ تم حذف بيانات اليوم!",

    # ── Goal ──────────────────────────────────────────────────────
    "goal_current": "🎯 *هدفك اليومي:*\n🔥 السعرات: {cal} سعرة\n🥩 البروتين: {protein} غ\n\nللتغيير: `/goal 2000 150`",
    "goal_not_set": "🎯 لم يتم تحديد هدف.\n\nحدده هكذا: `/goal سعرات بروتين`\nمثال: `/goal 2000 150`",
    "goal_saved": "✅ *تم تحديد الهدف!*\n🔥 السعرات: {cal} سعرة/يوم\n🥩 البروتين: {protein} غ/يوم",
    "goal_bad_format": "❌ صيغة غير صحيحة. استخدم: `/goal 2000 150`",

    # ── Weight ────────────────────────────────────────────────────
    "weight_last": "⚖️ *آخر وزن:* {weight} كغ ({day})\n\nلتسجيل وزن جديد: `/weight 80.5`",
    "weight_not_set": "⚖️ لم يتم تسجيل وزن بعد.\n\nسجّله هكذا: `/weight 80.5`",
    "weight_saved": "⚖️ *تم تسجيل الوزن:* {weight} كغ\n",
    "weight_to_goal": "\n🎯 للوصول إلى الهدف ({target} كغ): *{diff} كغ* متبقية\n",
    "weight_almost": "💪 أوشكت على الوصول! أنت قريب جداً من هدفك!",
    "weight_great_progress": "🔥 تقدم رائع، استمر هكذا!",
    "weight_good_start": "💪 بداية جيدة! كل يوم يقربك أكثر من هدفك.",
    "weight_goal_reached": "\n🏆 تم تحقيق الهدف! أنت أقل بـ {diff} كغ من وزنك المستهدف!",
    "weight_on_goal": "\n🎯 أنت بالضبط عند وزنك المستهدف! ممتاز!",
    "weight_set_target_hint": "\n💡 حدد وزناً مستهدفاً بالأمر `/target 75`",
    "weight_bad_format": "❌ صيغة غير صحيحة. استخدم: `/weight 80.5`",

    # ── Progress ──────────────────────────────────────────────────
    "progress_empty": "⚖️ لا توجد بيانات وزن.\n\nسجّل وزنك يومياً بالأمر `/weight 80.5` — سأريك التطور!",
    "progress_header": "📈 *تطور الوزن:*\n",
    "progress_entry_first": "📅 {day}: *{w} كغ*",
    "progress_entry_down": "📅 {day}: *{w} كغ* (🟢 {diff} كغ)",
    "progress_entry_up": "📅 {day}: *{w} كغ* (🔴 +{diff} كغ)",
    "progress_entry_same": "📅 {day}: *{w} كغ* (➡️ بدون تغيير)",
    "progress_total_down": "\n📉 خلال الفترة: *{diff} كغ* — نتيجة رائعة!",
    "progress_total_up": "\n📈 خلال الفترة: *+{diff} كغ*",
    "progress_total_stable": "\n➡️ خلال الفترة: الوزن مستقر",
    "progress_to_goal": "🎯 للوصول إلى الهدف ({target} كغ): *{diff} كغ* متبقية",
    "progress_goal_reached": "🏆 الهدف {target} كغ — *تم تحقيقه!*",

    # ── Target ────────────────────────────────────────────────────
    "target_current": "🎯 *الوزن المستهدف:* {target} كغ\n",
    "target_remaining": "📍 الوزن الحالي: {current} كغ — *{diff} كغ* متبقية",
    "target_reached": "🏆 الوزن الحالي: {current} كغ — تم تحقيق الهدف!",
    "target_change_hint": "\n\nللتغيير: `/target 70`",
    "target_not_set": "🎯 لم يتم تحديد وزن مستهدف.\n\nحدده هكذا: `/target 75`",
    "target_bad_format": "❌ صيغة غير صحيحة. استخدم: `/target 75`",
    "target_need_profile": "📋 للتحقق من سلامة الهدف، يلزم ملف شخصي (الطول، العمر، الجنس، النشاط).\n\nأعدّ ملفك الشخصي — سأتحقق من مدى أمان هدفك.",
    "btn_setup_profile": "👉 إعداد الملف الشخصي",
    "target_safe_set": "✅ *تم تحديد الهدف: {target} كغ*\n\n📊 السعرات الموصى بها: *{cal} سعرة/يوم*\n",
    "target_min_cal_warn": "⚠️ _الحد الأدنى الآمن للسعرات: {min_cal} سعرة/يوم_\n",
    "target_weeks": "⏱ الوقت المقدر: *{weeks} أسبوع*",
    "target_warn_low_bmi": "⚠️ الوزن المستهدف *{target} كغ* يعطي مؤشر كتلة جسم *{bmi}* — أقل من الطبيعي.\nالحد الأدنى الموصى به لطولك: *{min_weight} كغ*.\n\nيرجى استشارة أخصائي قبل البدء.",
    "target_danger_bmi": "🚨 الوزن المستهدف *{target} كغ* — مؤشر كتلة جسم *{bmi}*، منخفض بشكل خطير.\nالحد الأدنى الموصى به لطول {height} سم: *{min_weight} كغ*.\n\nنوصي بشدة باستشارة طبيب.",
    "target_critical_bmi": "❌ لا يمكن تحديد هدف *{target} كغ*.\nمؤشر كتلة الجسم *{bmi}* منخفض بشكل حرج ويهدد الحياة.\n\nالحد الأدنى الآمن لطولك: *{min_weight} كغ*.\nيرجى مراجعة طبيب أو أخصائي تغذية.",
    "btn_target_confirm": "✅ تحديد على أي حال",
    "btn_target_confirm_warn": "⚠️ تحديد على أي حال (غير موصى به)",
    "btn_target_change": "✏️ تغيير الهدف",
    "target_confirmed_msg": "✅ تم تحديد الوزن المستهدف *{target} كغ*.\n\n⚠️ تذكر التوصية باستشارة أخصائي.",
    "target_change_prompt": "أدخل وزناً مستهدفاً جديداً: `/target 70`",

    # ── Meal analysis ─────────────────────────────────────────────
    "analyzing_photo": "🔍 جارٍ تحليل الصورة...",
    "counting_calories": "🔍 جارٍ حساب السعرات...",
    "recalculating": "🔍 جارٍ إعادة الحساب...",
    "analysis_error_parse": "😔 لم أتمكن من معالجة الرد. حاول مرة أخرى أو التقط صورة أوضح.",
    "analysis_error_photo": "😔 حدث خطأ أثناء تحليل الصورة. حاول مرة أخرى!",
    "analysis_error_text": "😔 لم أفهم. حاول وصف الطعام بشكل أكثر تفصيلاً!",
    "analysis_error_generic": "😔 حدث خطأ. حاول مرة أخرى!",
    "correction_error": "😔 لم أتمكن من إعادة الحساب. صف الطعام بشكل أكثر تفصيلاً!",
    "corrected_prefix": "✅ *تم التصحيح!*\n\n",

    # ── Meal summary ──────────────────────────────────────────────
    "meal_summary_header": "🍽️ *{food}*\n\n🔥 *{cal} سعرة*\n🥩 بروتين: *{protein} غ*\n🧈 دهون: {fat} غ\n🍞 كربوهيدرات: {carbs} غ\n\n💬 _{comment}_\n\n📊 *ملخص اليوم:*\n🔥 {total_cal} سعرة (~{day_pct}% من المعدل)  🥩 بروتين: *{total_protein} غ*",
    "meal_remaining_profile": "\n\n🎯 المتبقي للهدف: *~{cal_left} سعرة* و*~{prot_left} غ بروتين*\n_(الهدف: {cal_low}–{cal_high} سعرة/يوم)_",
    "meal_on_target_profile": "\n\n✅ ضمن الهدف! ({cal_low}–{cal_high} سعرة/يوم)",
    "meal_over_target_profile": "\n\n⚠️ تجاوزت الهدف بـ ~*{over} سعرة*",
    "meal_remaining_default": "\n\n🎯 المتبقي للمعدل: *~{cal_left} سعرة* و*~{prot_left} غ بروتين*",
    "meal_on_target_default": "\n\n✅ تم بلوغ المعدل المتوسط!",
    "meal_over_target_default": "\n\n⚠️ تجاوزت المعدل المتوسط بـ *{over} سعرة*",

    # ── Meal keyboard ─────────────────────────────────────────────
    "btn_meal_confirm": "✅ صحيح",
    "btn_meal_edit": "✏️ تعديل",
    "btn_meal_delete": "🗑️ حذف",
    "edit_prompt": "✏️ اكتب التصحيح — سأعيد الحساب:",
    "quick_add_prompt": "📸 أرسل صورة وجبتك أو اكتب ما أكلته — سأحسب!",
    "menu_add_prompt": "📸 أرسل صورة وجبتك أو اكتب ما أكلته — سأحسب!",

    # ── Short input hint ──────────────────────────────────────────
    "short_input_hint": "📸 أرسل صورة أو اكتب وجبتك — سأحسب السعرات الحرارية!\n\nمثال: *«طبق حساء وخبز»* أو *«بيضتان، قهوة بالحليب»*",

    # ── Profile ───────────────────────────────────────────────────
    "profile_not_set": "📋 *لم يتم إعداد الملف الشخصي*\n\nأكمل ملفك الشخصي — سأحسب معدل السعرات والتقدم بدقة أكبر.",
    "btn_edit_profile": "✏️ تعديل الملف الشخصي",
    "profile_goal_lose": "إنقاص الوزن 🥦",
    "profile_goal_maintain": "الحفاظ على الوزن ⚖️",
    "profile_goal_gain": "زيادة الكتلة العضلية 💪",
    "profile_activity_sedentary": "خامل 🪑",
    "profile_activity_light": "خفيف 🚶",
    "profile_activity_moderate": "معتدل 🏃",
    "profile_activity_active": "مرتفع 💪",
    "profile_view": "👤 *ملفك الشخصي*\n\n🎯 الهدف: {goal}\n⚡ النشاط: {activity}\n📏 الطول: {height} سم\n⚖️ الوزن: {weight} كغ\n",
    "profile_last_weight": "📅 آخر وزن: *{w} كغ* ({day})\n",
    "profile_weight_goal_reached": "🏁 هدف الوزن: *{target} كغ* — تم تحقيقه! 🎉\n",
    "profile_weight_to_goal": "🏁 للوصول إلى الهدف ({target} كغ): *{diff} كغ*\n",
    "profile_norm": "\n🔥 المعدل: *{low}–{high} سعرة/يوم*\n🥩 البروتين: *{protein} غ/يوم*\n📊 المتناول اليوم: *{today_cal} سعرة*",

    # ── Onboarding / Profile flow ─────────────────────────────────
    "profile_prompt_title": "📊 *لنضبط السعرات وفق احتياجاتك وهدفك*\n\nأجب على 4 أسئلة — سيكون الحساب أدق\nيستغرق أقل من 30 ثانية",
    "btn_profile_yes": "👉 حسناً، لنبدأ",
    "btn_profile_skip": "تخطي",
    "ask_goal": "ما هو هدفك؟",
    "ask_sex": "ما جنسك؟",
    "ask_activity": "ما مستوى نشاطك؟",
    "ask_age": "كم عمرك؟\n\nأدخل رقماً، مثال: *28*",
    "ask_height": "ما طولك؟\n\nبالسنتيمتر، مثال: *178*",
    "ask_weight": "ما وزنك الحالي؟\n\nبالكيلوغرام، مثال: *75*",
    "ask_target_weight": "هل لديك وزن مستهدف؟",
    "btn_set_target_yes": "✏️ نعم، سأحدده",
    "btn_skip": "تخطي",
    "ask_target_weight_enter": "أدخل الوزن المستهدف بالكغ، مثال: *70*",
    "age_bad": "أدخل العمر كرقم، مثال: *28*",
    "height_bad": "أدخل الطول كرقم بالسنتيمتر، مثال: *178*",
    "weight_bad": "أدخل الوزن كرقم بالكيلوغرام، مثال: *75*",
    "target_weight_bad": "أدخل الوزن كرقم بالكيلوغرام، مثال: *70*",
    "target_weight_critical_onb": "❌ الوزن المستهدف *{target} كغ* — مؤشر كتلة جسم *{bmi}*، خطير بشكل حرج.\nالحد الأدنى الآمن لطول {height} سم: *{min_weight} كغ*.\n\nأدخل وزناً مستهدفاً آخر:",
    "btn_target_confirm_onb": "✅ تحديد على أي حال",
    "btn_target_change_onb": "✏️ تغيير الهدف",
    "target_change_onb_prompt": "أدخل وزناً مستهدفاً آخر بالكغ، مثال: *70*",

    # goal labels (used in _finish_profile)
    "goal_label_lose": "إنقاص الوزن",
    "goal_label_maintain": "الحفاظ على الوزن",
    "goal_label_gain": "زيادة الكتلة العضلية",

    # ── Profile goal buttons ──────────────────────────────────────
    "btn_goal_lose": "📉 إنقاص الوزن",
    "btn_goal_maintain": "⚖️ الحفاظ على الوزن",
    "btn_goal_gain": "📈 زيادة الكتلة العضلية",
    "btn_sex_male": "👨 ذكر",
    "btn_sex_female": "👩 أنثى",
    "btn_activity_sedentary": "🪑 خامل (مكتب، بدون رياضة)",
    "btn_activity_light": "🚶 خفيف (1–2 مرات/أسبوع)",
    "btn_activity_moderate": "🏃 معتدل (3–5 مرات/أسبوع)",
    "btn_activity_active": "💪 مرتفع (كل يوم)",

    # ── Finish profile ────────────────────────────────────────────
    "profile_done": "✅ *كل شيء جاهز!*\n\n🎯 الهدف: *{goal}*\n🔥 السعرات: *{low}–{high} سعرة/يوم*\n🥩 البروتين: *~{protein} غ/يوم*{target_line}\n\nبعد كل وجبة سأريك كم تبقى من السعرات 🎯",
    "profile_target_line_remaining": "\n⚖️ الوزن المستهدف: *{target} كغ* (~{diff} كغ متبقية)",
    "profile_target_line_reached": "\n⚖️ الوزن المستهدف: *{target} كغ* — تم تحقيقه بالفعل! 🏆",
    "ask_timezone": "🔔 *لنضبط تذكيرات الوجبات!*\n\nسأذكّرك بتسجيل وجباتك — فقط أرسل صورة أو اكتب ما أكلته.\n\nكم الساعة الآن عندك؟ مثال: *23:15*",

    # ── Notifications ─────────────────────────────────────────────
    "notify_header": "⏰ *إعدادات التذكيرات*\n\n🌍 المنطقة الزمنية: {tz} (الآن {time})\n\n☕ الإفطار — {b_time} ({b})\n🍲 الغداء — {l_time} ({l})\n🍽️ العشاء — {d_time} ({d})\n\n⚠️ نوصي بإبقاء تذكير واحد على الأقل مفعلاً",
    "btn_notif_all_on": "✅ تفعيل الكل",
    "btn_notif_all_off": "❌ إيقاف الكل",
    "btn_notif_change_tz": "🌍 تغيير المنطقة الزمنية",
    "notif_enabled": "✅",
    "notif_disabled": "❌",
    "notif_breakfast": "☕ الإفطار",
    "notif_lunch": "🍲 الغداء",
    "notif_dinner": "🍽️ العشاء",
    "notif_time_prompt": "⏰ أدخل وقت التذكير الجديد لـ *{meal}*\n\nالصيغة: *HH:MM*، مثال: *08:30*",
    "notif_timezone_prompt": "🕐 أدخل الساعة الحالية عندك، مثال: *23:15*\n\nسأحدد المنطقة الزمنية تلقائياً.",
    "notif_timezone_updated": "✅ تم تحديث المنطقة الزمنية: UTC{sign}{offset}\n\n",
    "notif_time_updated": "✅ تم تحديث وقت التذكير ({meal}): *{time}*\n\n",
    "notif_time_bad": "❌ لم أفهم الوقت. أدخله بصيغة *HH:MM*، مثال: *08:30*",
    "timezone_bad": "لم أفهم 🤔 أدخل الوقت بصيغة *HH:MM*، مثال: *23:15*",
    "meal_name_breakfast": "الإفطار",
    "meal_name_lunch": "الغداء",
    "meal_name_dinner": "العشاء",
    "notif_tz_saved": "🔔 *تم تفعيل التذكيرات!*\n\n🌍 المنطقة الزمنية: {tz}\n☕ الإفطار — 9:00\n🍲 الغداء — 13:00\n🍽️ العشاء — 19:00\n\nللضبط: /notify",
    "onb_tz_saved": "🔔 *تم تفعيل التذكيرات!*\n\n🌍 المنطقة الزمنية: {tz}\n☕ الإفطار — 9:00\n🍲 الغداء — 13:00\n🍽️ العشاء — 19:00\n\nللضبط: /notify",
    "onb_tz_skip": "حسناً، بدون تذكيرات 👌\nيمكن التفعيل في أي وقت: /notify",
    "notif_snooze_done": "✅ تم إيقاف تذكير {meal}.\nإعادة التفعيل: /notify",

    # ── Timezone city names ───────────────────────────────────────
    "tz_kyiv": "🇺🇦 كييف",
    "tz_moscow": "🇷🇺 موسكو",
    "tz_baku": "🇦🇿 باكو",
    "tz_almaty": "🇰🇿 ألماتي",
    "tz_tashkent": "🇺🇿 طشقند",
    "tz_novosibirsk": "نوفوسيبيرسك",
    "tz_irkutsk": "إيركوتسك",
    "tz_vladivostok": "فلاديفوستوك",
    "tz_skip": "❌ تخطي",

    # ── Trial / Paywall ───────────────────────────────────────────
    "trial_exhausted": "❌ *انتهت التحليلات المجانية* (15 من 15)\n\nاشترك لمواصلة حساب السعرات 👇",
    "trial_last_1": "⚠️ تبقى *تحليل مجاني واحد* من {limit} → /subscribe",
    "trial_last_few": "⚠️ تبقى *{left} تحليلات مجانية* من {limit} → /subscribe",
    "trial_some_left": "🎁 {left} تحليلات مجانية متبقية من {limit} → /subscribe",
    "trial_many_left": "🎁 التحليلات المجانية: {left} من {limit}",
    "btn_subscribe": "💳 اشترك",
    "subscribe_remaining": "🎁 التحليلات المجانية المتبقية: *{left} من {limit}*\n\n",
    "subscribe_exhausted": "❌ انتهت التحليلات المجانية\n\n",
    "subscribe_header": "💳 *اشتراك Meal Scan*\n\nاختر خطة:",
    "subscribe_header_full": "💳 *اشتراك Meal Scan*\n\nحساب غير محدود للسعرات من الصور والنص\n\nاختر خطة:",
    "subscribe_active": "✅ *الاشتراك نشط حتى {expires}*\n\nيمكنك التجديد مسبقاً — ستُضاف المدة إلى الفترة الحالية:",
    "payment_success": "🎉 *تم تفعيل الاشتراك لـ {label}!*\n\nتتبع السعرات بلا حدود 🍽️\nأرسل صورة أو اكتب وجبتك ↓",
    "sub_1m_label": "شهر واحد",
    "sub_3m_label": "3 أشهر",
    "sub_invoice_title_1m": "اشتراك Meal Scan — شهر واحد",
    "sub_invoice_title_3m": "اشتراك Meal Scan — 3 أشهر",
    "sub_invoice_desc": "حساب غير محدود للسعرات والمغذيات من الصور والنص",
    "sub_invoice_error": "❌ خطأ في إنشاء الفاتورة: {e}",

    # ── Delete command ────────────────────────────────────────────
    "delete_no_num": "❌ حدد رقم الوجبة.\nمثال: `/delete 2`\n\nقائمة اليوم: /today",
    "delete_bad_num": "❌ يجب أن يكون الرقم صحيحاً. مثلاً: `/delete 2`",
    "delete_no_meals": "📭 لا توجد وجبات مسجلة اليوم.",
    "delete_out_of_range": "❌ لا توجد وجبة #{num}. سجلات اليوم: {total}.\n\nعرض القائمة: /today",
    "delete_done": "🗑️ تم الحذف: *{food}* ({cal} سعرة)\n\n📊 المتبقي اليوم: *{total_cal} سعرة* ({n} وجبات)",

    # ── Edit command ──────────────────────────────────────────────
    "edit_no_args": "✏️ الصيغة: `/edit رقم وصف جديد`\nمثال: `/edit 2 دجاج مشوي 400 غرام`\n\nقائمة اليوم: /today",
    "edit_bad_num": "❌ حدد الرقم أولاً. مثلاً: `/edit 2 حساء 400 غرام`",
    "edit_no_meals": "📭 لا توجد وجبات مسجلة اليوم.",
    "edit_out_of_range": "❌ لا توجد وجبة #{num}. سجلات اليوم: {total}.",
    "edit_done": "✅ *تم تحديث الوجبة #{num}*\n\n🍽️ {food}\n🔥 {cal} سعرة | 🥩 {protein} غ | 🧈 {fat} غ | 🍞 {carbs} غ\n\n📊 اليوم: *{total_cal} سعرة* / 🥩 *{total_protein} غ بروتين*",

    # ── Delete from diary (callback) ──────────────────────────────
    "diary_deleted": "🗑️ تم حذف السجل.\n\n📊 المتناول اليوم: *{cal} سعرة* / 🥩 *{protein} غ بروتين* ({n} وجبات)\n{remaining}",
    "diary_cal_left": "🎯 المتبقي للهدف: *{cal_left} سعرة* و*{prot_left} غ بروتين*",
    "diary_cal_done": "✅ تم تحقيق هدف السعرات!",
    "diary_cal_over": "⚠️ تجاوزت الهدف بـ *{over} سعرة*",

    # ── Reminders ─────────────────────────────────────────────────
    "reminder_text": "{emoji} لا تنسَ إخباري بما تناولته في {meal}!\nالهدف: {goal_cal} سعرة. اليوم: {total_cal} سعرة\n\n📸 فقط أرسل صورة أو اكتب",
    "btn_reminder_add": "🍽️ إضافة وجبة",
    "btn_reminder_snooze": "❌ عدم التذكير بـ {meal}",

    # ── Weight tip ────────────────────────────────────────────────
    "weight_tip": "⚖️ *نصيحة: تتبع وزنك*\n\nيمكنك تسجيل وزنك كل صباح — سيُريك البوت التطور والتقدم نحو هدفك.\n\nاكتب /weight وأدخل وزنك الحالي.\nمخطط التقدم: /progress",

    # ── Admin ─────────────────────────────────────────────────────
    "resetme_done": "✅ تم حذف جميع البيانات. اكتب /start للبدء من جديد.",
    "gift_usage": "الاستخدام: /gift <user_id>",
    "gift_bad_id": "❌ يجب أن يكون user_id رقماً",
    "gift_done": "✅ المستخدم {uid} حصل على وصول دائم.",
    "error_terms": "❌ خطأ: {e}",
    "error_invoice": "❌ خطأ في إنشاء الفاتورة: {e}",
}
