texts = {
    # ── Menu buttons ──────────────────────────────────────────────
    "menu_diary":   "📔 Kundalik",
    "menu_profile": "👤 Profil",
    "menu_help":    "❓ Yordam",
    "menu_add":     "🍽️ Taom qo'shish",
    "input_placeholder": "Rasm yuboring yoki nima yeganingizni yozing...",

    # ── Language switching ────────────────────────────────────────
    "choose_language": "Tilni tanlang / Choose language:",
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
    "language_changed_az": "✅ Dil Azərbaycan dilinə dəyişdirildi 🇦🇿",
    "language_changed_hy": "✅ Language changed to Armenian 🇦🇲",
    "language_changed_uz": "✅ Til o'zbek tiliga o'zgartirildi 🇺🇿",
    "language_changed_ka": "✅ ენა შეიცვალა ქართულზე 🇬🇪",
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
    "btn_lang_az": "🇦🇿 Azərbaycan",
    "btn_lang_hy": "🇦🇲 Հայerեն",
    "btn_lang_uz": "🇺🇿 O'zbek",
    "btn_lang_ka": "🇬🇪 ქართული",

    # ── Claude API instruction ────────────────────────────────────
    "claude_lang": "o'zbek tilida",

    # ── Terms ─────────────────────────────────────────────────────
    "terms_greeting": "👋 Salom, {name}!\n\nBoshlashdan oldin iltimos buni o'qing:\n\n⚠️ Meal Scan — kaloriya va ovqatlanishni kuzatish yordamchisi.\nBu tibbiy ilova emas. Bot shifokor,\ndiyetolog yoki nutritsiologni almashtirmaydi.\n\n📄 Foydalanish shartlari: mealscan.org/terms.html\n\nQuyidagi tugmani bosish orqali foydalanish shartlarini qabul qilasiz.",
    "btn_accept_terms": "✅ Shartlarni qabul qilaman",

    # ── Start / Welcome ───────────────────────────────────────────
    "welcome_back": "Xush kelibsiz, {name}! 👋\n\n📸 Taomingiz rasmini yuboring yoki nima yeganingizni yozing — hisoblayman.",
    "welcome_new": "Men ovqatlanishingizni kuzatishga yordam beraman — rasm yoki matn bo'yicha kaloriya va BJYUni hisoblayman.\n\n📸 *Istalgan taomning rasmini yuboring*\n✏️ Yoki nima yeganingizni yozing\n\nHoziroq sinab ko'ring ↓\n\n———\nℹ️ Meal Scan — ovqatlanish kuzatish yordamchisi, tibbiy ilova emas. Sog'liq muammolaringiz bo'lsa yoki ratsioningizni o'zgartirmoqchi bo'lsangiz, avval shifokor yoki diyetolog bilan maslahatlashing.",
    "default_friend": "do'st",

    # ── Help ──────────────────────────────────────────────────────
    "help_text": (
        "🤖 *Botdan qanday foydalanish kerak:*\n\n"
        "📸 Taom rasmi yuboring — kaloriya va BJYUni hisoblayman\n"
        "✏️ Nima yeganingizni yozing — uni ham hisoblayman\n"
        "Masalan: _«tovuq bilan qorabuğdoy 300g»_\n\n"
        "📊 *Kaloriya va ovqatlanish:*\n"
        "/today — bugungi jami (kaloriya, oqsil, yog', uglevodlar)\n"
        "/history — so'nggi 7 kunning ovqatlanish tarixi\n"
        "/goal 2000 150 — kunlik kaloriya va oqsil maqsadini belgilang\n"
        "/goal — joriy maqsadingizni ko'ring\n"
        "/reset — bugungi yozuvlarni o'chiring\n\n"
        "⚖️ *Vazn va rivojlanish:*\n"
        "/weight 80.5 — vazningizni yozing (har kuni bajaring)\n"
        "/weight — so'nggi yozilgan vaznni ko'ring\n"
        "/target 75 — maqsad vaznini belgilang\n"
        "/target — maqsad vaznini va qancha qolganini ko'ring\n"
        "/progress — 7 kunlik vazn dinamikasi 🟢🔴 o'zgarishlar bilan\n\n"
        "💡 Maslahat: rasmdagi taom qanchalik aniq bo'lsa, natija shunchalik to'g'ri bo'ladi!\n\n"
        "🔔 *Eslatmalar:*\n"
        "/notify — ovqat eslatmalarini sozlang\n\n"
        "💬 *Qo'llab-quvvatlash:*\n"
        "/support — qo'llab-quvvatlash bilan bog'laning"
    ),

    # ── Support ───────────────────────────────────────────────────
    "support_text": "💬 *Meal Scan Qo'llab-quvvatlash*\n\nSavolingiz yoki muammoingiz bo'lsa — bizga yozing:\n\n👉 @Meal\_Scan\_Support",

    # ── Today ─────────────────────────────────────────────────────
    "today_empty": "📭 Bugun hali hech qanday taom yozuvi yo'q.\nHisoblashni boshlash uchun taom rasmini yuboring!",
    "today_header": "📊 *Bugungi jami — {name}*\n",
    "today_meal_line": "{i}. {food} — {cal} kkal ({time})",
    "today_total_cal": "\n🔥 *Jami: {cal} kkal*",
    "today_macros": "🥩 Oqsil: {protein} g  🧈 Yog': {fat} g  🍞 Uglevodlar: {carbs} g",
    "today_cal_left": "\n🎯 Maqsadga qolgan: *{cal_left} kkal* va *{prot_left} g oqsil*",
    "today_cal_done": "\n✅ *Kaloriya maqsadiga erishdingiz!*",
    "today_cal_over": "\n⚠️ Maqsad *{over} kkal* oshib ketdi",

    # ── History ───────────────────────────────────────────────────
    "history_empty": "📭 So'nggi 7 kun uchun ma'lumot yo'q.\nBoshlash uchun taom rasmini yuboring!",
    "history_header": "📅 *7 kunlik tarix — {name}*\n",
    "history_entry": "📆 {day}: *{cal} kkal* ({n} taom{suffix})",
    "history_meals_suffix_1": "",
    "history_meals_suffix_other": "",

    # ── Reset ─────────────────────────────────────────────────────
    "reset_done": "🗑️ Bugungi ma'lumotlar o'chirildi!",

    # ── Goal ──────────────────────────────────────────────────────
    "goal_current": "🎯 *Kunlik maqsadingiz:*\n🔥 Kaloriya: {cal} kkal\n🥩 Oqsil: {protein} g\n\nO'zgartirish uchun: `/goal 2000 150`",
    "goal_not_set": "🎯 Maqsad belgilanmagan.\n\nShunday belgilang: `/goal kaloriya oqsil`\nMasalan: `/goal 2000 150`",
    "goal_saved": "✅ *Maqsad belgilandi!*\n🔥 Kaloriya: {cal} kkal/kun\n🥩 Oqsil: {protein} g/kun",
    "goal_bad_format": "❌ Noto'g'ri format. Foydalaning: `/goal 2000 150`",

    # ── Weight ────────────────────────────────────────────────────
    "weight_last": "⚖️ *So'nggi vazn:* {weight} kg ({day})\n\nYangisini yozish uchun: `/weight 80.5`",
    "weight_not_set": "⚖️ Hali hech qanday vazn yozilmagan.\n\nShunday yozing: `/weight 80.5`",
    "weight_saved": "⚖️ *Vazn yozildi:* {weight} kg\n",
    "weight_to_goal": "\n🎯 Maqsadga ({target} kg): *{diff} kg* qoldi\n",
    "weight_almost": "💪 Oz qoldi! Maqsadingizga juda yaqinsiz!",
    "weight_great_progress": "🔥 Ajoyib rivojlanish, shunday davom eting!",
    "weight_good_start": "💪 Yaxshi boshlanish! Har kun maqsadingizga bir oz yaqinlashyapsiz.",
    "weight_goal_reached": "\n🏆 Maqsadga erishdingiz! Maqsad vazningizan {diff} kg pastdasiz!",
    "weight_on_goal": "\n🎯 Aynan maqsad vazninizdasisiz! A'lo!",
    "weight_set_target_hint": "\n💡 Maqsad vazningizni `/target 75` bilan belgilang",
    "weight_bad_format": "❌ Noto'g'ri format. Foydalaning: `/weight 80.5`",

    # ── Progress ──────────────────────────────────────────────────
    "progress_empty": "⚖️ Vazn ma'lumoti yo'q.\n\nHar kuni `/weight 80.5` bilan vazningizni yozing — dinamikani ko'rsataman!",
    "progress_header": "📈 *Vazn dinamikasi:*\n",
    "progress_entry_first": "📅 {day}: *{w} kg*",
    "progress_entry_down": "📅 {day}: *{w} kg* (🟢 {diff} kg)",
    "progress_entry_up": "📅 {day}: *{w} kg* (🔴 +{diff} kg)",
    "progress_entry_same": "📅 {day}: *{w} kg* (➡️ o'zgarish yo'q)",
    "progress_total_down": "\n📉 Davr ichida: *{diff} kg* — ajoyib natija!",
    "progress_total_up": "\n📈 Davr ichida: *+{diff} kg*",
    "progress_total_stable": "\n➡️ Davr ichida: vazn barqaror",
    "progress_to_goal": "🎯 Maqsadga ({target} kg): *{diff} kg* qoldi",
    "progress_goal_reached": "🏆 {target} kg maqsadi — *erishildi!*",

    # ── Target ────────────────────────────────────────────────────
    "target_current": "🎯 *Maqsad vazni:* {target} kg\n",
    "target_remaining": "📍 Joriy vazn: {current} kg — *{diff} kg* qoldi",
    "target_reached": "🏆 Joriy vazn: {current} kg — maqsadga erishildi!",
    "target_change_hint": "\n\nO'zgartirish: `/target 70`",
    "target_not_set": "🎯 Maqsad vazni belgilanmagan.\n\nShunday belgilang: `/target 75`",
    "target_bad_format": "❌ Noto'g'ri format. Foydalaning: `/target 75`",
    "target_need_profile": "📋 Maqsad xavfsizligini tekshirish uchun profil kerak (bo'y, yosh, jins, faollik).\n\nProfilingizni to'ldiring — maqsadingiz qanchalik xavfsizligini tekshiraman.",
    "btn_setup_profile": "👉 Profilni sozlash",
    "target_safe_set": "✅ *Maqsad belgilandi: {target} kg*\n\n📊 Tavsiya etilgan kaloriya: *{cal} kkal/kun*\n",
    "target_min_cal_warn": "⚠️ _Minimal xavfsiz kaloriya: {min_cal} kkal/kun_\n",
    "target_weeks": "⏱ Taxminiy muddat: *{weeks} hafta*",
    "target_warn_low_bmi": "⚠️ Maqsad vazni *{target} kg* BMI *{bmi}* beradi — normaldan past.\nBo'yingiz uchun minimal tavsiya etilgan vazn: *{min_weight} kg*.\n\nBoshlashdan oldin mutaxassis bilan maslahatlashing.",
    "target_danger_bmi": "🚨 Maqsad vazni *{target} kg* — BMI *{bmi}*, xavfli darajada past.\n{height} sm bo'y uchun tavsiya etilgan minimum: *{min_weight} kg*.\n\nShifokor bilan maslahatlashishni qat'iy tavsiya qilamiz.",
    "target_critical_bmi": "❌ *{target} kg* maqsadini belgilash mumkin emas.\nBMI *{bmi}* kritik darajada past va hayot uchun xavfli.\n\nBo'yingiz uchun minimal xavfsiz vazn: *{min_weight} kg*.\nIltimos shifokor yoki diyetologga murojaat qiling.",
    "btn_target_confirm": "✅ Baribir belgilash",
    "btn_target_confirm_warn": "⚠️ Baribir belgilash (tavsiya etilmaydi)",
    "btn_target_change": "✏️ Maqsadni o'zgartirish",
    "target_confirmed_msg": "✅ Maqsad vazni *{target} kg* belgilandi.\n\n⚠️ Mutaxassis bilan maslahat tavsiyasini yodda saqlang.",
    "target_change_prompt": "Yangi maqsad vaznini kiriting: `/target 70`",

    # ── Meal analysis ─────────────────────────────────────────────
    "analyzing_photo": "🔍 Rasm tahlil qilinmoqda...",
    "analyzing_text": "🔍 Kaloriyalar hisoblanmoqda...",
    "counting_calories": "🔍 Kaloriyalar hisoblanmoqda...",
    "recalculating": "🔍 Qayta hisoblanmoqda...",
    "analysis_error_parse": "😔 Javobni tahlil qilib bo'lmadi. Qayta urinib ko'ring yoki aniqroq rasm oling.",
    "analysis_error_photo": "😔 Rasmni tahlil qilishda xato yuz berdi. Qayta urinib ko'ring!",
    "analysis_error_text": "😔 Tushunib bo'lmadi. Batafsilroq tasvirlashga harakat qiling!",
    "analysis_error_generic": "😔 Xato yuz berdi. Qayta urinib ko'ring!",
    "correction_error": "😔 Qayta hisoblash mumkin bo'lmadi. Batafsilroq tasvirlashga harakat qiling!",
    "corrected_prefix": "✅ *Tuzatildi!*\n\n",

    # ── Meal summary ──────────────────────────────────────────────
    "meal_summary_header": "🍽️ *{food}*\n\n🔥 *{cal} kkal*\n🥩 Oqsil: *{protein} g*\n🧈 Yog': {fat} g\n🍞 Uglevodlar: {carbs} g\n\n💬 _{comment}_\n\n📊 *Bugungi jami:*\n🔥 {total_cal} kkal (~{day_pct}% kunlik normadan)  🥩 oqsil: *{total_protein} g*",
    "meal_remaining_profile": "\n\n🎯 Maqsadga qolgan: *~{cal_left} kkal* va *~{prot_left} g oqsil*\n_(maqsad: {cal_low}–{cal_high} kkal/kun)_",
    "meal_on_target_profile": "\n\n✅ Maqsad doirasida! ({cal_low}–{cal_high} kkal/kun)",
    "meal_over_target_profile": "\n\n⚠️ Maqsaddan ~*{over} kkal* ortiq",
    "meal_remaining_default": "\n\n🎯 O'rtacha normaga qolgan: *~{cal_left} kkal* va *~{prot_left} g oqsil*",
    "meal_on_target_default": "\n\n✅ O'rtacha normaga erishildi!",
    "meal_over_target_default": "\n\n⚠️ O'rtacha normadan *{over} kkal* ortiq",

    # ── Meal keyboard ─────────────────────────────────────────────
    "btn_meal_confirm": "✅ To'g'ri",
    "btn_meal_edit": "✏️ Tahrirlash",
    "btn_meal_delete": "🗑️ O'chirish",
    "edit_prompt": "✏️ Tuzatishni yozing — qayta hisoblayman:",
    "quick_add_prompt": "📸 Taomingiz rasmini yuboring yoki nima yeganingizni yozing — hisoblayman!",
    "menu_add_prompt": "📸 Taomingiz rasmini yuboring yoki nima yeganingizni yozing — hisoblayman!",

    # ── Short input hint ──────────────────────────────────────────
    "short_input_hint": "📸 Taom rasmi yuboring yoki nima yeganingizni yozing — kaloriyalarni hisoblayman!\n\nMasalan: *«bir kosa sho'rva va non»* yoki *«2 tuxum, sutli qahva»*",
    "send_photo_prompt": "📸 Rasm yuboring yoki taomni tasvirlab bering — kaloriyalarni hisoblayman!\n\nMasalan: *«tovuq va guruch 300g»*",

    # ── Profile ───────────────────────────────────────────────────
    "profile_not_set": "📋 *Profil sozlanmagan*\n\nProfilingizni to'ldiring — kaloriya normasini va rivojlanishingizni aniqroq hisoblayman.",
    "btn_edit_profile": "✏️ Profilni tahrirlash",
    "profile_goal_lose": "Vazn yo'qotish 🥦",
    "profile_goal_maintain": "Vaznni saqlash ⚖️",
    "profile_goal_gain": "Mushak olish 💪",
    "profile_activity_sedentary": "O'troq 🪑",
    "profile_activity_light": "Yengil 🚶",
    "profile_activity_moderate": "O'rtacha 🏃",
    "profile_activity_active": "Faol 💪",
    "profile_view": "👤 *Profilingiz*\n\n🎯 Maqsad: {goal}\n⚡ Faollik: {activity}\n📏 Bo'y: {height} sm\n⚖️ Vazn: {weight} kg\n",
    "profile_last_weight": "📅 So'nggi vazn: *{w} kg* ({day})\n",
    "profile_weight_goal_reached": "🏁 Vazn maqsadi: *{target} kg* — erishildi! 🎉\n",
    "profile_weight_to_goal": "🏁 Maqsadga ({target} kg): *{diff} kg*\n",
    "profile_norm": "\n🔥 Norma: *{low}–{high} kkal/kun*\n🥩 Oqsil: *{protein} g/kun*\n📊 Bugun yeyildi: *{today_cal} kkal*",

    # ── Onboarding / Profile flow ─────────────────────────────────
    "profile_prompt_title": "📊 *Keling, kaloriyalarni siz uchun sozlaymiz*\n\n4 savolga javob bering — hisoblash aniqroq bo'ladi\n30 soniyadan kam vaqt ketadi",
    "btn_profile_yes": "👉 Boshlaylik",
    "btn_profile_skip": "O'tkazib yuborish",
    "ask_goal": "Maqsadingiz nima?",
    "ask_sex": "Jinsingiz?",
    "ask_activity": "Turmush tarzingiz?",
    "ask_age": "Nechanchi yoshdasiz?\n\nRaqam yozing, masalan: *28*",
    "ask_height": "Bo'yingiz?\n\nSantimetrda yozing, masalan: *178*",
    "ask_weight": "Joriy vazningiz?\n\nKilogrammda yozing, masalan: *75*",
    "ask_target_weight": "Maqsad vazningiz bormi?",
    "btn_set_target_yes": "✏️ Ha, belgilayman",
    "btn_skip": "O'tkazib yuborish",
    "ask_target_weight_enter": "Maqsad vazningizni kg da yozing, masalan: *70*",
    "age_bad": "Yoshingizni raqamda yozing, masalan: *28*",
    "height_bad": "Bo'yingizni sm da raqamda yozing, masalan: *178*",
    "weight_bad": "Vazningizni kg da raqamda yozing, masalan: *75*",
    "target_weight_bad": "Vaznni kg da raqamda yozing, masalan: *70*",
    "target_weight_critical_onb": "❌ Maqsad vazni *{target} kg* — BMI *{bmi}*, kritik darajada xavfli.\n{height} sm bo'y uchun minimal xavfsiz vazn: *{min_weight} kg*.\n\nBoshqa maqsad vaznini yozing:",
    "btn_target_confirm_onb": "✅ Baribir belgilash",
    "btn_target_change_onb": "✏️ Maqsadni o'zgartirish",
    "target_change_onb_prompt": "Boshqa maqsad vaznini yozing, masalan: *70*",
    "goal_label_lose": "Vazn yo'qotish",
    "goal_label_maintain": "Vaznni saqlash",
    "goal_label_gain": "Mushak olish",

    # ── Profile goal buttons ──────────────────────────────────────
    "btn_goal_lose": "📉 Vazn yo'qotish",
    "btn_goal_maintain": "⚖️ Vaznni saqlash",
    "btn_goal_gain": "📈 Mushak olish",
    "btn_sex_male": "👨 Erkak",
    "btn_sex_female": "👩 Ayol",
    "btn_activity_sedentary": "🪑 O'troq (ofis, sport yo'q)",
    "btn_activity_light": "🚶 Yengil faollik (haftada 1–2 marta)",
    "btn_activity_moderate": "🏃 O'rtacha (haftada 3–5 marta)",
    "btn_activity_active": "💪 Faol (har kuni)",

    # ── Finish profile ────────────────────────────────────────────
    "profile_done": "✅ *Tayyor!*\n\n🎯 Maqsad: *{goal}*\n🔥 Kaloriya: *{low}–{high} kkal/kun*\n🥩 Oqsil: *~{protein} g/kun*{target_line}\n\nHar bir taomdan so'ng maqsadga necha kkal qolganini ko'rsataman 🎯",
    "profile_target_line_remaining": "\n⚖️ Maqsad vazni: *{target} kg* (~{diff} kg qoldi)",
    "profile_target_line_reached": "\n⚖️ Maqsad vazni: *{target} kg* — allaqachon erishildi! 🏆",
    "ask_timezone": "🔔 *Keling, ovqatlanishni kuzatish uchun eslatmalarni sozlaymiz!*\n\nTaom yozishni eslataman — shunchaki rasm yuboring yoki nima yeganingizni yozing.\n\nSiz uchun joriy vaqtni yozing, masalan: *23:15*",

    # ── Notifications ─────────────────────────────────────────────
    "notify_header": "⏰ *Eslatma sozlamalari*\n\n🌍 Vaqt mintaqasi: {tz} (hozir {time})\n\n☕ Nonushta — {b_time} ({b})\n🍲 Tushlik — {l_time} ({l})\n🍽️ Kechki ovqat — {d_time} ({d})\n\n⚠️ Kamida 1 ta eslatmani yoqiq saqlashni tavsiya qilamiz",
    "btn_notif_all_on": "✅ Hammasini yoqish",
    "btn_notif_all_off": "❌ Hammasini o'chirish",
    "btn_notif_change_tz": "🌍 Vaqt mintaqasini o'zgartirish",
    "notif_enabled": "✅",
    "notif_disabled": "❌",
    "notif_breakfast": "☕ Nonushta",
    "notif_lunch": "🍲 Tushlik",
    "notif_dinner": "🍽️ Kechki ovqat",
    "notif_time_prompt": "⏰ *{meal}* uchun yangi eslatma vaqtini yozing\n\nFormat: *SS:DD*, masalan: *08:30*",
    "notif_timezone_prompt": "🕐 Siz uchun joriy vaqtni yozing, masalan: *23:15*\n\nVaqt mintaqangizni avtomatik aniqlayman.",
    "notif_timezone_updated": "✅ Vaqt mintaqasi yangilandi: UTC{sign}{offset}\n\n",
    "notif_time_updated": "✅ Eslatma vaqti ({meal}) yangilandi: *{time}*\n\n",
    "notif_time_bad": "❌ Vaqtni tushunib bo'lmadi. *SS:DD* formatida yozing, masalan: *08:30*",
    "timezone_bad": "Tushunmadim 🤔 Vaqtni *SS:DD* formatida yozing, masalan: *23:15*",
    "meal_name_breakfast": "nonushta",
    "meal_name_lunch": "tushlik",
    "meal_name_dinner": "kechki ovqat",
    "notif_tz_saved": "🔔 *Eslatmalar yoqildi!*\n\n🌍 Vaqt mintaqasi: {tz}\n☕ Nonushta — 9:00\n🍲 Tushlik — 13:00\n🍽️ Kechki ovqat — 19:00\n\nSozlash: /notify",
    "onb_tz_saved": "🔔 *Eslatmalar yoqildi!*\n\n🌍 Vaqt mintaqasi: {tz}\n☕ Nonushta — 9:00\n🍲 Tushlik — 13:00\n🍽️ Kechki ovqat — 19:00\n\nSozlash: /notify",
    "onb_tz_skip": "OK, eslatma bo'lmaydi 👌\nIstalgan vaqt yoqing: /notify",
    "notif_snooze_done": "✅ {meal} uchun eslatma o'chirildi.\nQayta yoqish: /notify",

    # ── Timezone city names ───────────────────────────────────────
    "tz_kyiv": "🇺🇦 Kiyev",
    "tz_moscow": "🇷🇺 Moskva",
    "tz_baku": "🇦🇿 Boqu",
    "tz_almaty": "🇰🇿 Olmaota",
    "tz_tashkent": "🇺🇿 Toshkent",
    "tz_novosibirsk": "Novosibirsk",
    "tz_irkutsk": "Irkutsk",
    "tz_vladivostok": "Vladivostok",
    "tz_skip": "❌ O'tkazib yuborish",

    # ── Trial / Paywall ───────────────────────────────────────────
    "trial_exhausted": "❌ *Bepul tahlillar tugadi* (15 dan 15)\n\nKaloriyalarni hisoblashda davom etish uchun obuna oling 👇",
    "trial_last_1": "⚠️ {limit} dan *1 bepul tahlil* qoldi → /subscribe",
    "trial_last_few": "⚠️ {limit} dan *{left} bepul tahlil* qoldi → /subscribe",
    "trial_some_left": "🎁 {limit} dan {left} bepul tahlil qoldi → /subscribe",
    "trial_many_left": "🎁 Bepul tahlillar: {limit} dan {left}",
    "btn_subscribe": "💳 Obuna olish",
    "subscribe_remaining": "🎁 Bepul tahlillar qoldi: *{limit} dan {left}*\n\n",
    "subscribe_exhausted": "❌ Bepul tahlillar tugadi\n\n",
    "subscribe_header": "💳 *Meal Scan Obunasi*\n\nRejani tanlang:",
    "subscribe_header_full": "💳 *Meal Scan Obunasi*\n\nRasm va matndan cheksiz kaloriya hisoblash\n\nRejani tanlang:",
    "subscribe_active": "✅ *Obuna {expires} gacha faol*\n\nErtaroq yangilashingiz mumkin — vaqt joriy davrga qo'shiladi:",
    "payment_success": "🎉 *{label} uchun obuna faollashtirildi!*\n\nCheksiz kaloriya hisoblang 🍽️\nRasm yuboring yoki nima yeganingizni yozing ↓",
    "sub_1m_label": "1 oy",
    "sub_3m_label": "3 oy",
    "sub_invoice_title_1m": "Meal Scan Obunasi — 1 oy",
    "sub_invoice_title_3m": "Meal Scan Obunasi — 3 oy",
    "sub_invoice_desc": "Rasm va matndan cheksiz kaloriya va makro hisoblash",
    "sub_invoice_error": "❌ Hisob-faktura yaratish xatosi: {e}",

    # ── Delete command ────────────────────────────────────────────
    "delete_no_num": "❌ Taom raqamini ko'rsating.\nMasalan: `/delete 2`\n\nBugungi ro'yxat: /today",
    "delete_bad_num": "❌ Raqam butun son bo'lishi kerak. Masalan: `/delete 2`",
    "delete_no_meals": "📭 Bugun hech qanday taom yozuvi yo'q.",
    "delete_out_of_range": "❌ #{num} raqamli taom yo'q. Bugungi yozuvlar: {total}.\n\nRo'yxatga qarang: /today",
    "delete_done": "🗑️ O'chirildi: *{food}* ({cal} kkal)\n\n📊 Bugun qolgan: *{total_cal} kkal* ({n} taom)",

    # ── Edit command ──────────────────────────────────────────────
    "edit_no_args": "✏️ Format: `/edit raqam yangi tavsif`\nMasalan: `/edit 2 mol go'shti borscht 400g`\n\nBugungi ro'yxat: /today",
    "edit_bad_num": "❌ Avval raqam ko'rsating. Masalan: `/edit 2 borscht 400g`",
    "edit_no_meals": "📭 Bugun hech qanday taom yozuvi yo'q.",
    "edit_out_of_range": "❌ #{num} raqamli taom yo'q. Bugungi yozuvlar: {total}.",
    "edit_done": "✅ *#{num} raqamli taom yangilandi*\n\n🍽️ {food}\n🔥 {cal} kkal | 🥩 {protein} g | 🧈 {fat} g | 🍞 {carbs} g\n\n📊 Bugun: *{total_cal} kkal* / 🥩 *{total_protein} g oqsil*",

    # ── Delete from diary (callback) ──────────────────────────────
    "diary_deleted": "🗑️ Yozuv o'chirildi.\n\n📊 Bugun yeyildi: *{cal} kkal* / 🥩 *{protein} g oqsil* ({n} taom)\n{remaining}",
    "diary_cal_left": "🎯 Maqsadga qolgan: *{cal_left} kkal* va *{prot_left} g oqsil*",
    "diary_cal_done": "✅ Kaloriya maqsadiga erishildi!",
    "diary_cal_over": "⚠️ Maqsad *{over} kkal* oshib ketdi",

    # ── Reminders ─────────────────────────────────────────────────
    "reminder_text": "{emoji} {meal} uchun nima yeganingizni aytishni unutmang!\nMaqsad: {goal_cal} kkal. Bugun: {total_cal} kkal\n\n📸 Shunchaki rasm yuboring yoki yozing",
    "btn_reminder_add": "🍽️ Taom qo'shish",
    "btn_reminder_snooze": "❌ {meal} eslatmasini to'xtatish",

    # ── Win-back ──────────────────────────────────────────────────
    "winback": "Sizni sog'indik 👋\n\n15 bepul skaningiz tugadi — ammo sog'lom ovqatlanishga yo'lingiz endigina boshlanmoqda.\n\nObuna bo'ling va har bir ovqatlanishni kuzatishda davom eting, hech narsani o'tkazib yubormang 🥗",

    # ── Evening push ──────────────────────────────────────────────
    "evening_summary": "🌙 Kunning xulosasi\n\nBugun: *{total_cal} kkal* / {goal_cal} ({day_pct}%)\nOqsil: *{total_protein} g*",
    "evening_no_logs": "📸 Kun qanday o'tdi?\n\nBugun hali hech narsa yozilmadi — kechki ovqatni unutmang.\nShunchaki rasm oling, 5 soniya ketadi.",

    # ── Weight tip ────────────────────────────────────────────────
    "weight_tip": "⚖️ *Maslahat: vazningizni kuzating*\n\nHar ertalab vazningizni yozishingiz mumkin — bot dinamikani va maqsadga erishish jarayonini ko'rsatadi.\n\nShunchaki /weight yozing va joriy vazningizni kiriting.\nRivojlanish grafigi: /progress",

    # ── Admin ─────────────────────────────────────────────────────
    "resetme_done": "✅ Barcha ma'lumotlar o'chirildi. Qayta boshlash uchun /start yozing.",
    "gift_usage": "Foydalanish: /gift <user_id>",
    "gift_bad_id": "❌ user_id raqam bo'lishi kerak",
    "gift_done": "✅ {uid} foydalanuvchiga doimiy kirish berildi.",
    "error_terms": "❌ Xato: {e}",
    "error_invoice": "❌ Hisob-faktura yaratish xatosi: {e}",
}
