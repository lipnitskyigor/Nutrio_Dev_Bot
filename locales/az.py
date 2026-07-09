texts = {
    # ── Menu buttons ──────────────────────────────────────────────
    "menu_diary":   "📔 Gündəlik",
    "menu_profile": "👤 Profil",
    "menu_help":    "❓ Kömək",
    "menu_add":     "🍽️ Yemək əlavə et",
    "input_placeholder": "Şəkil göndərin və ya nə yediyinizi yazın...",

    # ── Language switching ────────────────────────────────────────
    "choose_language": "Dil seçin / Choose language:",
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
    "claude_lang": "Azərbaycan dilində",

    # ── Terms ─────────────────────────────────────────────────────
    "terms_greeting": "👋 Salam, {name}!\n\nBaşlamazdan əvvəl zəhmət olmasa bunu oxuyun:\n\n⚠️ Meal Scan kalori və qida izləmə köməkçisidir.\nBu tibbi tətbiq deyil. Bot həkimi,\ndiyetoloqu və ya qida mütəxəssisini əvəz etmir.\n\n📄 İstifadə şərtləri: mealscan.org/terms.html\n\nAşağıdakı düyməyə toxunmaqla istifadə şərtlərini qəbul edirsiniz.",
    "btn_accept_terms": "✅ Şərtləri qəbul et",

    # ── Start / Welcome ───────────────────────────────────────────
    "welcome_back": "Xoş gəldiniz, {name}! 👋\n\n📸 Yeməyinizin şəklini göndərin və ya nə yediyinizi yazın — hesablayacağam.",
    "welcome_new": "Qidalanmanızı izləməyə kömək edirəm — foto və ya mətn əsasında kalori və BJYKarb hesablayıram.\n\n📸 *İstənilən yeməyin şəklini göndərin*\n✏️ Yaxud nə yediyinizi yazın\n\nİndi sınayın ↓\n\n———\nℹ️ Meal Scan qida izləmə köməkçisidir, tibbi tətbiq deyil. Sağlamlıq problemləriniz varsa və ya pəhrizinizi dəyişmək istəyirsinizsə, əvvəlcə həkim və ya diyetoloqla məsləhətləşin.",
    "default_friend": "dost",

    # ── Help ──────────────────────────────────────────────────────
    "help_text": (
        "🤖 *Botdan necə istifadə etmək olar:*\n\n"
        "📸 Yemək şəkli göndərin — kalori və BJYKarb hesablayacağam\n"
        "✏️ Nə yediyinizi yazın — onu da hesablayacağam\n"
        "Məsələn: _«toyuq ilə qarabaşaq 300q»_\n\n"
        "📊 *Kalori və qida:*\n"
        "/today — bugünkü cəm (kalori, zülal, yağ, karbohidrat)\n"
        "/history — son 7 günün qida tarixi\n"
        "/goal 2000 150 — gündəlik kalori və zülal hədəfi təyin edin\n"
        "/goal — cari hədəfinizə baxın\n"
        "/reset — bugünkü qeydləri silin\n\n"
        "⚖️ *Çəki və irəliləyiş:*\n"
        "/weight 80.5 — çəkinizi qeyd edin (hər gün edin)\n"
        "/weight — sonuncu qeyd edilmiş çəkiyə baxın\n"
        "/target 75 — hədəf çəki təyin edin\n"
        "/target — hədəf çəkiyə və nə qədər qaldığına baxın\n"
        "/progress — 7 günlük çəki dinamikası 🟢🔴 dəyişikliklərlə\n\n"
        "💡 Məsləhət: şəkildəki yemək nə qədər aydın olarsa, nəticə bir o qədər dəqiq olar!\n\n"
        "🔔 *Xatırlatmalar:*\n"
        "/notify — yemək xatırlatmalarını tənzimləyin\n\n"
        "💬 *Dəstək:*\n"
        "/support — dəstəklə əlaqə saxlayın"
    ),

    # ── Support ───────────────────────────────────────────────────
    "support_text": "💬 *Meal Scan Dəstəyi*\n\nSualınız və ya probleminiz varsa — bizə yazın:\n\n👉 @Meal\_Scan\_Support",

    # ── Today ─────────────────────────────────────────────────────
    "today_empty": "📭 Bu gün hələ heç bir qida qeydi yoxdur.\nSaymağa başlamaq üşün yeməyin şəklini göndərin!",
    "today_header": "📊 *Bugünkü cəm — {name}*\n",
    "today_meal_line": "{i}. {food} — {cal} kkal ({time})",
    "today_total_cal": "\n🔥 *Cəmi: {cal} kkal*",
    "today_macros": "🥩 Zülal: {protein} q  🧈 Yağ: {fat} q  🍞 Karbohidrat: {carbs} q",
    "today_cal_left": "\n🎯 Hədəfə qədər qalan: *{cal_left} kkal* və *{prot_left} q zülal*",
    "today_cal_done": "\n✅ *Kalori hədəfinə çatdınız!*",
    "today_cal_over": "\n⚠️ Hədəf *{over} kkal* aşıldı",

    # ── History ───────────────────────────────────────────────────
    "history_empty": "📭 Son 7 gün üçün məlumat yoxdur.\nBaşlamaq üçün yemək şəkli göndərin!",
    "history_header": "📅 *7 günlük tarix — {name}*\n",
    "history_entry": "📆 {day}: *{cal} kkal* ({n} yemək{suffix})",
    "history_meals_suffix_1": "",
    "history_meals_suffix_other": "",

    # ── Reset ─────────────────────────────────────────────────────
    "reset_done": "🗑️ Bugünkü məlumatlar silindi!",

    # ── Goal ──────────────────────────────────────────────────────
    "goal_current": "🎯 *Gündəlik hədəfiniz:*\n🔥 Kalori: {cal} kkal\n🥩 Zülal: {protein} q\n\nDəyişdirmək üçün: `/goal 2000 150`",
    "goal_not_set": "🎯 Hədəf təyin edilməyib.\n\nBelə təyin edin: `/goal kalori zülal`\nMəsələn: `/goal 2000 150`",
    "goal_saved": "✅ *Hədəf təyin edildi!*\n🔥 Kalori: {cal} kkal/gün\n🥩 Zülal: {protein} q/gün",
    "goal_bad_format": "❌ Yanlış format. İstifadə edin: `/goal 2000 150`",

    # ── Weight ────────────────────────────────────────────────────
    "weight_last": "⚖️ *Sonuncu çəki:* {weight} kq ({day})\n\nYenisini qeyd etmək üçün: `/weight 80.5`",
    "weight_not_set": "⚖️ Hələ heç bir çəki qeyd edilməyib.\n\nBelə qeyd edin: `/weight 80.5`",
    "weight_saved": "⚖️ *Çəki qeyd edildi:* {weight} kq\n",
    "weight_to_goal": "\n🎯 Hədəfə qədər ({target} kq): *{diff} kq* qalıb\n",
    "weight_almost": "💪 Az qaldı! Hədəfinizə çox yaxınsınız!",
    "weight_great_progress": "🔥 Əla irəliləyiş, belə davam edin!",
    "weight_good_start": "💪 Yaxşı başlanğıc! Hər gün hədəfinizə bir az daha yaxınlaşırsınız.",
    "weight_goal_reached": "\n🏆 Hədəfə çatdınız! Hədəf çəkinizdən {diff} kq aşağıdasınız!",
    "weight_on_goal": "\n🎯 Tam hədəf çəkinizdəsiniz! Əla!",
    "weight_set_target_hint": "\n💡 Hədəf çəkinizi `/target 75` ilə təyin edin",
    "weight_bad_format": "❌ Yanlış format. İstifadə edin: `/weight 80.5`",

    # ── Progress ──────────────────────────────────────────────────
    "progress_empty": "⚖️ Çəki məlumatı yoxdur.\n\nHər gün `/weight 80.5` ilə çəkinizi qeyd edin — dinamikanı göstərəcəyəm!",
    "progress_header": "📈 *Çəki dinamikası:*\n",
    "progress_entry_first": "📅 {day}: *{w} kq*",
    "progress_entry_down": "📅 {day}: *{w} kq* (🟢 {diff} kq)",
    "progress_entry_up": "📅 {day}: *{w} kq* (🔴 +{diff} kq)",
    "progress_entry_same": "📅 {day}: *{w} kq* (➡️ dəyişiklik yoxdur)",
    "progress_total_down": "\n📉 Dövr ərzində: *{diff} kq* — əla nəticə!",
    "progress_total_up": "\n📈 Dövr ərzində: *+{diff} kq*",
    "progress_total_stable": "\n➡️ Dövr ərzində: çəki sabitdir",
    "progress_to_goal": "🎯 Hədəfə qədər ({target} kq): *{diff} kq* qalıb",
    "progress_goal_reached": "🏆 {target} kq hədəfi — *çatıldı!*",

    # ── Target ────────────────────────────────────────────────────
    "target_current": "🎯 *Hədəf çəki:* {target} kq\n",
    "target_remaining": "📍 Cari çəki: {current} kq — *{diff} kq* qalıb",
    "target_reached": "🏆 Cari çəki: {current} kq — hədəfə çatıldı!",
    "target_change_hint": "\n\nDəyişdirmək: `/target 70`",
    "target_not_set": "🎯 Hədəf çəki təyin edilməyib.\n\nBelə təyin edin: `/target 75`",
    "target_bad_format": "❌ Yanlış format. İstifadə edin: `/target 75`",
    "target_need_profile": "📋 Hədəfin təhlükəsizliyini yoxlamaq üçün profil lazımdır (boy, yaş, cins, aktivlik).\n\nProfilinizi qurun — hədəfinizin nə qədər təhlükəsiz olduğunu yoxlayacağam.",
    "btn_setup_profile": "👉 Profili qur",
    "target_safe_set": "✅ *Hədəf təyin edildi: {target} kq*\n\n📊 Tövsiyə olunan kalori: *{cal} kkal/gün*\n",
    "target_min_cal_warn": "⚠️ _Minimum təhlükəsiz kalori: {min_cal} kkal/gün_\n",
    "target_weeks": "⏱ Təxmini müddət: *{weeks} həftə*",
    "target_warn_low_bmi": "⚠️ Hədəf çəki *{target} kq* BMI *{bmi}* verir — normaldan aşağı.\nBoyunuz üçün minimum tövsiyə olunan çəki: *{min_weight} kq*.\n\nBaşlamazdan əvvəl mütəxəssislə məsləhətləşin.",
    "target_danger_bmi": "🚨 Hədəf çəki *{target} kq* — BMI *{bmi}*, təhlükəli dərəcədə aşağı.\n{height} sm boy üçün tövsiyə olunan minimum: *{min_weight} kq*.\n\nHəkim ilə məsləhətləşməyi şiddətlə tövsiyə edirik.",
    "target_critical_bmi": "❌ *{target} kq* hədəfini təyin etmək mümkün deyil.\nBMI *{bmi}* kritik dərəcədə aşağı və həyat üçün təhlükəlidir.\n\nBoyunuz üçün minimum təhlükəsiz çəki: *{min_weight} kq*.\nZəhmət olmasa həkim və ya diyetoloqa müraciət edin.",
    "btn_target_confirm": "✅ Yenə də təyin et",
    "btn_target_confirm_warn": "⚠️ Yenə də təyin et (tövsiyə edilmir)",
    "btn_target_change": "✏️ Hədəfi dəyiş",
    "target_confirmed_msg": "✅ Hədəf çəki *{target} kq* təyin edildi.\n\n⚠️ Mütəxəssislə məsləhətləşmə tövsiyəsini yadda saxlayın.",
    "target_change_prompt": "Yeni hədəf çəki daxil edin: `/target 70`",

    # ── Meal analysis ─────────────────────────────────────────────
    "analyzing_photo": "🔍 Şəkil təhlil edilir...",
    "counting_calories": "🔍 Kalorilər hesablanır...",
    "recalculating": "🔍 Yenidən hesablanır...",
    "analysis_error_parse": "😔 Cavabı analiz etmək mümkün olmadı. Yenidən cəhd edin və ya daha aydın şəkil çəkin.",
    "analysis_error_photo": "😔 Şəkili analiz edərkən xəta baş verdi. Yenidən cəhd edin!",
    "analysis_error_text": "😔 Anlamaq mümkün olmadı. Daha ətraflı təsvir etməyə çalışın!",
    "analysis_error_generic": "😔 Xəta baş verdi. Yenidən cəhd edin!",
    "correction_error": "😔 Yenidən hesablamaq mümkün olmadı. Daha ətraflı təsvir etməyə çalışın!",
    "corrected_prefix": "✅ *Düzəldildi!*\n\n",

    # ── Meal summary ──────────────────────────────────────────────
    "meal_summary_header": "🍽️ *{food}*\n\n🔥 *{cal} kkal*\n🥩 Zülal: *{protein} q*\n🧈 Yağ: {fat} q\n🍞 Karbohidrat: {carbs} q\n\n💬 _{comment}_\n\n📊 *Bugünkü cəm:*\n🔥 {total_cal} kkal (~{day_pct}% gündəlik normanın)  🥩 zülal: *{total_protein} q*",
    "meal_remaining_profile": "\n\n🎯 Hədəfə qədər qalan: *~{cal_left} kkal* və *~{prot_left} q zülal*\n_(hədəf: {cal_low}–{cal_high} kkal/gün)_",
    "meal_on_target_profile": "\n\n✅ Hədəf daxilindədir! ({cal_low}–{cal_high} kkal/gün)",
    "meal_over_target_profile": "\n\n⚠️ Hədəfdən ~*{over} kkal* artıqdır",
    "meal_remaining_default": "\n\n🎯 Orta normaya qədər qalan: *~{cal_left} kkal* və *~{prot_left} q zülal*",
    "meal_on_target_default": "\n\n✅ Orta normaya çatıldı!",
    "meal_over_target_default": "\n\n⚠️ Orta normadan *{over} kkal* artıqdır",

    # ── Meal keyboard ─────────────────────────────────────────────
    "btn_meal_confirm": "✅ Düzdür",
    "btn_meal_edit": "✏️ Düzəlt",
    "btn_meal_delete": "🗑️ Sil",
    "edit_prompt": "✏️ Düzəlişi yazın — yenidən hesablayacağam:",
    "quick_add_prompt": "📸 Yeməyinizin şəklini göndərin və ya nə yediyinizi yazın — hesablayacağam!",
    "menu_add_prompt": "📸 Yeməyinizin şəklini göndərin və ya nə yediyinizi yazın — hesablayacağam!",

    # ── Short input hint ──────────────────────────────────────────
    "short_input_hint": "📸 Yemək şəkli göndərin və ya nə yediyinizi yazın — kalorileri hesablayacağam!\n\nMəsələn: *«bir qab şorba və çörək»* və ya *«2 yumurta, südlü qəhvə»*",

    # ── Profile ───────────────────────────────────────────────────
    "profile_not_set": "📋 *Profil qurulmayıb*\n\nProfilinizi doldurun — kalori normanızı və irəliləyişinizi daha dəqiq hesablayacağam.",
    "btn_edit_profile": "✏️ Profili redaktə et",
    "profile_goal_lose": "Çəki itirmək 🥦",
    "profile_goal_maintain": "Çəkini saxlamaq ⚖️",
    "profile_goal_gain": "Əzələ qazanmaq 💪",
    "profile_activity_sedentary": "Oturaq 🪑",
    "profile_activity_light": "Yüngül 🚶",
    "profile_activity_moderate": "Orta 🏃",
    "profile_activity_active": "Aktiv 💪",
    "profile_view": "👤 *Profiliniz*\n\n🎯 Hədəf: {goal}\n⚡ Aktivlik: {activity}\n📏 Boy: {height} sm\n⚖️ Çəki: {weight} kq\n",
    "profile_last_weight": "📅 Sonuncu çəki: *{w} kq* ({day})\n",
    "profile_weight_goal_reached": "🏁 Çəki hədəfi: *{target} kq* — çatıldı! 🎉\n",
    "profile_weight_to_goal": "🏁 Hədəfə qədər ({target} kq): *{diff} kq*\n",
    "profile_norm": "\n🔥 Norma: *{low}–{high} kkal/gün*\n🥩 Zülal: *{protein} q/gün*\n📊 Bu gün yeyildi: *{today_cal} kkal*",

    # ── Onboarding / Profile flow ─────────────────────────────────
    "profile_prompt_title": "📊 *Gəlin kaloriləri sizin üçün tənzimləyək*\n\n4 suala cavab verin — hesablama daha dəqiq olacaq\n30 saniyədən az vaxt aparır",
    "btn_profile_yes": "👉 Başlayaq",
    "btn_profile_skip": "Keç",
    "ask_goal": "Hədəfiniz nədir?",
    "ask_sex": "Cinsiniz?",
    "ask_activity": "Həyat tərziniz?",
    "ask_age": "Neçə yaşınız var?\n\nRəqəm yazın, məsələn: *28*",
    "ask_height": "Boyunuz?\n\nSantimetrlə yazın, məsələn: *178*",
    "ask_weight": "Cari çəkiniz?\n\nKiloqramla yazın, məsələn: *75*",
    "ask_target_weight": "Hədəf çəkiniz varmı?",
    "btn_set_target_yes": "✏️ Bəli, təyin edəcəm",
    "btn_skip": "Keç",
    "ask_target_weight_enter": "Hədəf çəkinizi kq ilə yazın, məsələn: *70*",
    "age_bad": "Yaşınızı rəqəmlə yazın, məsələn: *28*",
    "height_bad": "Boyunuzu sm ilə rəqəmlə yazın, məsələn: *178*",
    "weight_bad": "Çəkinizi kq ilə rəqəmlə yazın, məsələn: *75*",
    "target_weight_bad": "Çəkini kq ilə rəqəmlə yazın, məsələn: *70*",
    "target_weight_critical_onb": "❌ Hədəf çəki *{target} kq* — BMI *{bmi}*, kritik dərəcədə təhlükəlidir.\n{height} sm boy üçün minimum təhlükəsiz çəki: *{min_weight} kq*.\n\nBaşqa bir hədəf çəki yazın:",
    "btn_target_confirm_onb": "✅ Yenə də təyin et",
    "btn_target_change_onb": "✏️ Hədəfi dəyiş",
    "target_change_onb_prompt": "Başqa bir hədəf çəki yazın, məsələn: *70*",
    "goal_label_lose": "Çəki itirmək",
    "goal_label_maintain": "Çəkini saxlamaq",
    "goal_label_gain": "Əzələ qazanmaq",

    # ── Profile goal buttons ──────────────────────────────────────
    "btn_goal_lose": "📉 Çəki itirmək",
    "btn_goal_maintain": "⚖️ Çəkini saxlamaq",
    "btn_goal_gain": "📈 Əzələ qazanmaq",
    "btn_sex_male": "👨 Kişi",
    "btn_sex_female": "👩 Qadın",
    "btn_activity_sedentary": "🪑 Oturaq (ofis, idman yoxdur)",
    "btn_activity_light": "🚶 Yüngül aktivlik (həftədə 1–2 dəfə)",
    "btn_activity_moderate": "🏃 Orta (həftədə 3–5 dəfə)",
    "btn_activity_active": "💪 Aktiv (hər gün)",

    # ── Finish profile ────────────────────────────────────────────
    "profile_done": "✅ *Hazırdır!*\n\n🎯 Hədəf: *{goal}*\n🔥 Kalori: *{low}–{high} kkal/gün*\n🥩 Zülal: *~{protein} q/gün*{target_line}\n\nHər yeməkdən sonra hədəfə neçə kkal qaldığını göstərəcəyəm 🎯",
    "profile_target_line_remaining": "\n⚖️ Hədəf çəki: *{target} kq* (~{diff} kq qalıb)",
    "profile_target_line_reached": "\n⚖️ Hədəf çəki: *{target} kq* — artıq çatıldı! 🏆",
    "ask_timezone": "🔔 *Gəlin qida izləmə xatırlatmalarını quraq!*\n\nYemək qeyd etməyi xatırladacağam — sadəcə şəkil göndərin və ya nə yediyinizi yazın.\n\nSizin üçün cari saatı yazın, məsələn: *23:15*",

    # ── Notifications ─────────────────────────────────────────────
    "notify_header": "⏰ *Xatırlatma parametrləri*\n\n🌍 Saat qurşağı: {tz} (indi {time})\n\n☕ Səhər yeməyi — {b_time} ({b})\n🍲 Nahar — {l_time} ({l})\n🍽️ Axşam yeməyi — {d_time} ({d})\n\n⚠️ Ən azı 1 xatırlatmanı aktiv saxlamağı tövsiyə edirik",
    "btn_notif_all_on": "✅ Hamısını aktiv et",
    "btn_notif_all_off": "❌ Hamısını deaktiv et",
    "btn_notif_change_tz": "🌍 Saat qurşağını dəyiş",
    "notif_enabled": "✅",
    "notif_disabled": "❌",
    "notif_breakfast": "☕ Səhər yeməyi",
    "notif_lunch": "🍲 Nahar",
    "notif_dinner": "🍽️ Axşam yeməyi",
    "notif_time_prompt": "⏰ *{meal}* üçün yeni xatırlatma vaxtını yazın\n\nFormat: *SS:DQ*, məsələn: *08:30*",
    "notif_timezone_prompt": "🕐 Sizin üçün cari saatı yazın, məsələn: *23:15*\n\nSaat qurşağınızı avtomatik müəyyən edəcəyəm.",
    "notif_timezone_updated": "✅ Saat qurşağı yeniləndi: UTC{sign}{offset}\n\n",
    "notif_time_updated": "✅ Xatırlatma vaxtı ({meal}) yeniləndi: *{time}*\n\n",
    "notif_time_bad": "❌ Saatı anlamaq mümkün olmadı. *SS:DQ* formatında yazın, məsələn: *08:30*",
    "timezone_bad": "Anlamadım 🤔 Saatı *SS:DQ* formatında yazın, məsələn: *23:15*",
    "meal_name_breakfast": "səhər yeməyi",
    "meal_name_lunch": "nahar",
    "meal_name_dinner": "axşam yeməyi",
    "notif_tz_saved": "🔔 *Xatırlatmalar aktiv edildi!*\n\n🌍 Saat qurşağı: {tz}\n☕ Səhər yeməyi — 9:00\n🍲 Nahar — 13:00\n🍽️ Axşam yeməyi — 19:00\n\nTənzimləyin: /notify",
    "onb_tz_saved": "🔔 *Xatırlatmalar aktiv edildi!*\n\n🌍 Saat qurşağı: {tz}\n☕ Səhər yeməyi — 9:00\n🍲 Nahar — 13:00\n🍽️ Axşam yeməyi — 19:00\n\nTənzimləyin: /notify",
    "onb_tz_skip": "Tamam, xatırlatma olmayacaq 👌\nİstənilən vaxt aktiv edin: /notify",
    "notif_snooze_done": "✅ {meal} xatırlatması deaktiv edildi.\nYenidən aktiv edin: /notify",

    # ── Timezone city names ───────────────────────────────────────
    "tz_kyiv": "🇺🇦 Kiyev",
    "tz_moscow": "🇷🇺 Moskva",
    "tz_baku": "🇦🇿 Bakı",
    "tz_almaty": "🇰🇿 Almatı",
    "tz_tashkent": "🇺🇿 Daşkənd",
    "tz_novosibirsk": "Novosibirsk",
    "tz_irkutsk": "İrkutsk",
    "tz_vladivostok": "Vladivostok",
    "tz_skip": "❌ Keç",

    # ── Trial / Paywall ───────────────────────────────────────────
    "trial_exhausted": "❌ *Pulsuz analizlər bitdi* (15-dən 15)\n\nArtıq 15 yemək təhlil etmisən — limitsiz davam et → /subscribe",
    "trial_last_1": "🔴 Son pulsuz analiz! Sonra — limitsiz → /subscribe",
    "trial_last_few": "⚠️ {limit}-dən {left} qalıb. Gündəliyini kəsmə → /subscribe",
    "trial_some_left": "🎁 {limit}-dən {left} qalıb. Sonra — abunəliklə limitsiz analizlər",
    "trial_many_left": "🎁 {limit}-dən {left} pulsuz analiz qalıb",
    "btn_subscribe": "💳 Abunəlik al",
    "subscribe_remaining": "🎁 Pulsuz analizlər qalıb: *{limit}-dən {left}*\n\n",
    "subscribe_exhausted": "❌ Pulsuz analizlər bitdi\n\n",
    "subscribe_header": "💳 *Meal Scan Abunəliyi*\n\nPlan seçin:",
    "subscribe_header_full": "💳 *Meal Scan Abunəliyi*\n\nFoto və mətndən limitsiz kalori sayma\n\nPlan seçin:",
    "subscribe_active": "✅ *Abunəlik {expires} tarixinə qədər aktivdir*\n\nErken yeniləyə bilərsiniz — vaxt cari dövrə əlavə olunacaq:",
    "payment_success": "🎉 *{label} üçün abunəlik aktiv edildi!*\n\nLimitsiz kalori sayın 🍽️\nŞəkil göndərin və ya nə yediyinizi yazın ↓",
    "sub_1m_label": "1 ay",
    "sub_3m_label": "3 ay",
    "sub_invoice_title_1m": "Meal Scan Abunəliyi — 1 ay",
    "sub_invoice_title_3m": "Meal Scan Abunəliyi — 3 ay",
    "sub_invoice_desc": "Foto və mətndən limitsiz kalori və makro sayma",
    "sub_invoice_error": "❌ Faktura yaratma xətası: {e}",

    # ── Delete command ────────────────────────────────────────────
    "delete_no_num": "❌ Yemək nömrəsini göstərin.\nMəsələn: `/delete 2`\n\nBugünkü siyahı: /today",
    "delete_bad_num": "❌ Nömrə tam ədəd olmalıdır. Məsələn: `/delete 2`",
    "delete_no_meals": "📭 Bu gün heç bir qida qeydi yoxdur.",
    "delete_out_of_range": "❌ #{num} nömrəli yemək yoxdur. Bugünkü qeydlər: {total}.\n\nSiyahıya baxın: /today",
    "delete_done": "🗑️ Silindi: *{food}* ({cal} kkal)\n\n📊 Bu gün qalan: *{total_cal} kkal* ({n} yemək)",

    # ── Edit command ──────────────────────────────────────────────
    "edit_no_args": "✏️ Format: `/edit nömrə yeni təsvir`\nMəsələn: `/edit 2 mal əti borştu 400q`\n\nBugünkü siyahı: /today",
    "edit_bad_num": "❌ Əvvəlcə nömrə göstərin. Məsələn: `/edit 2 borşt 400q`",
    "edit_no_meals": "📭 Bu gün heç bir qida qeydi yoxdur.",
    "edit_out_of_range": "❌ #{num} nömrəli yemək yoxdur. Bugünkü qeydlər: {total}.",
    "edit_done": "✅ *#{num} nömrəli yemək yeniləndi*\n\n🍽️ {food}\n🔥 {cal} kkal | 🥩 {protein} q | 🧈 {fat} q | 🍞 {carbs} q\n\n📊 Bu gün: *{total_cal} kkal* / 🥩 *{total_protein} q zülal*",

    # ── Delete from diary (callback) ──────────────────────────────
    "diary_deleted": "🗑️ Qeyd silindi.\n\n📊 Bu gün yeyildi: *{cal} kkal* / 🥩 *{protein} q zülal* ({n} yemək)\n{remaining}",
    "diary_cal_left": "🎯 Hədəfə qədər qalan: *{cal_left} kkal* və *{prot_left} q zülal*",
    "diary_cal_done": "✅ Kalori hədəfinə çatıldı!",
    "diary_cal_over": "⚠️ Hədəf *{over} kkal* aşıldı",

    # ── Reminders ─────────────────────────────────────────────────
    "reminder_text": "{emoji} {meal} üçün nə yediyinizi bildirməyi unutmayın!\nHədəf: {goal_cal} kkal. Bu gün: {total_cal} kkal\n\n📸 Sadəcə şəkil göndərin və ya yazın",
    "btn_reminder_add": "🍽️ Yemək əlavə et",
    "btn_reminder_snooze": "❌ {meal} xatırlatmasını dayandır",

    # ── Win-back ──────────────────────────────────────────────────
    "winback": "Sizi çox istədik 👋\n\n15 pulsuz skanınız bitdi — lakin sağlam qidalanmaya gedən yolunuz yeni başlayır.\n\nAbunə olun və hər yemək qəbulunu izləməyə davam edin, heç nəyi qaçırmayın 🥗",

    # ── Evening push ──────────────────────────────────────────────
    "evening_summary": "🌙 Günün yekunları\n\nBu gün: *{total_cal} kkal* / {goal_cal} ({day_pct}%)\nZülal: *{total_protein} q*",
    "evening_no_logs": "📸 Gün necə keçdi?\n\nBu gün hələ heç nə qeyd edilməyib — axşam yeməyini unutmayın.\nSadəcə şəkil çəkin, 5 saniyə çəkəcək.",

    # ── Weight tip ────────────────────────────────────────────────
    "weight_tip": "⚖️ *Məsləhət: çəkinizi izləyin*\n\nHər səhər çəkinizi qeyd edə bilərsiniz — bot dinamikanı və hədəfə doğru irəliləyişi göstərəcək.\n\nSadəcə /weight yazın və cari çəkinizi daxil edin.\nİrəliləyiş qrafiki: /progress",

    # ── Admin ─────────────────────────────────────────────────────
    "resetme_done": "✅ Bütün məlumatlar silindi. Yenidən başlamaq üçün /start yazın.",
    "gift_usage": "İstifadə: /gift <user_id>",
    "gift_bad_id": "❌ user_id rəqəm olmalıdır",
    "gift_done": "✅ {uid} istifadəçiyə daimi giriş verildi.",
    "error_terms": "❌ Xəta: {e}",
    "error_invoice": "❌ Faktura yaratma xətası: {e}",

    # ── Send photo prompt ─────────────────────────────────────────
    "analyzing_text": "🔍 Kalorilər hesablanır...",
    "send_photo_prompt": "📸 Şəkil göndərin və ya yeməyi təsvir edin — kalorileri hesablayacağam!\n\nMəsələn: *«toyuq və düyü 300q»*",
    # ── Onboarding (new flow) ───────────────────────────────────
    "onb_welcome": "Salam! 👋 Qidalanmanı izləməyə kömək edirəm — foto və ya mətnə görə kalori və makroları hesablayıram.\n\nNəyi izləmək istəyirsiniz?",
    "onb_terms_hint": "Basmaqla [istifadə şərtləri](https://mealscan.org/terms.html) ilə razılaşırsınız",
    "btn_onb_goal_lose": "🔻 Arıqlamaq",
    "btn_onb_goal_gain": "🔺 Kökəlmək",
    "btn_onb_goal_maintain": "⚖️ Çəkini saxlamaq",
    "btn_onb_goal_track": "📊 Sadəcə qidalanmanı izləyirəm",
    "onb_ask_sex": "Cinsiyyətinizi göstərin:",
    "onb_ask_age": "Neçə yaşınız var?\n\nRəqəm yazın, məsələn: *28*",
    "onb_ask_weight_height": "Çəki və boyunuz?\n\nİki rəqəm boşluqla yazın, məsələn: *70 175*",
    "onb_weight_height_bad": "Anlamadım 🤔 İki rəqəm boşluqla yazın: çəki və boy\nMəsələn: *70 175*",
    "onb_ask_activity": "Nə qədər tez-tez məşq edirsiniz?",
    "btn_onb_act_sedentary": "🪑 Demək olar ki, məşq etmirəm",
    "btn_onb_act_light": "🚶 Həftədə 1–2 dəfə",
    "btn_onb_act_moderate": "🏃 Həftədə 3–5 dəfə",
    "btn_onb_act_active": "💪 Hər gün",
    "onb_complete": "Əla! 🎉\n\n🔥 Kalori norması: *{low}–{high} kkal/gün*\n🥩 Zülal: *~{protein} q/gün*\n\nİndi istənilən yeməyin fotosu göndərin və ya nə yediyinizi yazın — hamısını hesablayacağam 📸",
    "onb_reminders_prompt": "Yemək haqqında xatırlatmamı istəyirsiniz? ⏰\n\nSəhər, günorta və axşam yazacağam.",
    "btn_onb_reminders_yes": "🔔 Xatırlatmaları qurmaq",
    "btn_onb_reminders_skip": "İndi yox",


    "dst_prompt": "⏰ Həftə sonu bəzi ölkələrdə saatlar dəyişdirildi. Səndə vaxt dəyişdi?",
    "btn_dst_yes": "Bəli, dəyişdi",
    "btn_dst_no": "Xeyr, bizdə dəyişmir",
    "dst_saved": "✅ Hazırdır! İndi səndə {time}. Xatırlatmalar bu vaxta görə gələcək.",
}
