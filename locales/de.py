texts = {
    # ── Menu buttons ──────────────────────────────────────────────
    "menu_diary": "📔 Tagebuch",
    "menu_profile": "👤 Profil",
    "menu_help": "❓ Hilfe",
    "menu_add": "🍽️ Mahlzeit hinzufügen",
    "input_placeholder": "Foto senden oder Mahlzeit beschreiben...",

    # ── Language switching ────────────────────────────────────────
    "choose_language": "Sprache wählen:",
    "language_changed_ru": "✅ Язык изменён на русский 🇷🇺",
    "language_changed_en": "✅ Language changed to English 🇬🇧",
    "language_changed_de": "✅ Sprache auf Deutsch geändert 🇩🇪",
    "language_changed_pl": "✅ Język zmieniony na polski 🇵🇱",
    "language_changed_uk": "✅ Мову змінено на українську 🇺🇦",
    "language_changed_be": "✅ Мова зменена на беларускую 🇧🇾",
    "btn_lang_ru": "🇷🇺 Русский",
    "btn_lang_en": "🇬🇧 English",
    "btn_lang_uk": "🇺🇦 Українська",
    "btn_lang_be": "🇧🇾 Беларуская",
    "btn_lang_de": "🇩🇪 Deutsch",
    "btn_lang_pl": "🇵🇱 Polski",

    # ── Claude API instruction ────────────────────────────────────
    "claude_lang": "auf Deutsch",

    # ── Terms ─────────────────────────────────────────────────────
    "terms_greeting": "👋 Hallo, {name}!\n\nBitte lies folgendes, bevor wir starten:\n\n⚠️ Meal Scan ist ein Assistent zur Kalorien- und Nährstoffverfolgung.\nDies ist keine medizinische App. Der Bot ersetzt keinen Arzt,\nDiätassistenten oder Ernährungsberater.\n\n📄 Nutzungsbedingungen: mealscan.org/terms.html\n\nMit dem Tippen der Schaltfläche stimmst du den Nutzungsbedingungen zu.",
    "btn_accept_terms": "✅ Bedingungen akzeptieren",

    # ── Start / Welcome ───────────────────────────────────────────
    "welcome_back": "Willkommen zurück, {name}! 👋\n\n📸 Sende ein Foto deiner Mahlzeit oder beschreibe, was du gegessen hast — ich berechne es.",
    "welcome_new": "Ich helfe dir, deine Ernährung zu verfolgen — ich zähle Kalorien und Makros aus Fotos oder Text.\n\n📸 *Sende ein Foto einer Mahlzeit*\n✏️ Oder schreibe, was du gegessen hast\n\nProbier es gleich aus ↓\n\n———\nℹ️ Meal Scan ist ein Ernährungs-Assistent, keine medizinische App. Bei gesundheitlichen Problemen bitte einen Arzt oder Ernährungsberater konsultieren.",
    "default_friend": "Freund",

    # ── Help ──────────────────────────────────────────────────────
    "help_text": (
        "🤖 *So nutzt du den Bot:*\n\n"
        "📸 Foto senden — ich zähle Kalorien und Makros\n"
        "✏️ Mahlzeit beschreiben — das zähle ich auch\n"
        "Zum Beispiel: _«Hähnchen mit Reis 300g»_\n\n"
        "📊 *Kalorien & Ernährung:*\n"
        "/today — heutige Zusammenfassung (Kalorien, Eiweiß, Fett, Kohlenhydrate)\n"
        "/history — Ernährungsverlauf der letzten 7 Tage\n"
        "/goal 2000 150 — Tagesziel für Kalorien & Eiweiß setzen\n"
        "/goal — aktuelles Ziel anzeigen\n"
        "/reset — heutige Einträge löschen\n\n"
        "⚖️ *Gewicht & Fortschritt:*\n"
        "/weight 80.5 — Gewicht erfassen (täglich)\n"
        "/weight — letztes erfasstes Gewicht anzeigen\n"
        "/target 75 — Zielgewicht setzen\n"
        "/target — Zielgewicht und Restweg anzeigen\n"
        "/progress — Gewichtsverlauf 7 Tage mit 🟢🔴 Änderungen\n\n"
        "💡 Tipp: Je klarer das Essen auf dem Foto, desto genauer das Ergebnis!\n\n"
        "🔔 *Erinnerungen:*\n"
        "/notify — Mahlzeit-Erinnerungen einstellen\n\n"
        "💬 *Support:*\n"
        "/support — Support kontaktieren"
    ),

    # ── Support ───────────────────────────────────────────────────
    "support_text": "💬 *Meal Scan Support*\n\nFragen oder Probleme:\n\n👉 @Meal_Scan_Support",

    # ── Today ─────────────────────────────────────────────────────
    "today_empty": "📭 Heute noch keine Mahlzeiten erfasst.\nSende ein Foto, um zu beginnen!",
    "today_header": "📊 *Heutige Zusammenfassung — {name}*\n",
    "today_meal_line": "{i}. {food} — {cal} kcal ({time})",
    "today_total_cal": "\n🔥 *Gesamt: {cal} kcal*",
    "today_macros": "🥩 Eiweiß: {protein} g  🧈 Fett: {fat} g  🍞 Kohlenhydrate: {carbs} g",
    "today_cal_left": "\n🎯 Noch bis zum Ziel: *{cal_left} kcal* und *{prot_left} g Eiweiß*",
    "today_cal_done": "\n✅ *Tägliches Kalorienziel erreicht!*",
    "today_cal_over": "\n⚠️ Ziel überschritten um *{over} kcal*",

    # ── History ───────────────────────────────────────────────────
    "history_empty": "📭 Keine Daten der letzten 7 Tage.\nSende ein Foto, um zu beginnen!",
    "history_header": "📅 *7-Tage-Verlauf — {name}*\n",
    "history_entry": "📆 {day}: *{cal} kcal* ({n} Mahlzeit{suffix})",
    "history_meals_suffix_1": "",
    "history_meals_suffix_other": "en",

    # ── Reset ─────────────────────────────────────────────────────
    "reset_done": "🗑️ Heutige Daten gelöscht!",

    # ── Goal ──────────────────────────────────────────────────────
    "goal_current": "🎯 *Dein Tagesziel:*\n🔥 Kalorien: {cal} kcal\n🥩 Eiweiß: {protein} g\n\nÄndern: `/goal 2000 150`",
    "goal_not_set": "🎯 Kein Ziel gesetzt.\n\nSo festlegen: `/goal Kalorien Eiweiß`\nBeispiel: `/goal 2000 150`",
    "goal_saved": "✅ *Ziel gesetzt!*\n🔥 Kalorien: {cal} kcal/Tag\n🥩 Eiweiß: {protein} g/Tag",
    "goal_bad_format": "❌ Falsches Format. Verwende: `/goal 2000 150`",

    # ── Weight ────────────────────────────────────────────────────
    "weight_last": "⚖️ *Letztes Gewicht:* {weight} kg ({day})\n\nNeues erfassen: `/weight 80.5`",
    "weight_not_set": "⚖️ Noch kein Gewicht erfasst.\n\nSo erfassen: `/weight 80.5`",
    "weight_saved": "⚖️ *Gewicht erfasst:* {weight} kg\n",
    "weight_to_goal": "\n🎯 Zum Ziel ({target} kg): noch *{diff} kg*\n",
    "weight_almost": "💪 Fast geschafft! Du bist so nah am Ziel!",
    "weight_great_progress": "🔥 Großartiger Fortschritt, weiter so!",
    "weight_good_start": "💪 Guter Start! Jeden Tag kommst du deinem Ziel näher.",
    "weight_goal_reached": "\n🏆 Ziel erreicht! Du bist {diff} kg unter deinem Zielgewicht!",
    "weight_on_goal": "\n🎯 Du bist genau auf deinem Zielgewicht! Ausgezeichnet!",
    "weight_set_target_hint": "\n💡 Zielgewicht mit `/target 75` festlegen",
    "weight_bad_format": "❌ Falsches Format. Verwende: `/weight 80.5`",

    # ── Progress ──────────────────────────────────────────────────
    "progress_empty": "⚖️ Keine Gewichtsdaten.\n\nErfasse dein Gewicht täglich mit `/weight 80.5` — ich zeige dir den Verlauf!",
    "progress_header": "📈 *Gewichtsverlauf:*\n",
    "progress_entry_first": "📅 {day}: *{w} kg*",
    "progress_entry_down": "📅 {day}: *{w} kg* (🟢 {diff} kg)",
    "progress_entry_up": "📅 {day}: *{w} kg* (🔴 +{diff} kg)",
    "progress_entry_same": "📅 {day}: *{w} kg* (➡️ keine Änderung)",
    "progress_total_down": "\n📉 Im Zeitraum: *{diff} kg* — tolles Ergebnis!",
    "progress_total_up": "\n📈 Im Zeitraum: *+{diff} kg*",
    "progress_total_stable": "\n➡️ Im Zeitraum: Gewicht stabil",
    "progress_to_goal": "🎯 Zum Ziel ({target} kg): noch *{diff} kg*",
    "progress_goal_reached": "🏆 Ziel {target} kg — *erreicht!*",

    # ── Target ────────────────────────────────────────────────────
    "target_current": "🎯 *Zielgewicht:* {target} kg\n",
    "target_remaining": "📍 Aktuelles Gewicht: {current} kg — noch *{diff} kg*",
    "target_reached": "🏆 Aktuelles Gewicht: {current} kg — Ziel erreicht!",
    "target_change_hint": "\n\nÄndern: `/target 70`",
    "target_not_set": "🎯 Kein Zielgewicht gesetzt.\n\nSo festlegen: `/target 75`",
    "target_bad_format": "❌ Falsches Format. Verwende: `/target 75`",
    "target_need_profile": "📋 Zur Sicherheitsprüfung des Ziels wird ein Profil benötigt (Größe, Alter, Geschlecht, Aktivität).\n\nProfil einrichten — dann prüfe ich die Sicherheit deines Ziels.",
    "btn_setup_profile": "👉 Profil einrichten",
    "target_safe_set": "✅ *Ziel gesetzt: {target} kg*\n\n📊 Empfohlene Kalorien: *{cal} kcal/Tag*\n",
    "target_min_cal_warn": "⚠️ _Mindest-Kalorienbedarf: {min_cal} kcal/Tag_\n",
    "target_weeks": "⏱ Geschätzte Zeit: *{weeks} Wochen*",
    "target_warn_low_bmi": "⚠️ Zielgewicht *{target} kg* ergibt einen BMI von *{bmi}* — unter dem Normalbereich.\nMindestempfohlenes Gewicht für deine Größe: *{min_weight} kg*.\n\nBitte konsultiere vor Beginn einen Spezialisten.",
    "target_danger_bmi": "🚨 Zielgewicht *{target} kg* — BMI *{bmi}*, gefährlich niedrig.\nEmpfohlenes Minimum für {height} cm: *{min_weight} kg*.\n\nWir empfehlen dringend, einen Arzt aufzusuchen.",
    "target_critical_bmi": "❌ Ziel *{target} kg* kann nicht gesetzt werden.\nBMI *{bmi}* ist kritisch niedrig und lebensbedrohlich.\n\nMindestgewicht für deine Größe: *{min_weight} kg*.\nBitte wende dich an einen Arzt oder Ernährungsberater.",
    "btn_target_confirm": "✅ Trotzdem setzen",
    "btn_target_confirm_warn": "⚠️ Trotzdem setzen (nicht empfohlen)",
    "btn_target_change": "✏️ Ziel ändern",
    "target_confirmed_msg": "✅ Zielgewicht *{target} kg* gesetzt.\n\n⚠️ Denke an die Empfehlung, einen Spezialisten zu konsultieren.",
    "target_change_prompt": "Neues Zielgewicht eingeben: `/target 70`",

    # ── Meal analysis ─────────────────────────────────────────────
    "analyzing_photo": "🔍 Foto wird analysiert...",
    "counting_calories": "🔍 Kalorien werden berechnet...",
    "recalculating": "🔍 Neu berechnen...",
    "analysis_error_parse": "😔 Antwort konnte nicht verarbeitet werden. Bitte erneut versuchen oder ein klareres Foto machen.",
    "analysis_error_photo": "😔 Fehler bei der Fotoanalyse. Bitte erneut versuchen!",
    "analysis_error_text": "😔 Konnte nicht verstehen. Bitte genauer beschreiben!",
    "analysis_error_generic": "😔 Ein Fehler ist aufgetreten. Bitte erneut versuchen!",
    "correction_error": "😔 Neuberechnung fehlgeschlagen. Bitte genauer beschreiben!",
    "corrected_prefix": "✅ *Korrigiert!*\n\n",

    # ── Meal summary ──────────────────────────────────────────────
    "meal_summary_header": "🍽️ *{food}*\n\n🔥 *{cal} kcal*\n🥩 Eiweiß: *{protein} g*\n🧈 Fett: {fat} g\n🍞 Kohlenhydrate: {carbs} g\n\n💬 _{comment}_\n\n📊 *Heutige Zusammenfassung:*\n🔥 {total_cal} kcal (~{day_pct}% der Tagesnorm)  🥩 Eiweiß: *{total_protein} g*",
    "meal_remaining_profile": "\n\n🎯 Noch bis zum Ziel: *~{cal_left} kcal* und *~{prot_left} g Eiweiß*\n_(Ziel: {cal_low}–{cal_high} kcal/Tag)_",
    "meal_on_target_profile": "\n\n✅ Im Zielbereich! ({cal_low}–{cal_high} kcal/Tag)",
    "meal_over_target_profile": "\n\n⚠️ Ziel überschritten um ~*{over} kcal*",
    "meal_remaining_default": "\n\n🎯 Noch bis zur Durchschnittsnorm: *~{cal_left} kcal* und *~{prot_left} g Eiweiß*",
    "meal_on_target_default": "\n\n✅ Durchschnittsnorm erreicht!",
    "meal_over_target_default": "\n\n⚠️ Über der Durchschnittsnorm um *{over} kcal*",

    # ── Meal keyboard ─────────────────────────────────────────────
    "btn_meal_confirm": "✅ Korrekt",
    "btn_meal_edit": "✏️ Bearbeiten",
    "btn_meal_delete": "🗑️ Löschen",
    "edit_prompt": "✏️ Schreibe die Korrektur — ich berechne neu:",
    "quick_add_prompt": "📸 Sende ein Foto oder beschreibe deine Mahlzeit — ich berechne!",
    "menu_add_prompt": "📸 Sende ein Foto oder beschreibe deine Mahlzeit — ich berechne!",

    # ── Short input hint ──────────────────────────────────────────
    "short_input_hint": "📸 Sende ein Foto oder beschreibe deine Mahlzeit — ich zähle die Kalorien!\n\nZum Beispiel: *«Teller Suppe und Brot»* oder *«2 Eier, Kaffee mit Milch»*",

    # ── Profile ───────────────────────────────────────────────────
    "profile_not_set": "📋 *Profil nicht eingerichtet*\n\nFülle dein Profil aus — dann berechne ich deine Kaloriennorm und deinen Fortschritt genauer.",
    "btn_edit_profile": "✏️ Profil bearbeiten",
    "profile_goal_lose": "Abnehmen 🥦",
    "profile_goal_maintain": "Gewicht halten ⚖️",
    "profile_goal_gain": "Muskeln aufbauen 💪",
    "profile_activity_sedentary": "Sitzend 🪑",
    "profile_activity_light": "Leicht 🚶",
    "profile_activity_moderate": "Moderat 🏃",
    "profile_activity_active": "Hoch 💪",
    "profile_view": "👤 *Dein Profil*\n\n🎯 Ziel: {goal}\n⚡ Aktivität: {activity}\n📏 Größe: {height} cm\n⚖️ Gewicht: {weight} kg\n",
    "profile_last_weight": "📅 Letztes Gewicht: *{w} kg* ({day})\n",
    "profile_weight_goal_reached": "🏁 Gewichtsziel: *{target} kg* — erreicht! 🎉\n",
    "profile_weight_to_goal": "🏁 Zum Ziel ({target} kg): *{diff} kg*\n",
    "profile_norm": "\n🔥 Norm: *{low}–{high} kcal/Tag*\n🥩 Eiweiß: *{protein} g/Tag*\n📊 Heute gegessen: *{today_cal} kcal*",

    # ── Onboarding / Profile flow ─────────────────────────────────
    "profile_prompt_title": "📊 *Lass uns Kalorien auf dich und dein Ziel abstimmen*\n\nBeantworte 4 Fragen — und die Berechnung wird genauer\nDauert weniger als 30 Sekunden",
    "btn_profile_yes": "👉 Los geht's",
    "btn_profile_skip": "Überspringen",
    "ask_goal": "Was ist dein Ziel?",
    "ask_sex": "Dein Geschlecht?",
    "ask_activity": "Dein Aktivitätslevel?",
    "ask_age": "Wie alt bist du?\n\nZahl eingeben, z.B.: *28*",
    "ask_height": "Deine Größe?\n\nIn Zentimetern, z.B.: *178*",
    "ask_weight": "Dein aktuelles Gewicht?\n\nIn Kilogramm, z.B.: *75*",
    "ask_target_weight": "Hast du ein Zielgewicht?",
    "btn_set_target_yes": "✏️ Ja, festlegen",
    "btn_skip": "Überspringen",
    "ask_target_weight_enter": "Zielgewicht in kg eingeben, z.B.: *70*",
    "age_bad": "Bitte Alter als Zahl eingeben, z.B.: *28*",
    "height_bad": "Bitte Größe in cm eingeben, z.B.: *178*",
    "weight_bad": "Bitte Gewicht in kg eingeben, z.B.: *75*",
    "target_weight_bad": "Bitte Gewicht in kg eingeben, z.B.: *70*",
    "target_weight_critical_onb": "❌ Zielgewicht *{target} kg* — BMI *{bmi}*, kritisch gefährlich.\nMindestgewicht für {height} cm: *{min_weight} kg*.\n\nBitte anderes Zielgewicht eingeben:",
    "btn_target_confirm_onb": "✅ Trotzdem setzen",
    "btn_target_change_onb": "✏️ Ziel ändern",
    "target_change_onb_prompt": "Anderes Zielgewicht in kg eingeben, z.B.: *70*",

    # goal labels (used in _finish_profile)
    "goal_label_lose": "Abnehmen",
    "goal_label_maintain": "Gewicht halten",
    "goal_label_gain": "Muskeln aufbauen",

    # ── Profile goal buttons ──────────────────────────────────────
    "btn_goal_lose": "📉 Abnehmen",
    "btn_goal_maintain": "⚖️ Gewicht halten",
    "btn_goal_gain": "📈 Muskeln aufbauen",
    "btn_sex_male": "👨 Männlich",
    "btn_sex_female": "👩 Weiblich",
    "btn_activity_sedentary": "🪑 Sitzend (Büro, kein Sport)",
    "btn_activity_light": "🚶 Leichte Aktivität (1–2x pro Woche)",
    "btn_activity_moderate": "🏃 Moderat (3–5x pro Woche)",
    "btn_activity_active": "💪 Hoch (täglich)",

    # ── Finish profile ────────────────────────────────────────────
    "profile_done": "✅ *Alles bereit!*\n\n🎯 Ziel: *{goal}*\n🔥 Kalorien: *{low}–{high} kcal/Tag*\n🥩 Eiweiß: *~{protein} g/Tag*{target_line}\n\nNach jeder Mahlzeit zeige ich, wie viele Kalorien noch übrig sind 🎯",
    "profile_target_line_remaining": "\n⚖️ Zielgewicht: *{target} kg* (~{diff} kg verbleibend)",
    "profile_target_line_reached": "\n⚖️ Zielgewicht: *{target} kg* — bereits erreicht! 🏆",
    "ask_timezone": "🔔 *Mahlzeit-Erinnerungen einrichten!*\n\nIch erinnere dich, deine Mahlzeiten zu erfassen — schick einfach ein Foto oder beschreibe, was du gegessen hast.\n\nWie spät ist es jetzt bei dir? z.B.: *23:15*",

    # ── Notifications ─────────────────────────────────────────────
    "notify_header": "⏰ *Erinnerungseinstellungen*\n\n🌍 Zeitzone: {tz} (jetzt {time})\n\n☕ Frühstück — {b_time} ({b})\n🍲 Mittagessen — {l_time} ({l})\n🍽️ Abendessen — {d_time} ({d})\n\n⚠️ Wir empfehlen, mindestens 1 Erinnerung aktiviert zu lassen",
    "btn_notif_all_on": "✅ Alle aktivieren",
    "btn_notif_all_off": "❌ Alle deaktivieren",
    "btn_notif_change_tz": "🌍 Zeitzone ändern",
    "notif_enabled": "✅",
    "notif_disabled": "❌",
    "notif_breakfast": "☕ Frühstück",
    "notif_lunch": "🍲 Mittagessen",
    "notif_dinner": "🍽️ Abendessen",
    "notif_time_prompt": "⏰ Neue Erinnerungszeit für *{meal}* eingeben\n\nFormat: *HH:MM*, z.B.: *08:30*",
    "notif_timezone_prompt": "🕐 Wie spät ist es jetzt bei dir? z.B.: *23:15*\n\nIch bestimme die Zeitzone automatisch.",
    "notif_timezone_updated": "✅ Zeitzone aktualisiert: UTC{sign}{offset}\n\n",
    "notif_time_updated": "✅ Erinnerungszeit ({meal}) aktualisiert: *{time}*\n\n",
    "notif_time_bad": "❌ Zeit nicht erkannt. Bitte im Format *HH:MM* eingeben, z.B.: *08:30*",
    "timezone_bad": "Nicht verstanden 🤔 Bitte Zeit im Format *HH:MM* eingeben, z.B.: *23:15*",
    "meal_name_breakfast": "Frühstück",
    "meal_name_lunch": "Mittagessen",
    "meal_name_dinner": "Abendessen",
    "notif_tz_saved": "🔔 *Erinnerungen aktiviert!*\n\n🌍 Zeitzone: {tz}\n☕ Frühstück — 9:00\n🍲 Mittagessen — 13:00\n🍽️ Abendessen — 19:00\n\nEinstellen: /notify",
    "onb_tz_saved": "🔔 *Erinnerungen aktiviert!*\n\n🌍 Zeitzone: {tz}\n☕ Frühstück — 9:00\n🍲 Mittagessen — 13:00\n🍽️ Abendessen — 19:00\n\nEinstellen: /notify",
    "onb_tz_skip": "OK, keine Erinnerungen 👌\nJederzeit aktivieren: /notify",
    "notif_snooze_done": "✅ Erinnerung für {meal} deaktiviert.\nWieder aktivieren: /notify",

    # ── Timezone city names ───────────────────────────────────────
    "tz_kyiv": "🇺🇦 Kiew",
    "tz_moscow": "🇷🇺 Moskau",
    "tz_baku": "🇦🇿 Baku",
    "tz_almaty": "🇰🇿 Almaty",
    "tz_tashkent": "🇺🇿 Taschkent",
    "tz_novosibirsk": "Nowosibirsk",
    "tz_irkutsk": "Irkutsk",
    "tz_vladivostok": "Wladiwostok",
    "tz_skip": "❌ Überspringen",

    # ── Trial / Paywall ───────────────────────────────────────────
    "trial_exhausted": "❌ *Kostenlose Analysen aufgebraucht* (15 von 15)\n\nAbonniere, um weiter Kalorien zu zählen 👇",
    "trial_last_1": "⚠️ Noch *1 kostenlose Analyse* von {limit} → /subscribe",
    "trial_last_few": "⚠️ Noch *{left} kostenlose Analysen* von {limit} → /subscribe",
    "trial_some_left": "🎁 {left} kostenlose Analysen übrig von {limit} → /subscribe",
    "trial_many_left": "🎁 Kostenlose Analysen: {left} von {limit}",
    "btn_subscribe": "💳 Abonnieren",
    "subscribe_remaining": "🎁 Kostenlose Analysen übrig: *{left} von {limit}*\n\n",
    "subscribe_exhausted": "❌ Kostenlose Analysen aufgebraucht\n\n",
    "subscribe_header": "💳 *Meal Scan Abonnement*\n\nTarif wählen:",
    "subscribe_header_full": "💳 *Meal Scan Abonnement*\n\nUnbegrenzte Kalorienzählung aus Fotos und Text\n\nTarif wählen:",
    "subscribe_active": "✅ *Abonnement aktiv bis {expires}*\n\nDu kannst es vorzeitig verlängern — die Zeit wird zum aktuellen Zeitraum addiert:",
    "payment_success": "🎉 *Abonnement für {label} aktiviert!*\n\nKalorien unbegrenzt zählen 🍽️\nFoto senden oder Mahlzeit beschreiben ↓",
    "sub_1m_label": "1 Monat",
    "sub_3m_label": "3 Monate",
    "sub_invoice_title_1m": "Meal Scan Abonnement — 1 Monat",
    "sub_invoice_title_3m": "Meal Scan Abonnement — 3 Monate",
    "sub_invoice_desc": "Unbegrenzte Kalorien- und Makrozählung aus Fotos und Text",
    "sub_invoice_error": "❌ Fehler beim Erstellen der Rechnung: {e}",

    # ── Delete command ────────────────────────────────────────────
    "delete_no_num": "❌ Mahlzeitnummer angeben.\nBeispiel: `/delete 2`\n\nHeutige Liste: /today",
    "delete_bad_num": "❌ Die Nummer muss eine ganze Zahl sein. Zum Beispiel: `/delete 2`",
    "delete_no_meals": "📭 Heute keine Mahlzeiten erfasst.",
    "delete_out_of_range": "❌ Keine Mahlzeit #{num}. Heutige Einträge: {total}.\n\nListe anzeigen: /today",
    "delete_done": "🗑️ Gelöscht: *{food}* ({cal} kcal)\n\n📊 Heute verbleibend: *{total_cal} kcal* ({n} Mahlzeiten)",

    # ── Edit command ──────────────────────────────────────────────
    "edit_no_args": "✏️ Format: `/edit Nummer neue Beschreibung`\nBeispiel: `/edit 2 Rindfleisch-Borschtsch 400g`\n\nHeutige Liste: /today",
    "edit_bad_num": "❌ Zuerst Nummer angeben. Zum Beispiel: `/edit 2 Suppe 400g`",
    "edit_no_meals": "📭 Heute keine Mahlzeiten erfasst.",
    "edit_out_of_range": "❌ Keine Mahlzeit #{num}. Heutige Einträge: {total}.",
    "edit_done": "✅ *Mahlzeit #{num} aktualisiert*\n\n🍽️ {food}\n🔥 {cal} kcal | 🥩 {protein} g | 🧈 {fat} g | 🍞 {carbs} g\n\n📊 Heute: *{total_cal} kcal* / 🥩 *{total_protein} g Eiweiß*",

    # ── Delete from diary (callback) ──────────────────────────────
    "diary_deleted": "🗑️ Eintrag gelöscht.\n\n📊 Heute gegessen: *{cal} kcal* / 🥩 *{protein} g Eiweiß* ({n} Mahlzeiten)\n{remaining}",
    "diary_cal_left": "🎯 Noch bis zum Ziel: *{cal_left} kcal* und *{prot_left} g Eiweiß*",
    "diary_cal_done": "✅ Kalorienziel erreicht!",
    "diary_cal_over": "⚠️ Ziel überschritten um *{over} kcal*",

    # ── Reminders ─────────────────────────────────────────────────
    "reminder_text": "{emoji} Vergiss nicht mir zu sagen, was du zum {meal} gegessen hast!\nZiel: {goal_cal} kcal. Heute: {total_cal} kcal\n\n📸 Einfach Foto senden oder tippen",
    "btn_reminder_add": "🍽️ Mahlzeit hinzufügen",
    "btn_reminder_snooze": "❌ Nicht mehr an {meal} erinnern",

    # ── Weight tip ────────────────────────────────────────────────
    "weight_tip": "⚖️ *Tipp: Gewicht verfolgen*\n\nErfasse dein Gewicht jeden Morgen — der Bot zeigt dir Verlauf und Fortschritt zum Ziel.\n\nEinfach /weight eingeben und aktuelles Gewicht angeben.\nFortschrittsübersicht: /progress",

    # ── Admin ─────────────────────────────────────────────────────
    "resetme_done": "✅ Alle Daten gelöscht. Schreibe /start um neu zu beginnen.",
    "gift_usage": "Verwendung: /gift <user_id>",
    "gift_bad_id": "❌ user_id muss eine Zahl sein",
    "gift_done": "✅ Benutzer {uid} erhält dauerhaften Zugang.",
    "error_terms": "❌ Fehler: {e}",
    "error_invoice": "❌ Fehler beim Erstellen der Rechnung: {e}",
}
