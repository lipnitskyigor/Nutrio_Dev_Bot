texts = {
    # ── Menu buttons ──────────────────────────────────────────────
    "menu_diary": "📔 Dziennik",
    "menu_profile": "👤 Profil",
    "menu_help": "❓ Pomoc",
    "menu_add": "🍽️ Dodaj posiłek",
    "input_placeholder": "Wyślij zdjęcie lub opisz co zjadłeś...",

    # ── Language switching ────────────────────────────────────────
    "choose_language": "Wybierz język:",
    "language_changed_ru": "✅ Язык изменён на русский 🇷🇺",
    "language_changed_en": "✅ Language changed to English 🇬🇧",
    "language_changed_de": "✅ Sprache auf Deutsch geändert 🇩🇪",
    "language_changed_pl": "✅ Język zmieniony na polski 🇵🇱",
    "btn_lang_ru": "🇷🇺 Русский",
    "btn_lang_en": "🇬🇧 English",
    "btn_lang_de": "🇩🇪 Deutsch",
    "btn_lang_pl": "🇵🇱 Polski",

    # ── Claude API instruction ────────────────────────────────────
    "claude_lang": "po polsku",

    # ── Terms ─────────────────────────────────────────────────────
    "terms_greeting": "👋 Cześć, {name}!\n\nZanim zaczniemy, przeczytaj ważne informacje:\n\n⚠️ Meal Scan to asystent do liczenia kalorii i makroskładników.\nTo nie jest aplikacja medyczna. Bot nie zastępuje lekarza,\ndietytyka ani dietetyka.\n\n📄 Warunki użytkowania: mealscan.org/terms.html\n\nNaciskając przycisk poniżej, zgadzasz się z warunkami użytkowania.",
    "btn_accept_terms": "✅ Akceptuję warunki",

    # ── Start / Welcome ───────────────────────────────────────────
    "welcome_back": "Witaj z powrotem, {name}! 👋\n\n📸 Wyślij zdjęcie posiłku lub opisz co zjadłeś — policzę.",
    "welcome_new": "Pomagam śledzić odżywianie — liczę kalorie i makroskładniki ze zdjęć lub tekstu.\n\n📸 *Wyślij zdjęcie dowolnego posiłku*\n✏️ Lub napisz co zjadłeś\n\nSpróbuj teraz ↓\n\n———\nℹ️ Meal Scan to asystent żywieniowy, nie aplikacja medyczna. W razie problemów zdrowotnych lub przed zmianą diety skonsultuj się z lekarzem lub dietetykiem.",
    "default_friend": "przyjacielu",

    # ── Help ──────────────────────────────────────────────────────
    "help_text": (
        "🤖 *Jak korzystać z bota:*\n\n"
        "📸 Wyślij zdjęcie jedzenia — policzę kalorie i makroskładniki\n"
        "✏️ Napisz co zjadłeś — też policzę\n"
        "Na przykład: _«kurczak z ryżem 300g»_\n\n"
        "📊 *Kalorie i odżywianie:*\n"
        "/today — podsumowanie dnia (kalorie, białko, tłuszcz, węglowodany)\n"
        "/history — historia odżywiania z ostatnich 7 dni\n"
        "/goal 2000 150 — ustaw dzienny cel kalorii i białka\n"
        "/goal — sprawdź aktualny cel\n"
        "/reset — usuń dzisiejsze wpisy\n\n"
        "⚖️ *Waga i postęp:*\n"
        "/weight 80.5 — zapisz wagę (rób to codziennie)\n"
        "/weight — sprawdź ostatnio zapisaną wagę\n"
        "/target 75 — ustaw docelową wagę\n"
        "/target — sprawdź docelową wagę i ile zostało\n"
        "/progress — dynamika wagi z 7 dni ze zmianami 🟢🔴\n\n"
        "💡 Wskazówka: im wyraźniej widać jedzenie na zdjęciu, tym dokładniejszy wynik!\n\n"
        "🔔 *Przypomnienia:*\n"
        "/notify — ustaw przypomnienia o posiłkach\n\n"
        "💬 *Pomoc:*\n"
        "/support — skontaktuj się z pomocą"
    ),

    # ── Support ───────────────────────────────────────────────────
    "support_text": "💬 *Meal Scan — Pomoc*\n\nMasz pytanie lub problem — napisz do nas:\n\n👉 @MealScanSupport",

    # ── Today ─────────────────────────────────────────────────────
    "today_empty": "📭 Brak posiłków na dziś.\nWyślij zdjęcie dania, żeby zacząć liczyć!",
    "today_header": "📊 *Podsumowanie dnia — {name}*\n",
    "today_meal_line": "{i}. {food} — {cal} kcal ({time})",
    "today_total_cal": "\n🔥 *Razem: {cal} kcal*",
    "today_macros": "🥩 Białko: {protein} g  🧈 Tłuszcz: {fat} g  🍞 Węglowodany: {carbs} g",
    "today_cal_left": "\n🎯 Do celu: *{cal_left} kcal* i *{prot_left} g białka*",
    "today_cal_done": "\n✅ *Dzienny cel kaloryczny osiągnięty!*",
    "today_cal_over": "\n⚠️ Cel przekroczony o *{over} kcal*",

    # ── History ───────────────────────────────────────────────────
    "history_empty": "📭 Brak danych z ostatnich 7 dni.\nWyślij zdjęcie jedzenia, żeby zacząć!",
    "history_header": "📅 *Historia 7 dni — {name}*\n",
    "history_entry": "📆 {day}: *{cal} kcal* ({n} posiłek{suffix})",
    "history_meals_suffix_1": "",
    "history_meals_suffix_other": "ów",

    # ── Reset ─────────────────────────────────────────────────────
    "reset_done": "🗑️ Dane z dziś usunięte!",

    # ── Goal ──────────────────────────────────────────────────────
    "goal_current": "🎯 *Twój dzienny cel:*\n🔥 Kalorie: {cal} kcal\n🥩 Białko: {protein} g\n\nZmień: `/goal 2000 150`",
    "goal_not_set": "🎯 Brak celu.\n\nUstaw tak: `/goal kalorie białko`\nNp.: `/goal 2000 150`",
    "goal_saved": "✅ *Cel ustawiony!*\n🔥 Kalorie: {cal} kcal/dzień\n🥩 Białko: {protein} g/dzień",
    "goal_bad_format": "❌ Zły format. Użyj: `/goal 2000 150`",

    # ── Weight ────────────────────────────────────────────────────
    "weight_last": "⚖️ *Ostatnia waga:* {weight} kg ({day})\n\nAby zapisać nową: `/weight 80.5`",
    "weight_not_set": "⚖️ Waga jeszcze nie zapisana.\n\nZapisz tak: `/weight 80.5`",
    "weight_saved": "⚖️ *Waga zapisana:* {weight} kg\n",
    "weight_to_goal": "\n🎯 Do celu ({target} kg): pozostało *{diff} kg*\n",
    "weight_almost": "💪 Prawie! Jesteś tak blisko celu!",
    "weight_great_progress": "🔥 Świetny postęp, tak trzymaj!",
    "weight_good_start": "💪 Dobry start! Każdy dzień przybliża cię do celu.",
    "weight_goal_reached": "\n🏆 Cel osiągnięty! Jesteś {diff} kg poniżej docelowej wagi!",
    "weight_on_goal": "\n🎯 Jesteś dokładnie na docelowej wadze! Doskonale!",
    "weight_set_target_hint": "\n💡 Ustaw docelową wagę komendą `/target 75`",
    "weight_bad_format": "❌ Zły format. Użyj: `/weight 80.5`",

    # ── Progress ──────────────────────────────────────────────────
    "progress_empty": "⚖️ Brak danych o wadze.\n\nZapisuj wagę każdego dnia komendą `/weight 80.5` — pokażę ci dynamikę!",
    "progress_header": "📈 *Dynamika wagi:*\n",
    "progress_entry_first": "📅 {day}: *{w} kg*",
    "progress_entry_down": "📅 {day}: *{w} kg* (🟢 {diff} kg)",
    "progress_entry_up": "📅 {day}: *{w} kg* (🔴 +{diff} kg)",
    "progress_entry_same": "📅 {day}: *{w} kg* (➡️ bez zmian)",
    "progress_total_down": "\n📉 W okresie: *{diff} kg* — świetny wynik!",
    "progress_total_up": "\n📈 W okresie: *+{diff} kg*",
    "progress_total_stable": "\n➡️ W okresie: waga stabilna",
    "progress_to_goal": "🎯 Do celu ({target} kg): pozostało *{diff} kg*",
    "progress_goal_reached": "🏆 Cel {target} kg — *osiągnięty!*",

    # ── Target ────────────────────────────────────────────────────
    "target_current": "🎯 *Docelowa waga:* {target} kg\n",
    "target_remaining": "📍 Aktualna waga: {current} kg — pozostało *{diff} kg*",
    "target_reached": "🏆 Aktualna waga: {current} kg — cel osiągnięty!",
    "target_change_hint": "\n\nZmień: `/target 70`",
    "target_not_set": "🎯 Docelowa waga nie ustawiona.\n\nUstaw tak: `/target 75`",
    "target_bad_format": "❌ Zły format. Użyj: `/target 75`",
    "target_need_profile": "📋 Do sprawdzenia bezpieczeństwa celu potrzebny jest profil (wzrost, wiek, płeć, aktywność).\n\nSkonfiguruj profil — sprawdzę czy cel jest bezpieczny.",
    "btn_setup_profile": "👉 Skonfiguruj profil",
    "target_safe_set": "✅ *Cel ustawiony: {target} kg*\n\n📊 Zalecane kalorie: *{cal} kcal/dzień*\n",
    "target_min_cal_warn": "⚠️ _Minimalne bezpieczne kalorie: {min_cal} kcal/dzień_\n",
    "target_weeks": "⏱ Szacowany czas: *{weeks} tygodni*",
    "target_warn_low_bmi": "⚠️ Docelowa waga *{target} kg* daje BMI *{bmi}* — poniżej normy.\nMinimalna zalecana waga dla twojego wzrostu: *{min_weight} kg*.\n\nSkonsultuj się ze specjalistą przed rozpoczęciem.",
    "target_danger_bmi": "🚨 Docelowa waga *{target} kg* — BMI *{bmi}*, niebezpiecznie niska wartość.\nZalecane minimum dla wzrostu {height} cm: *{min_weight} kg*.\n\nStanowczo zalecamy konsultację z lekarzem.",
    "target_critical_bmi": "❌ Nie można ustawić celu *{target} kg*.\nBMI *{bmi}* jest krytycznie niskie i zagraża życiu.\n\nMinimalna bezpieczna waga dla twojego wzrostu: *{min_weight} kg*.\nProszę, skontaktuj się z lekarzem lub dietetykiem.",
    "btn_target_confirm": "✅ Ustaw mimo to",
    "btn_target_confirm_warn": "⚠️ Ustaw mimo to (niezalecane)",
    "btn_target_change": "✏️ Zmień cel",
    "target_confirmed_msg": "✅ Docelowa waga *{target} kg* ustawiona.\n\n⚠️ Pamiętaj o zaleceniu konsultacji ze specjalistą.",
    "target_change_prompt": "Podaj nową docelową wagę: `/target 70`",

    # ── Meal analysis ─────────────────────────────────────────────
    "analyzing_photo": "🔍 Analizuję zdjęcie...",
    "counting_calories": "🔍 Liczę kalorie...",
    "recalculating": "🔍 Przeliczam...",
    "analysis_error_parse": "😔 Nie udało się przetworzyć odpowiedzi. Spróbuj ponownie lub zrób wyraźniejsze zdjęcie.",
    "analysis_error_photo": "😔 Błąd podczas analizy zdjęcia. Spróbuj ponownie!",
    "analysis_error_text": "😔 Nie zrozumiałem. Spróbuj opisać dokładniej!",
    "analysis_error_generic": "😔 Wystąpił błąd. Spróbuj ponownie!",
    "correction_error": "😔 Nie udało się przeliczyć. Opisz dokładniej!",
    "corrected_prefix": "✅ *Poprawiono!*\n\n",

    # ── Meal summary ──────────────────────────────────────────────
    "meal_summary_header": "🍽️ *{food}*\n\n🔥 *{cal} kcal*\n🥩 Białko: *{protein} g*\n🧈 Tłuszcz: {fat} g\n🍞 Węglowodany: {carbs} g\n\n💬 _{comment}_\n\n📊 *Podsumowanie dnia:*\n🔥 {total_cal} kcal (~{day_pct}% normy)  🥩 białko: *{total_protein} g*",
    "meal_remaining_profile": "\n\n🎯 Do celu: *~{cal_left} kcal* i *~{prot_left} g białka*\n_(cel: {cal_low}–{cal_high} kcal/dzień)_",
    "meal_on_target_profile": "\n\n✅ W normie! ({cal_low}–{cal_high} kcal/dzień)",
    "meal_over_target_profile": "\n\n⚠️ Powyżej celu o ~*{over} kcal*",
    "meal_remaining_default": "\n\n🎯 Do średniej normy: *~{cal_left} kcal* i *~{prot_left} g białka*",
    "meal_on_target_default": "\n\n✅ Średnia norma osiągnięta!",
    "meal_over_target_default": "\n\n⚠️ Powyżej średniej normy o *{over} kcal*",

    # ── Meal keyboard ─────────────────────────────────────────────
    "btn_meal_confirm": "✅ Poprawnie",
    "btn_meal_edit": "✏️ Edytuj",
    "btn_meal_delete": "🗑️ Usuń",
    "edit_prompt": "✏️ Napisz korektę — przeliczę:",
    "quick_add_prompt": "📸 Wyślij zdjęcie posiłku lub napisz co zjadłeś — policzę!",
    "menu_add_prompt": "📸 Wyślij zdjęcie posiłku lub napisz co zjadłeś — policzę!",

    # ── Short input hint ──────────────────────────────────────────
    "short_input_hint": "📸 Wyślij zdjęcie jedzenia lub napisz co zjadłeś — policzę kalorie!\n\nNa przykład: *«talerz zupy i chleb»* lub *«2 jajka, kawa z mlekiem»*",

    # ── Profile ───────────────────────────────────────────────────
    "profile_not_set": "📋 *Profil nie skonfigurowany*\n\nWypełnij profil — będę dokładniej liczyć twoją normę kalorii i postęp.",
    "btn_edit_profile": "✏️ Edytuj profil",
    "profile_goal_lose": "Schudnąć 🥦",
    "profile_goal_maintain": "Utrzymać wagę ⚖️",
    "profile_goal_gain": "Zbudować masę 💪",
    "profile_activity_sedentary": "Siedzący 🪑",
    "profile_activity_light": "Lekka 🚶",
    "profile_activity_moderate": "Umiarkowana 🏃",
    "profile_activity_active": "Wysoka 💪",
    "profile_view": "👤 *Twój profil*\n\n🎯 Cel: {goal}\n⚡ Aktywność: {activity}\n📏 Wzrost: {height} cm\n⚖️ Waga: {weight} kg\n",
    "profile_last_weight": "📅 Ostatnia waga: *{w} kg* ({day})\n",
    "profile_weight_goal_reached": "🏁 Cel wagowy: *{target} kg* — osiągnięty! 🎉\n",
    "profile_weight_to_goal": "🏁 Do celu ({target} kg): *{diff} kg*\n",
    "profile_norm": "\n🔥 Norma: *{low}–{high} kcal/dzień*\n🥩 Białko: *{protein} g/dzień*\n📊 Zjedzone dziś: *{today_cal} kcal*",

    # ── Onboarding / Profile flow ─────────────────────────────────
    "profile_prompt_title": "📊 *Skonfigurujmy kalorie pod ciebie i twój cel*\n\nOdpowiedz na 4 pytania — obliczenia będą dokładniejsze\nZajmie mniej niż 30 sekund",
    "btn_profile_yes": "👉 Tak, zaczynamy",
    "btn_profile_skip": "Pomiń",
    "ask_goal": "Jaki masz cel?",
    "ask_sex": "Twoja płeć?",
    "ask_activity": "Twój styl życia?",
    "ask_age": "Ile masz lat?\n\nWpisz liczbę, np.: *28*",
    "ask_height": "Twój wzrost?\n\nWpisz w centymetrach, np.: *178*",
    "ask_weight": "Twoja aktualna waga?\n\nWpisz w kilogramach, np.: *75*",
    "ask_target_weight": "Masz docelową wagę?",
    "btn_set_target_yes": "✏️ Tak, podam",
    "btn_skip": "Pomiń",
    "ask_target_weight_enter": "Wpisz docelową wagę w kg, np.: *70*",
    "age_bad": "Wpisz wiek jako liczbę, np.: *28*",
    "height_bad": "Wpisz wzrost jako liczbę w cm, np.: *178*",
    "weight_bad": "Wpisz wagę jako liczbę w kg, np.: *75*",
    "target_weight_bad": "Wpisz wagę jako liczbę w kg, np.: *70*",
    "target_weight_critical_onb": "❌ Docelowa waga *{target} kg* — BMI *{bmi}*, krytycznie niebezpieczna.\nMinimalna bezpieczna waga dla wzrostu {height} cm: *{min_weight} kg*.\n\nWpisz inną docelową wagę:",
    "btn_target_confirm_onb": "✅ Ustaw mimo to",
    "btn_target_change_onb": "✏️ Zmień cel",
    "target_change_onb_prompt": "Wpisz inną docelową wagę w kg, np.: *70*",

    # goal labels (used in _finish_profile)
    "goal_label_lose": "Schudnąć",
    "goal_label_maintain": "Utrzymać wagę",
    "goal_label_gain": "Zbudować masę",

    # ── Profile goal buttons ──────────────────────────────────────
    "btn_goal_lose": "📉 Schudnąć",
    "btn_goal_maintain": "⚖️ Utrzymać wagę",
    "btn_goal_gain": "📈 Zbudować masę",
    "btn_sex_male": "👨 Mężczyzna",
    "btn_sex_female": "👩 Kobieta",
    "btn_activity_sedentary": "🪑 Siedzący (biuro, bez sportu)",
    "btn_activity_light": "🚶 Lekka aktywność (1–2 razy w tygodniu)",
    "btn_activity_moderate": "🏃 Umiarkowana (3–5 razy w tygodniu)",
    "btn_activity_active": "💪 Wysoka (codziennie)",

    # ── Finish profile ────────────────────────────────────────────
    "profile_done": "✅ *Gotowe!*\n\n🎯 Cel: *{goal}*\n🔥 Kalorie: *{low}–{high} kcal/dzień*\n🥩 Białko: *~{protein} g/dzień*{target_line}\n\nPo każdym posiłku pokażę ile kalorii jeszcze zostało 🎯",
    "profile_target_line_remaining": "\n⚖️ Docelowa waga: *{target} kg* (~{diff} kg do celu)",
    "profile_target_line_reached": "\n⚖️ Docelowa waga: *{target} kg* — już osiągnięta! 🏆",
    "ask_timezone": "🔔 *Ustawmy przypomnienia o posiłkach!*\n\nBędę ci przypominać o logowaniu jedzenia — wyślij zdjęcie lub napisz co zjadłeś.\n\nKtóra jest teraz u ciebie godzina? np.: *23:15*",

    # ── Notifications ─────────────────────────────────────────────
    "notify_header": "⏰ *Ustawienia przypomnień*\n\n🌍 Strefa czasowa: {tz} (teraz {time})\n\n☕ Śniadanie — {b_time} ({b})\n🍲 Obiad — {l_time} ({l})\n🍽️ Kolacja — {d_time} ({d})\n\n⚠️ Zalecamy pozostawienie co najmniej 1 przypomnienia włączonego",
    "btn_notif_all_on": "✅ Włącz wszystkie",
    "btn_notif_all_off": "❌ Wyłącz wszystkie",
    "btn_notif_change_tz": "🌍 Zmień strefę czasową",
    "notif_enabled": "✅",
    "notif_disabled": "❌",
    "notif_breakfast": "☕ Śniadanie",
    "notif_lunch": "🍲 Obiad",
    "notif_dinner": "🍽️ Kolacja",
    "notif_time_prompt": "⏰ Wpisz nowy czas przypomnienia dla *{meal}*\n\nFormat: *GG:MM*, np.: *08:30*",
    "notif_timezone_prompt": "🕐 Wpisz która jest teraz godzina, np.: *23:15*\n\nOkreślę strefę czasową automatycznie.",
    "notif_timezone_updated": "✅ Strefa czasowa zaktualizowana: UTC{sign}{offset}\n\n",
    "notif_time_updated": "✅ Czas przypomnienia ({meal}) zaktualizowany: *{time}*\n\n",
    "notif_time_bad": "❌ Nie rozumiem czasu. Wpisz w formacie *GG:MM*, np.: *08:30*",
    "timezone_bad": "Nie rozumiem 🤔 Wpisz czas w formacie *GG:MM*, np.: *23:15*",
    "meal_name_breakfast": "śniadanie",
    "meal_name_lunch": "obiad",
    "meal_name_dinner": "kolacja",
    "notif_tz_saved": "🔔 *Przypomnienia włączone!*\n\n🌍 Strefa czasowa: {tz}\n☕ Śniadanie — 9:00\n🍲 Obiad — 13:00\n🍽️ Kolacja — 19:00\n\nSkonfiguruj: /notify",
    "onb_tz_saved": "🔔 *Przypomnienia włączone!*\n\n🌍 Strefa czasowa: {tz}\n☕ Śniadanie — 9:00\n🍲 Obiad — 13:00\n🍽️ Kolacja — 19:00\n\nSkonfiguruj: /notify",
    "onb_tz_skip": "OK, bez przypomnień 👌\nWłącz w dowolnej chwili: /notify",
    "notif_snooze_done": "✅ Przypomnienie o {meal} wyłączone.\nWłącz ponownie: /notify",

    # ── Timezone city names ───────────────────────────────────────
    "tz_kyiv": "🇺🇦 Kijów",
    "tz_moscow": "🇷🇺 Moskwa",
    "tz_baku": "🇦🇿 Baku",
    "tz_almaty": "🇰🇿 Ałmaty",
    "tz_tashkent": "🇺🇿 Taszkent",
    "tz_novosibirsk": "Nowosybirsk",
    "tz_irkutsk": "Irkuck",
    "tz_vladivostok": "Władywostok",
    "tz_skip": "❌ Pomiń",

    # ── Trial / Paywall ───────────────────────────────────────────
    "trial_exhausted": "❌ *Darmowe analizy wyczerpane* (15 z 15)\n\nKup subskrypcję, żeby dalej liczyć kalorie 👇",
    "trial_last_1": "⚠️ Pozostała *1 darmowa analiza* z {limit} → /subscribe",
    "trial_last_few": "⚠️ Pozostały *{left} darmowe analizy* z {limit} → /subscribe",
    "trial_some_left": "🎁 Pozostało {left} darmowych analiz z {limit} → /subscribe",
    "trial_many_left": "🎁 Darmowe analizy: {left} z {limit}",
    "btn_subscribe": "💳 Subskrybuj",
    "subscribe_remaining": "🎁 Pozostałe darmowe analizy: *{left} z {limit}*\n\n",
    "subscribe_exhausted": "❌ Darmowe analizy wyczerpane\n\n",
    "subscribe_header": "💳 *Subskrypcja Meal Scan*\n\nWybierz plan:",
    "subscribe_header_full": "💳 *Subskrypcja Meal Scan*\n\nNieograniczone liczenie kalorii ze zdjęć i tekstu\n\nWybierz plan:",
    "subscribe_active": "✅ *Subskrypcja aktywna do {expires}*\n\nMożesz odnowić wcześniej — czas zostanie dodany do aktualnego okresu:",
    "payment_success": "🎉 *Subskrypcja aktywowana na {label}!*\n\nLicz kalorie bez ograniczeń 🍽️\nWyślij zdjęcie lub napisz co zjadłeś ↓",
    "sub_1m_label": "1 miesiąc",
    "sub_3m_label": "3 miesiące",
    "sub_invoice_title_1m": "Subskrypcja Meal Scan — 1 miesiąc",
    "sub_invoice_title_3m": "Subskrypcja Meal Scan — 3 miesiące",
    "sub_invoice_desc": "Nieograniczone liczenie kalorii i makroskładników ze zdjęć i tekstu",
    "sub_invoice_error": "❌ Błąd podczas tworzenia faktury: {e}",

    # ── Delete command ────────────────────────────────────────────
    "delete_no_num": "❌ Podaj numer posiłku.\nPrzykład: `/delete 2`\n\nDzisiejsza lista: /today",
    "delete_bad_num": "❌ Numer musi być liczbą całkowitą. Na przykład: `/delete 2`",
    "delete_no_meals": "📭 Brak dzisiejszych wpisów o jedzeniu.",
    "delete_out_of_range": "❌ Brak posiłku #{num}. Dzisiejsze wpisy: {total}.\n\nPokaż listę: /today",
    "delete_done": "🗑️ Usunięto: *{food}* ({cal} kcal)\n\n📊 Pozostało dziś: *{total_cal} kcal* ({n} posiłków)",

    # ── Edit command ──────────────────────────────────────────────
    "edit_no_args": "✏️ Format: `/edit numer nowy opis`\nPrzykład: `/edit 2 barszcz wołowy 400g`\n\nDzisiejsza lista: /today",
    "edit_bad_num": "❌ Najpierw podaj numer. Na przykład: `/edit 2 zupa 400g`",
    "edit_no_meals": "📭 Brak dzisiejszych wpisów o jedzeniu.",
    "edit_out_of_range": "❌ Brak posiłku #{num}. Dzisiejsze wpisy: {total}.",
    "edit_done": "✅ *Posiłek #{num} zaktualizowany*\n\n🍽️ {food}\n🔥 {cal} kcal | 🥩 {protein} g | 🧈 {fat} g | 🍞 {carbs} g\n\n📊 Dziś: *{total_cal} kcal* / 🥩 *{total_protein} g białka*",

    # ── Delete from diary (callback) ──────────────────────────────
    "diary_deleted": "🗑️ Wpis usunięty.\n\n📊 Zjedzone dziś: *{cal} kcal* / 🥩 *{protein} g białka* ({n} posiłków)\n{remaining}",
    "diary_cal_left": "🎯 Do celu: *{cal_left} kcal* i *{prot_left} g białka*",
    "diary_cal_done": "✅ Dzienny cel kaloryczny osiągnięty!",
    "diary_cal_over": "⚠️ Cel przekroczony o *{over} kcal*",

    # ── Reminders ─────────────────────────────────────────────────
    "reminder_text": "{emoji} Nie zapomnij powiedzieć mi co zjadłeś na {meal}!\nCel: {goal_cal} kcal. Dziś: {total_cal} kcal\n\n📸 Wyślij zdjęcie lub napisz tekstem",
    "btn_reminder_add": "🍽️ Dodaj posiłek",
    "btn_reminder_snooze": "❌ Nie przypominaj o {meal}",

    # ── Weight tip ────────────────────────────────────────────────
    "weight_tip": "⚖️ *Wskazówka: śledź wagę*\n\nMożesz zapisywać wagę każdego ranka — bot pokaże dynamikę i postęp do celu.\n\nWpisz komendę /weight i podaj aktualną wagę.\nWykres postępu: /progress",

    # ── Admin ─────────────────────────────────────────────────────
    "resetme_done": "✅ Wszystkie dane usunięte. Wpisz /start żeby zacząć od nowa.",
    "gift_usage": "Użycie: /gift <user_id>",
    "gift_bad_id": "❌ user_id musi być liczbą",
    "gift_done": "✅ Użytkownik {uid} otrzymał stały dostęp.",
    "error_terms": "❌ Błąd: {e}",
    "error_invoice": "❌ Błąd podczas tworzenia faktury: {e}",
}
