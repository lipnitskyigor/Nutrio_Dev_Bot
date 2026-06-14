texts = {
    # ── Menu buttons ──────────────────────────────────────────────
    "menu_diary": "📔 डायरी",
    "menu_profile": "👤 प्रोफ़ाइल",
    "menu_help": "❓ सहायता",
    "menu_add": "🍽️ खाना जोड़ें",
    "input_placeholder": "फ़ोटो भेजें या लिखें आपने क्या खाया...",

    # ── Language switching ────────────────────────────────────────
    "choose_language": "भाषा चुनें:",
    "language_changed_ru": "✅ Язык изменён на русский 🇷🇺",
    "language_changed_en": "✅ Language changed to English 🇬🇧",
    "language_changed_uk": "✅ Мову змінено на українську 🇺🇦",
    "language_changed_be": "✅ Мова зменена на беларускую 🇧🇾",
    "language_changed_de": "✅ Sprache auf Deutsch geändert 🇩🇪",
    "language_changed_pl": "✅ Język zmieniony na polski 🇵🇱",
    "language_changed_es": "✅ Idioma cambiado a español 🇪🇸",
    "language_changed_pt": "✅ Idioma alterado para português 🇧🇷",
    "language_changed_ar": "✅ تم تغيير اللغة إلى العربية 🇸🇦",
    "language_changed_kk": "✅ Тіл қазақшаға өзгертілді 🇰🇿",
    "language_changed_hi": "✅ भाषा हिंदी में बदली गई 🇮🇳",
    "btn_lang_ru": "🇷🇺 Русский",
    "btn_lang_en": "🇬🇧 English",
    "btn_lang_uk": "🇺🇦 Українська",
    "btn_lang_be": "🇧🇾 Беларуская",
    "btn_lang_de": "🇩🇪 Deutsch",
    "btn_lang_pl": "🇵🇱 Polski",
    "btn_lang_es": "🇪🇸 Español",
    "btn_lang_pt": "🇧🇷 Português",
    "btn_lang_ar": "🇸🇦 العربية",
    "btn_lang_kk": "🇰🇿 Қазақша",
    "btn_lang_hi": "🇮🇳 हिंदी",

    # ── Claude API instruction ────────────────────────────────────
    "claude_lang": "हिंदी में",

    # ── Terms ─────────────────────────────────────────────────────
    "terms_greeting": "👋 नमस्ते, {name}!\n\nशुरू करने से पहले कृपया यह पढ़ें:\n\n⚠️ Meal Scan एक कैलोरी और पोषण ट्रैकिंग सहायक है।\nयह कोई मेडिकल ऐप नहीं है। बॉट डॉक्टर,\nडाइटिशियन या न्यूट्रिशनिस्ट की जगह नहीं लेता।\n\n📄 उपयोग की शर्तें: mealscan.org/terms.html\n\nनीचे दिए बटन पर टैप करके आप उपयोग की शर्तों से सहमत होते हैं।",
    "btn_accept_terms": "✅ शर्तें स्वीकार करें",

    # ── Start / Welcome ───────────────────────────────────────────
    "welcome_back": "वापस स्वागत है, {name}! 👋\n\n📸 अपने खाने की फ़ोटो भेजें या लिखें आपने क्या खाया — मैं गणना करूँगा।",
    "welcome_new": "मैं आपके पोषण को ट्रैक करने में मदद करता हूँ — फ़ोटो या टेक्स्ट से कैलोरी और मैक्रोज़ गिनता हूँ।\n\n📸 *किसी भी डिश की फ़ोटो भेजें*\n✏️ या लिखें आपने क्या खाया\n\nअभी आज़माएं ↓\n\n———\nℹ️ Meal Scan एक पोषण ट्रैकिंग सहायक है, मेडिकल ऐप नहीं। यदि आपको कोई स्वास्थ्य समस्या है या आहार बदलने वाले हैं, तो पहले डॉक्टर या डाइटिशियन से सलाह लें।",
    "default_friend": "दोस्त",

    # ── Help ──────────────────────────────────────────────────────
    "help_text": (
        "🤖 *बॉट का उपयोग कैसे करें:*\n\n"
        "📸 खाने की फ़ोटो भेजें — मैं कैलोरी और मैक्रोज़ गिनूँगा\n"
        "✏️ लिखें आपने क्या खाया — मैं वो भी गिनूँगा\n"
        "उदाहरण: _«300 ग्राम चावल के साथ चिकन»_\n\n"
        "📊 *कैलोरी और पोषण:*\n"
        "/today — आज का कुल (कैलोरी, प्रोटीन, वसा, कार्ब्स)\n"
        "/history — पिछले 7 दिनों का इतिहास\n"
        "/goal 2000 150 — दैनिक कैलोरी और प्रोटीन लक्ष्य सेट करें\n"
        "/goal — अपना वर्तमान लक्ष्य देखें\n"
        "/reset — आज की एंट्री साफ़ करें\n\n"
        "⚖️ *वज़न और प्रगति:*\n"
        "/weight 80.5 — अपना वज़न दर्ज करें (हर दिन करें)\n"
        "/weight — अंतिम दर्ज वज़न देखें\n"
        "/target 75 — लक्ष्य वज़न सेट करें\n"
        "/target — लक्ष्य वज़न और शेष देखें\n"
        "/progress — 7 दिनों की वज़न गतिशीलता 🟢🔴 बदलाव के साथ\n\n"
        "💡 टिप: फ़ोटो में खाना जितना साफ़ होगा, परिणाम उतना सटीक होगा!\n\n"
        "🔔 *रिमाइंडर:*\n"
        "/notify — भोजन रिमाइंडर सेट करें\n\n"
        "💬 *सहायता:*\n"
        "/support — सहायता से संपर्क करें"
    ),

    # ── Support ───────────────────────────────────────────────────
    "support_text": "💬 *Meal Scan सहायता*\n\nयदि आपका कोई सवाल या समस्या है — हमें लिखें:\n\n👉 @Meal\_Scan\_Support",

    # ── Today ─────────────────────────────────────────────────────
    "today_empty": "📭 आज के लिए कोई खाने की एंट्री नहीं है।\nगिनती शुरू करने के लिए डिश की फ़ोटो भेजें!",
    "today_header": "📊 *आज का कुल — {name}*\n",
    "today_meal_line": "{i}. {food} — {cal} kcal ({time})",
    "today_total_cal": "\n🔥 *कुल: {cal} kcal*",
    "today_macros": "🥩 प्रोटीन: {protein} ग्रा  🧈 वसा: {fat} ग्रा  🍞 कार्ब्स: {carbs} ग्रा",
    "today_cal_left": "\n🎯 लक्ष्य तक शेष: *{cal_left} kcal* और *{prot_left} ग्रा प्रोटीन*",
    "today_cal_done": "\n✅ *कैलोरी लक्ष्य पूरा हो गया!*",
    "today_cal_over": "\n⚠️ लक्ष्य से *{over} kcal* अधिक",

    # ── History ───────────────────────────────────────────────────
    "history_empty": "📭 पिछले 7 दिनों का कोई डेटा नहीं।\nशुरू करने के लिए खाने की फ़ोटो भेजें!",
    "history_header": "📅 *7-दिन का इतिहास — {name}*\n",
    "history_entry": "📆 {day}: *{cal} kcal* ({n} भोजन{suffix})",
    "history_meals_suffix_1": "",
    "history_meals_suffix_other": "",

    # ── Reset ─────────────────────────────────────────────────────
    "reset_done": "🗑️ आज का डेटा साफ़ कर दिया गया!",

    # ── Goal ──────────────────────────────────────────────────────
    "goal_current": "🎯 *आपका दैनिक लक्ष्य:*\n🔥 कैलोरी: {cal} kcal\n🥩 प्रोटीन: {protein} ग्रा\n\nबदलने के लिए: `/goal 2000 150`",
    "goal_not_set": "🎯 लक्ष्य सेट नहीं है।\n\nइस तरह सेट करें: `/goal कैलोरी प्रोटीन`\nउदाहरण: `/goal 2000 150`",
    "goal_saved": "✅ *लक्ष्य सेट हो गया!*\n🔥 कैलोरी: {cal} kcal/दिन\n🥩 प्रोटीन: {protein} ग्रा/दिन",
    "goal_bad_format": "❌ गलत फ़ॉर्मेट। उपयोग करें: `/goal 2000 150`",

    # ── Weight ────────────────────────────────────────────────────
    "weight_last": "⚖️ *अंतिम वज़न:* {weight} kg ({day})\n\nनया दर्ज करने के लिए: `/weight 80.5`",
    "weight_not_set": "⚖️ अभी तक कोई वज़न दर्ज नहीं हुआ।\n\nइस तरह दर्ज करें: `/weight 80.5`",
    "weight_saved": "⚖️ *वज़न दर्ज हो गया:* {weight} kg\n",
    "weight_to_goal": "\n🎯 लक्ष्य तक ({target} kg): *{diff} kg* शेष\n",
    "weight_almost": "💪 लगभग पहुँच गए! आप अपने लक्ष्य के बहुत करीब हैं!",
    "weight_great_progress": "🔥 बेहतरीन प्रगति, इसी तरह जारी रखें!",
    "weight_good_start": "💪 अच्छी शुरुआत! हर दिन आप अपने लक्ष्य के करीब पहुँच रहे हैं।",
    "weight_goal_reached": "\n🏆 लक्ष्य पूरा हो गया! आप लक्ष्य वज़न से {diff} kg नीचे हैं!",
    "weight_on_goal": "\n🎯 आप बिल्कुल अपने लक्ष्य वज़न पर हैं! शानदार!",
    "weight_set_target_hint": "\n💡 `/target 75` से अपना लक्ष्य वज़न सेट करें",
    "weight_bad_format": "❌ गलत फ़ॉर्मेट। उपयोग करें: `/weight 80.5`",

    # ── Progress ──────────────────────────────────────────────────
    "progress_empty": "⚖️ वज़न का कोई डेटा नहीं।\n\nहर दिन `/weight 80.5` से अपना वज़न दर्ज करें — मैं गतिशीलता दिखाऊँगा!",
    "progress_header": "📈 *वज़न की गतिशीलता:*\n",
    "progress_entry_first": "📅 {day}: *{w} kg*",
    "progress_entry_down": "📅 {day}: *{w} kg* (🟢 {diff} kg)",
    "progress_entry_up": "📅 {day}: *{w} kg* (🔴 +{diff} kg)",
    "progress_entry_same": "📅 {day}: *{w} kg* (➡️ कोई बदलाव नहीं)",
    "progress_total_down": "\n📉 इस अवधि में: *{diff} kg* — शानदार नतीजा!",
    "progress_total_up": "\n📈 इस अवधि में: *+{diff} kg*",
    "progress_total_stable": "\n➡️ इस अवधि में: वज़न स्थिर है",
    "progress_to_goal": "🎯 लक्ष्य तक ({target} kg): *{diff} kg* शेष",
    "progress_goal_reached": "🏆 लक्ष्य {target} kg — *पूरा हो गया!*",

    # ── Target ────────────────────────────────────────────────────
    "target_current": "🎯 *लक्ष्य वज़न:* {target} kg\n",
    "target_remaining": "📍 वर्तमान वज़न: {current} kg — *{diff} kg* शेष",
    "target_reached": "🏆 वर्तमान वज़न: {current} kg — लक्ष्य पूरा हो गया!",
    "target_change_hint": "\n\nबदलें: `/target 70`",
    "target_not_set": "🎯 लक्ष्य वज़न सेट नहीं है।\n\nइस तरह सेट करें: `/target 75`",
    "target_bad_format": "❌ गलत फ़ॉर्मेट। उपयोग करें: `/target 75`",
    "target_need_profile": "📋 लक्ष्य की सुरक्षा जाँचने के लिए प्रोफ़ाइल चाहिए (ऊँचाई, उम्र, लिंग, गतिविधि)।\n\nअपनी प्रोफ़ाइल सेट करें — और मैं बताऊँगा कि आपका लक्ष्य कितना सुरक्षित है।",
    "btn_setup_profile": "👉 प्रोफ़ाइल सेट करें",
    "target_safe_set": "✅ *लक्ष्य सेट हो गया: {target} kg*\n\n📊 अनुशंसित कैलोरी: *{cal} kcal/दिन*\n",
    "target_min_cal_warn": "⚠️ _न्यूनतम सुरक्षित कैलोरी: {min_cal} kcal/दिन_\n",
    "target_weeks": "⏱ अनुमानित समय: *{weeks} सप्ताह*",
    "target_warn_low_bmi": "⚠️ लक्ष्य वज़न *{target} kg* से BMI *{bmi}* होगा — सामान्य से कम।\nआपकी ऊँचाई के लिए न्यूनतम अनुशंसित वज़न: *{min_weight} kg*।\n\nशुरू करने से पहले किसी विशेषज्ञ से सलाह लें।",
    "target_danger_bmi": "🚨 लक्ष्य वज़न *{target} kg* — BMI *{bmi}*, खतरनाक रूप से कम।\n{height} cm ऊँचाई के लिए अनुशंसित न्यूनतम: *{min_weight} kg*।\n\nहम दृढ़ता से डॉक्टर से परामर्श करने की सलाह देते हैं।",
    "target_critical_bmi": "❌ लक्ष्य *{target} kg* सेट नहीं किया जा सकता।\nBMI *{bmi}* अत्यंत कम और जीवन के लिए खतरनाक है।\n\nआपकी ऊँचाई के लिए न्यूनतम सुरक्षित वज़न: *{min_weight} kg*।\nकृपया किसी डॉक्टर या डाइटिशियन से मिलें।",
    "btn_target_confirm": "✅ फिर भी सेट करें",
    "btn_target_confirm_warn": "⚠️ फिर भी सेट करें (अनुशंसित नहीं)",
    "btn_target_change": "✏️ लक्ष्य बदलें",
    "target_confirmed_msg": "✅ लक्ष्य वज़न *{target} kg* सेट हो गया।\n\n⚠️ विशेषज्ञ से परामर्श की सलाह याद रखें।",
    "target_change_prompt": "नया लक्ष्य वज़न दर्ज करें: `/target 70`",

    # ── Meal analysis ─────────────────────────────────────────────
    "analyzing_photo": "🔍 फ़ोटो का विश्लेषण हो रहा है...",
    "counting_calories": "🔍 कैलोरी गिनी जा रही है...",
    "recalculating": "🔍 पुनर्गणना हो रही है...",
    "analysis_error_parse": "😔 जवाब समझ नहीं आया। दोबारा कोशिश करें या साफ़ फ़ोटो भेजें।",
    "analysis_error_photo": "😔 फ़ोटो का विश्लेषण करते समय त्रुटि हुई। दोबारा कोशिश करें!",
    "analysis_error_text": "😔 समझ नहीं आया। अधिक विस्तार से वर्णन करने की कोशिश करें!",
    "analysis_error_generic": "😔 कोई त्रुटि हुई। दोबारा कोशिश करें!",
    "correction_error": "😔 पुनर्गणना नहीं हो सकी। अधिक विस्तार से वर्णन करें!",
    "corrected_prefix": "✅ *सुधारा गया!*\n\n",

    # ── Meal summary ──────────────────────────────────────────────
    "meal_summary_header": "🍽️ *{food}*\n\n🔥 *{cal} kcal*\n🥩 प्रोटीन: *{protein} ग्रा*\n🧈 वसा: {fat} ग्रा\n🍞 कार्ब्स: {carbs} ग्रा\n\n💬 _{comment}_\n\n📊 *आज का कुल:*\n🔥 {total_cal} kcal (~{day_pct}% दैनिक आवश्यकता)  🥩 प्रोटीन: *{total_protein} ग्रा*",
    "meal_remaining_profile": "\n\n🎯 लक्ष्य तक शेष: *~{cal_left} kcal* और *~{prot_left} ग्रा प्रोटीन*\n_(लक्ष्य: {cal_low}–{cal_high} kcal/दिन)_",
    "meal_on_target_profile": "\n\n✅ लक्ष्य के अंदर! ({cal_low}–{cal_high} kcal/दिन)",
    "meal_over_target_profile": "\n\n⚠️ लक्ष्य से ~*{over} kcal* अधिक",
    "meal_remaining_default": "\n\n🎯 औसत आवश्यकता तक शेष: *~{cal_left} kcal* और *~{prot_left} ग्रा प्रोटीन*",
    "meal_on_target_default": "\n\n✅ औसत आवश्यकता पूरी हो गई!",
    "meal_over_target_default": "\n\n⚠️ औसत आवश्यकता से *{over} kcal* अधिक",

    # ── Meal keyboard ─────────────────────────────────────────────
    "btn_meal_confirm": "✅ सही है",
    "btn_meal_edit": "✏️ संपादित करें",
    "btn_meal_delete": "🗑️ हटाएं",
    "edit_prompt": "✏️ सुधार टाइप करें — मैं पुनर्गणना करूँगा:",
    "quick_add_prompt": "📸 अपने खाने की फ़ोटो भेजें या लिखें आपने क्या खाया — मैं गणना करूँगा!",
    "menu_add_prompt": "📸 अपने खाने की फ़ोटो भेजें या लिखें आपने क्या खाया — मैं गणना करूँगा!",

    # ── Short input hint ──────────────────────────────────────────
    "short_input_hint": "📸 खाने की फ़ोटो भेजें या लिखें आपने क्या खाया — मैं कैलोरी गिनूँगा!\n\nउदाहरण: *«सूप का एक कटोरा और रोटी»* या *«2 अंडे, दूध वाली चाय»*",

    # ── Profile ───────────────────────────────────────────────────
    "profile_not_set": "📋 *प्रोफ़ाइल सेट नहीं है*\n\nअपनी प्रोफ़ाइल भरें — और मैं आपकी कैलोरी आवश्यकता और प्रगति अधिक सटीक रूप से गिनूँगा।",
    "btn_edit_profile": "✏️ प्रोफ़ाइल संपादित करें",
    "profile_goal_lose": "वज़न घटाना 🥦",
    "profile_goal_maintain": "वज़न बनाए रखना ⚖️",
    "profile_goal_gain": "मांसपेशी बनाना 💪",
    "profile_activity_sedentary": "निष्क्रिय 🪑",
    "profile_activity_light": "हल्की गतिविधि 🚶",
    "profile_activity_moderate": "मध्यम 🏃",
    "profile_activity_active": "सक्रिय 💪",
    "profile_view": "👤 *आपकी प्रोफ़ाइल*\n\n🎯 लक्ष्य: {goal}\n⚡ गतिविधि: {activity}\n📏 ऊँचाई: {height} cm\n⚖️ वज़न: {weight} kg\n",
    "profile_last_weight": "📅 अंतिम वज़न: *{w} kg* ({day})\n",
    "profile_weight_goal_reached": "🏁 वज़न लक्ष्य: *{target} kg* — पूरा हो गया! 🎉\n",
    "profile_weight_to_goal": "🏁 लक्ष्य तक ({target} kg): *{diff} kg*\n",
    "profile_norm": "\n🔥 आवश्यकता: *{low}–{high} kcal/दिन*\n🥩 प्रोटीन: *{protein} ग्रा/दिन*\n📊 आज खाया: *{today_cal} kcal*",

    # ── Onboarding / Profile flow ─────────────────────────────────
    "profile_prompt_title": "📊 *आपके और आपके लक्ष्य के अनुसार कैलोरी सेट करते हैं*\n\n4 सवालों के जवाब दें — गणना अधिक सटीक होगी\n30 सेकंड से कम समय लगेगा",
    "btn_profile_yes": "👉 चलिए शुरू करते हैं",
    "btn_profile_skip": "छोड़ें",
    "ask_goal": "आपका लक्ष्य क्या है?",
    "ask_sex": "आपका लिंग?",
    "ask_activity": "आपकी जीवनशैली कैसी है?",
    "ask_age": "आपकी उम्र कितनी है?\n\nनंबर लिखें, उदाहरण: *28*",
    "ask_height": "आपकी ऊँचाई?\n\nसेंटीमीटर में लिखें, उदाहरण: *178*",
    "ask_weight": "आपका वर्तमान वज़न?\n\nकिलोग्राम में लिखें, उदाहरण: *75*",
    "ask_target_weight": "क्या आपका कोई लक्ष्य वज़न है?",
    "btn_set_target_yes": "✏️ हाँ, मैं सेट करूँगा",
    "btn_skip": "छोड़ें",
    "ask_target_weight_enter": "अपना लक्ष्य वज़न kg में लिखें, उदाहरण: *70*",
    "age_bad": "उम्र नंबर में लिखें, उदाहरण: *28*",
    "height_bad": "ऊँचाई नंबर में cm में लिखें, उदाहरण: *178*",
    "weight_bad": "वज़न नंबर में kg में लिखें, उदाहरण: *75*",
    "target_weight_bad": "वज़न नंबर में kg में लिखें, उदाहरण: *70*",
    "target_weight_critical_onb": "❌ लक्ष्य वज़न *{target} kg* — BMI *{bmi}*, अत्यंत खतरनाक।\n{height} cm ऊँचाई के लिए न्यूनतम सुरक्षित वज़न: *{min_weight} kg*।\n\nकोई अलग लक्ष्य वज़न लिखें:",
    "btn_target_confirm_onb": "✅ फिर भी सेट करें",
    "btn_target_change_onb": "✏️ लक्ष्य बदलें",
    "target_change_onb_prompt": "kg में कोई अलग लक्ष्य वज़न लिखें, उदाहरण: *70*",

    # goal labels (used in _finish_profile)
    "goal_label_lose": "वज़न घटाना",
    "goal_label_maintain": "वज़न बनाए रखना",
    "goal_label_gain": "मांसपेशी बनाना",

    # ── Profile goal buttons ──────────────────────────────────────
    "btn_goal_lose": "📉 वज़न घटाना",
    "btn_goal_maintain": "⚖️ वज़न बनाए रखना",
    "btn_goal_gain": "📈 मांसपेशी बनाना",
    "btn_sex_male": "👨 पुरुष",
    "btn_sex_female": "👩 महिला",
    "btn_activity_sedentary": "🪑 निष्क्रिय (ऑफिस, खेल नहीं)",
    "btn_activity_light": "🚶 हल्की गतिविधि (सप्ताह में 1–2 बार)",
    "btn_activity_moderate": "🏃 मध्यम (सप्ताह में 3–5 बार)",
    "btn_activity_active": "💪 सक्रिय (हर दिन)",

    # ── Finish profile ────────────────────────────────────────────
    "profile_done": "✅ *तैयार है!*\n\n🎯 लक्ष्य: *{goal}*\n🔥 कैलोरी: *{low}–{high} kcal/दिन*\n🥩 प्रोटीन: *~{protein} ग्रा/दिन*{target_line}\n\nहर भोजन के बाद मैं दिखाऊँगा कि लक्ष्य तक कितनी kcal बची है 🎯",
    "profile_target_line_remaining": "\n⚖️ लक्ष्य वज़न: *{target} kg* (~{diff} kg शेष)",
    "profile_target_line_reached": "\n⚖️ लक्ष्य वज़न: *{target} kg* — पहले से ही पूरा! 🏆",
    "ask_timezone": "🔔 *पोषण ट्रैकिंग के लिए रिमाइंडर सेट करते हैं!*\n\nमैं आपको खाना दर्ज करने की याद दिलाऊँगा — बस फ़ोटो भेजें या लिखें।\n\nअभी आपके यहाँ क्या समय है, लिखें, उदाहरण: *23:15*",

    # ── Notifications ─────────────────────────────────────────────
    "notify_header": "⏰ *रिमाइंडर सेटिंग्स*\n\n🌍 समय क्षेत्र: {tz} (अभी {time})\n\n☕ नाश्ता — {b_time} ({b})\n🍲 दोपहर का खाना — {l_time} ({l})\n🍽️ रात का खाना — {d_time} ({d})\n\n⚠️ हम कम से कम 1 रिमाइंडर चालू रखने की सलाह देते हैं",
    "btn_notif_all_on": "✅ सभी चालू करें",
    "btn_notif_all_off": "❌ सभी बंद करें",
    "btn_notif_change_tz": "🌍 समय क्षेत्र बदलें",
    "notif_enabled": "✅",
    "notif_disabled": "❌",
    "notif_breakfast": "☕ नाश्ता",
    "notif_lunch": "🍲 दोपहर का खाना",
    "notif_dinner": "🍽️ रात का खाना",
    "notif_time_prompt": "⏰ *{meal}* के लिए नया रिमाइंडर समय लिखें\n\nफ़ॉर्मेट: *HH:MM*, उदाहरण: *08:30*",
    "notif_timezone_prompt": "🕐 अभी आपके यहाँ क्या समय है, लिखें, उदाहरण: *23:15*\n\nमैं आपका समय क्षेत्र स्वचालित रूप से निर्धारित करूँगा।",
    "notif_timezone_updated": "✅ समय क्षेत्र अपडेट हो गया: UTC{sign}{offset}\n\n",
    "notif_time_updated": "✅ रिमाइंडर समय ({meal}) अपडेट हो गया: *{time}*\n\n",
    "notif_time_bad": "❌ समय समझ नहीं आया। *HH:MM* फ़ॉर्मेट में लिखें, उदाहरण: *08:30*",
    "timezone_bad": "समझ नहीं आया 🤔 समय *HH:MM* फ़ॉर्मेट में लिखें, उदाहरण: *23:15*",
    "meal_name_breakfast": "नाश्ता",
    "meal_name_lunch": "दोपहर का खाना",
    "meal_name_dinner": "रात का खाना",
    "notif_tz_saved": "🔔 *रिमाइंडर चालू हो गए!*\n\n🌍 समय क्षेत्र: {tz}\n☕ नाश्ता — 9:00\n🍲 दोपहर का खाना — 13:00\n🍽️ रात का खाना — 19:00\n\nसेटिंग: /notify",
    "onb_tz_saved": "🔔 *रिमाइंडर चालू हो गए!*\n\n🌍 समय क्षेत्र: {tz}\n☕ नाश्ता — 9:00\n🍲 दोपहर का खाना — 13:00\n🍽️ रात का खाना — 19:00\n\nसेटिंग: /notify",
    "onb_tz_skip": "ठीक है, रिमाइंडर के बिना 👌\nकभी भी चालू करें: /notify",
    "notif_snooze_done": "✅ {meal} का रिमाइंडर बंद कर दिया।\nदोबारा चालू करें: /notify",

    # ── Timezone city names ───────────────────────────────────────
    "tz_kyiv": "🇺🇦 कीव",
    "tz_moscow": "🇷🇺 मॉस्को",
    "tz_baku": "🇦🇿 बाकू",
    "tz_almaty": "🇰🇿 अल्माटी",
    "tz_tashkent": "🇺🇿 ताशकंद",
    "tz_novosibirsk": "नोवोसिबिर्स्क",
    "tz_irkutsk": "इर्कुत्स्क",
    "tz_vladivostok": "व्लादिवोस्तोक",
    "tz_skip": "❌ छोड़ें",

    # ── Trial / Paywall ───────────────────────────────────────────
    "trial_exhausted": "❌ *मुफ़्त विश्लेषण समाप्त हो गए* (15 में से 15)\n\nकैलोरी गिनना जारी रखने के लिए सदस्यता लें 👇",
    "trial_last_1": "⚠️ {limit} में से *1 मुफ़्त विश्लेषण* बचा है → /subscribe",
    "trial_last_few": "⚠️ {limit} में से *{left} मुफ़्त विश्लेषण* बचे हैं → /subscribe",
    "trial_some_left": "🎁 {limit} में से {left} मुफ़्त विश्लेषण बचे हैं → /subscribe",
    "trial_many_left": "🎁 मुफ़्त विश्लेषण: {limit} में से {left}",
    "btn_subscribe": "💳 सदस्यता लें",
    "subscribe_remaining": "🎁 मुफ़्त विश्लेषण शेष: *{limit} में से {left}*\n\n",
    "subscribe_exhausted": "❌ मुफ़्त विश्लेषण समाप्त हो गए\n\n",
    "subscribe_header": "💳 *Meal Scan सदस्यता*\n\nप्लान चुनें:",
    "subscribe_header_full": "💳 *Meal Scan सदस्यता*\n\nफ़ोटो और टेक्स्ट से असीमित कैलोरी गणना\n\nप्लान चुनें:",
    "subscribe_active": "✅ *सदस्यता {expires} तक सक्रिय है*\n\nआप पहले से नवीनीकरण कर सकते हैं — समय वर्तमान अवधि में जुड़ जाएगा:",
    "payment_success": "🎉 *{label} के लिए सदस्यता सक्रिय हो गई!*\n\nबिना सीमा के कैलोरी गिनें 🍽️\nफ़ोटो भेजें या लिखें आपने क्या खाया ↓",
    "sub_1m_label": "1 महीना",
    "sub_3m_label": "3 महीने",
    "sub_invoice_title_1m": "Meal Scan सदस्यता — 1 महीना",
    "sub_invoice_title_3m": "Meal Scan सदस्यता — 3 महीने",
    "sub_invoice_desc": "फ़ोटो और टेक्स्ट से असीमित कैलोरी और मैक्रो गणना",
    "sub_invoice_error": "❌ इनवॉइस बनाने में त्रुटि: {e}",

    # ── Delete command ────────────────────────────────────────────
    "delete_no_num": "❌ भोजन नंबर बताएं।\nउदाहरण: `/delete 2`\n\nआज की सूची: /today",
    "delete_bad_num": "❌ नंबर पूर्णांक होना चाहिए। उदाहरण: `/delete 2`",
    "delete_no_meals": "📭 आज के लिए कोई खाने की एंट्री नहीं है।",
    "delete_out_of_range": "❌ #{num} नंबर नहीं है। आज की एंट्री: {total}।\n\nसूची देखें: /today",
    "delete_done": "🗑️ हटाया गया: *{food}* ({cal} kcal)\n\n📊 आज शेष: *{total_cal} kcal* ({n} भोजन)",

    # ── Edit command ──────────────────────────────────────────────
    "edit_no_args": "✏️ फ़ॉर्मेट: `/edit नंबर नया विवरण`\nउदाहरण: `/edit 2 बीफ़ बोर्श 400g`\n\nआज की सूची: /today",
    "edit_bad_num": "❌ पहले नंबर बताएं। उदाहरण: `/edit 2 बोर्श 400g`",
    "edit_no_meals": "📭 आज के लिए कोई खाने की एंट्री नहीं है।",
    "edit_out_of_range": "❌ #{num} नंबर नहीं है। आज की एंट्री: {total}।",
    "edit_done": "✅ *भोजन #{num} अपडेट हो गया*\n\n🍽️ {food}\n🔥 {cal} kcal | 🥩 {protein} ग्रा | 🧈 {fat} ग्रा | 🍞 {carbs} ग्रा\n\n📊 आज: *{total_cal} kcal* / 🥩 *{total_protein} ग्रा प्रोटीन*",

    # ── Delete from diary (callback) ──────────────────────────────
    "diary_deleted": "🗑️ एंट्री हटा दी गई।\n\n📊 आज खाया: *{cal} kcal* / 🥩 *{protein} ग्रा प्रोटीन* ({n} भोजन)\n{remaining}",
    "diary_cal_left": "🎯 लक्ष्य तक शेष: *{cal_left} kcal* और *{prot_left} ग्रा प्रोटीन*",
    "diary_cal_done": "✅ कैलोरी लक्ष्य पूरा हो गया!",
    "diary_cal_over": "⚠️ लक्ष्य से *{over} kcal* अधिक",

    # ── Reminders ─────────────────────────────────────────────────
    "reminder_text": "{emoji} मत भूलें {meal} के बारे में बताना!\nलक्ष्य: {goal_cal} kcal. आज: {total_cal} kcal\n\n📸 बस फ़ोटो भेजें या टाइप करें",
    "btn_reminder_add": "🍽️ खाना जोड़ें",
    "btn_reminder_snooze": "❌ {meal} की याद मत दिलाओ",

    "winback": "हमें आपकी याद आई 👋\n\nआपके 15 मुफ़्त स्कैन समाप्त हो गए — लेकिन स्वस्थ खान-पान की आपकी यात्रा अभी शुरू हुई है।\n\nसब्सक्राइब करें और हर भोजन को ट्रैक करते रहें ताकि कुछ न छूटे 🥗",
    "evening_summary": "🌙 दिन का सारांश\n\nआज: *{total_cal} कैलोरी* {goal_cal} में से ({day_pct}%)\nप्रोटीन: *{total_protein} ग्राम*",
    "evening_no_logs": "📸 आपका दिन कैसा रहा?\n\nआज अभी तक कुछ भी दर्ज नहीं हुआ — रात के खाने को मत भूलें।\nबस एक फ़ोटो भेजें, 5 सेकंड लगेंगे।",

    # ── Weight tip ────────────────────────────────────────────────
    "weight_tip": "⚖️ *टिप: अपना वज़न ट्रैक करें*\n\nआप हर सुबह अपना वज़न दर्ज कर सकते हैं — बॉट आपको गतिशीलता और लक्ष्य की ओर प्रगति दिखाएगा।\n\nबस /weight टाइप करें और अपना वर्तमान वज़न दर्ज करें।\nप्रगति चार्ट: /progress",

    # ── Admin ─────────────────────────────────────────────────────
    "resetme_done": "✅ सभी डेटा साफ़ कर दिया गया। दोबारा शुरू करने के लिए /start टाइप करें।",
    "gift_usage": "उपयोग: /gift <user_id>",
    "gift_bad_id": "❌ user_id एक नंबर होना चाहिए",
    "gift_done": "✅ यूज़र {uid} को स्थायी एक्सेस दी गई।",
    "error_terms": "❌ त्रुटि: {e}",
    "error_invoice": "❌ इनवॉइस बनाने में त्रुटि: {e}",
}
