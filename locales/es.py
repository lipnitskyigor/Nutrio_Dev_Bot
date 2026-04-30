texts = {
    # ── Menu buttons ──────────────────────────────────────────────
    "menu_diary": "📔 Diario",
    "menu_profile": "👤 Perfil",
    "menu_help": "❓ Ayuda",
    "menu_add": "🍽️ Añadir comida",
    "input_placeholder": "Envía una foto o describe lo que comiste...",

    # ── Language switching ────────────────────────────────────────
    "choose_language": "Elige idioma:",
    "language_changed_ru": "✅ Язык изменён на русский 🇷🇺",
    "language_changed_en": "✅ Language changed to English 🇬🇧",
    "language_changed_de": "✅ Sprache auf Deutsch geändert 🇩🇪",
    "language_changed_pl": "✅ Język zmieniony na polski 🇵🇱",
    "language_changed_es": "✅ Idioma cambiado a español 🇪🇸",
    "language_changed_pt": "✅ Idioma alterado para português 🇧🇷",
    "language_changed_uk": "✅ Мову змінено на українську 🇺🇦",
    "language_changed_be": "✅ Мова зменена на беларускую 🇧🇾",
    "btn_lang_ru": "🇷🇺 Русский",
    "btn_lang_en": "🇬🇧 English",
    "btn_lang_uk": "🇺🇦 Українська",
    "btn_lang_be": "🇧🇾 Беларуская",
    "btn_lang_de": "🇩🇪 Deutsch",
    "btn_lang_pl": "🇵🇱 Polski",
    "btn_lang_es": "🇪🇸 Español",
    "btn_lang_pt": "🇧🇷 Português",

    # ── Claude API instruction ────────────────────────────────────
    "claude_lang": "en español",

    # ── Terms ─────────────────────────────────────────────────────
    "terms_greeting": "👋 ¡Hola, {name}!\n\nAntes de empezar, lee esto importante:\n\n⚠️ Meal Scan es un asistente para contar calorías y macronutrientes.\nNo es una app médica. El bot no reemplaza a un médico,\ndietista o nutricionista.\n\n📄 Términos de uso: mealscan.org/terms.html\n\nAl pulsar el botón de abajo aceptas los términos de uso.",
    "btn_accept_terms": "✅ Acepto los términos",

    # ── Start / Welcome ───────────────────────────────────────────
    "welcome_back": "¡Bienvenido de nuevo, {name}! 👋\n\n📸 Envía una foto de tu comida o descríbela — la analizo.",
    "welcome_new": "Te ayudo a controlar tu alimentación — cuento calorías y macros de fotos o texto.\n\n📸 *Envía la foto de cualquier comida*\n✏️ O escribe lo que comiste\n\nPruébalo ahora ↓\n\n———\nℹ️ Meal Scan es un asistente nutricional, no una app médica. Si tienes problemas de salud, consulta a un médico o dietista.",
    "default_friend": "amigo",

    # ── Help ──────────────────────────────────────────────────────
    "help_text": (
        "🤖 *Cómo usar el bot:*\n\n"
        "📸 Envía foto de comida — cuento calorías y macros\n"
        "✏️ Describe tu comida — también lo cuento\n"
        "Por ejemplo: _«pollo con arroz 300g»_\n\n"
        "📊 *Calorías y nutrición:*\n"
        "/today — resumen de hoy (calorías, proteína, grasa, carbos)\n"
        "/history — historial de los últimos 7 días\n"
        "/goal 2000 150 — establecer objetivo diario de calorías y proteína\n"
        "/goal — ver objetivo actual\n"
        "/reset — borrar entradas de hoy\n\n"
        "⚖️ *Peso y progreso:*\n"
        "/weight 80.5 — registrar peso (hazlo cada día)\n"
        "/weight — ver último peso registrado\n"
        "/target 75 — establecer peso objetivo\n"
        "/target — ver peso objetivo y cuánto falta\n"
        "/progress — evolución del peso en 7 días con cambios 🟢🔴\n\n"
        "💡 Consejo: ¡cuanto más clara se vea la comida en la foto, más preciso el resultado!\n\n"
        "🔔 *Recordatorios:*\n"
        "/notify — configurar recordatorios de comidas\n\n"
        "💬 *Soporte:*\n"
        "/support — contactar soporte"
    ),

    # ── Support ───────────────────────────────────────────────────
    "support_text": "💬 *Soporte Meal Scan*\n\n¿Preguntas o problemas? Escríbenos:\n\n👉 @Meal_Scan_Support",

    # ── Today ─────────────────────────────────────────────────────
    "today_empty": "📭 Sin comidas registradas hoy.\n¡Envía una foto para empezar a contar!",
    "today_header": "📊 *Resumen de hoy — {name}*\n",
    "today_meal_line": "{i}. {food} — {cal} kcal ({time})",
    "today_total_cal": "\n🔥 *Total: {cal} kcal*",
    "today_macros": "🥩 Proteína: {protein} g  🧈 Grasa: {fat} g  🍞 Carbos: {carbs} g",
    "today_cal_left": "\n🎯 Para llegar al objetivo: *{cal_left} kcal* y *{prot_left} g proteína*",
    "today_cal_done": "\n✅ *¡Objetivo calórico del día alcanzado!*",
    "today_cal_over": "\n⚠️ Objetivo superado en *{over} kcal*",

    # ── History ───────────────────────────────────────────────────
    "history_empty": "📭 Sin datos de los últimos 7 días.\n¡Envía una foto para empezar!",
    "history_header": "📅 *Historial 7 días — {name}*\n",
    "history_entry": "📆 {day}: *{cal} kcal* ({n} comida{suffix})",
    "history_meals_suffix_1": "",
    "history_meals_suffix_other": "s",

    # ── Reset ─────────────────────────────────────────────────────
    "reset_done": "🗑️ ¡Datos de hoy eliminados!",

    # ── Goal ──────────────────────────────────────────────────────
    "goal_current": "🎯 *Tu objetivo diario:*\n🔥 Calorías: {cal} kcal\n🥩 Proteína: {protein} g\n\nCambiar: `/goal 2000 150`",
    "goal_not_set": "🎯 Sin objetivo.\n\nEstablécelo: `/goal calorías proteína`\nEj.: `/goal 2000 150`",
    "goal_saved": "✅ *¡Objetivo establecido!*\n🔥 Calorías: {cal} kcal/día\n🥩 Proteína: {protein} g/día",
    "goal_bad_format": "❌ Formato incorrecto. Usa: `/goal 2000 150`",

    # ── Weight ────────────────────────────────────────────────────
    "weight_last": "⚖️ *Último peso:* {weight} kg ({day})\n\nPara registrar uno nuevo: `/weight 80.5`",
    "weight_not_set": "⚖️ No hay peso registrado todavía.\n\nRegístralo así: `/weight 80.5`",
    "weight_saved": "⚖️ *Peso registrado:* {weight} kg\n",
    "weight_to_goal": "\n🎯 Para llegar al objetivo ({target} kg): *{diff} kg* restantes\n",
    "weight_almost": "💪 ¡Casi! ¡Estás tan cerca del objetivo!",
    "weight_great_progress": "🔥 ¡Gran progreso, sigue así!",
    "weight_good_start": "💪 ¡Buen comienzo! Cada día te acerca más al objetivo.",
    "weight_goal_reached": "\n🏆 ¡Objetivo alcanzado! ¡Estás {diff} kg por debajo de tu peso objetivo!",
    "weight_on_goal": "\n🎯 ¡Estás exactamente en tu peso objetivo! ¡Excelente!",
    "weight_set_target_hint": "\n💡 Establece un peso objetivo con `/target 75`",
    "weight_bad_format": "❌ Formato incorrecto. Usa: `/weight 80.5`",

    # ── Progress ──────────────────────────────────────────────────
    "progress_empty": "⚖️ Sin datos de peso.\n\nRegistra tu peso cada día con `/weight 80.5` — ¡te mostraré la evolución!",
    "progress_header": "📈 *Evolución del peso:*\n",
    "progress_entry_first": "📅 {day}: *{w} kg*",
    "progress_entry_down": "📅 {day}: *{w} kg* (🟢 {diff} kg)",
    "progress_entry_up": "📅 {day}: *{w} kg* (🔴 +{diff} kg)",
    "progress_entry_same": "📅 {day}: *{w} kg* (➡️ sin cambios)",
    "progress_total_down": "\n📉 En el período: *{diff} kg* — ¡gran resultado!",
    "progress_total_up": "\n📈 En el período: *+{diff} kg*",
    "progress_total_stable": "\n➡️ En el período: peso estable",
    "progress_to_goal": "🎯 Para llegar al objetivo ({target} kg): *{diff} kg* restantes",
    "progress_goal_reached": "🏆 Objetivo {target} kg — *¡alcanzado!*",

    # ── Target ────────────────────────────────────────────────────
    "target_current": "🎯 *Peso objetivo:* {target} kg\n",
    "target_remaining": "📍 Peso actual: {current} kg — *{diff} kg* restantes",
    "target_reached": "🏆 Peso actual: {current} kg — ¡objetivo alcanzado!",
    "target_change_hint": "\n\nCambiar: `/target 70`",
    "target_not_set": "🎯 Peso objetivo no establecido.\n\nEstablécelo así: `/target 75`",
    "target_bad_format": "❌ Formato incorrecto. Usa: `/target 75`",
    "target_need_profile": "📋 Para verificar la seguridad del objetivo se necesita un perfil (altura, edad, sexo, actividad).\n\nConfigura tu perfil — comprobaré si tu objetivo es seguro.",
    "btn_setup_profile": "👉 Configurar perfil",
    "target_safe_set": "✅ *Objetivo establecido: {target} kg*\n\n📊 Calorías recomendadas: *{cal} kcal/día*\n",
    "target_min_cal_warn": "⚠️ _Calorías mínimas seguras: {min_cal} kcal/día_\n",
    "target_weeks": "⏱ Tiempo estimado: *{weeks} semanas*",
    "target_warn_low_bmi": "⚠️ El peso objetivo *{target} kg* da un IMC de *{bmi}* — por debajo de lo normal.\nPeso mínimo recomendado para tu altura: *{min_weight} kg*.\n\nConsulta a un especialista antes de empezar.",
    "target_danger_bmi": "🚨 El peso objetivo *{target} kg* — IMC *{bmi}*, peligrosamente bajo.\nMínimo recomendado para {height} cm: *{min_weight} kg*.\n\nRecomendamos encarecidamente consultar a un médico.",
    "target_critical_bmi": "❌ No se puede establecer el objetivo *{target} kg*.\nIMC *{bmi}* es críticamente bajo y pone en riesgo la vida.\n\nPeso mínimo seguro para tu altura: *{min_weight} kg*.\nPor favor consulta a un médico o dietista.",
    "btn_target_confirm": "✅ Establecer de todas formas",
    "btn_target_confirm_warn": "⚠️ Establecer de todas formas (no recomendado)",
    "btn_target_change": "✏️ Cambiar objetivo",
    "target_confirmed_msg": "✅ Peso objetivo *{target} kg* establecido.\n\n⚠️ Recuerda la recomendación de consultar a un especialista.",
    "target_change_prompt": "Introduce un nuevo peso objetivo: `/target 70`",

    # ── Meal analysis ─────────────────────────────────────────────
    "analyzing_photo": "🔍 Analizando foto...",
    "counting_calories": "🔍 Calculando calorías...",
    "recalculating": "🔍 Recalculando...",
    "analysis_error_parse": "😔 No pude procesar la respuesta. Inténtalo de nuevo o haz una foto más clara.",
    "analysis_error_photo": "😔 Error al analizar la foto. ¡Inténtalo de nuevo!",
    "analysis_error_text": "😔 No entendí. ¡Describe con más detalle!",
    "analysis_error_generic": "😔 Ocurrió un error. ¡Inténtalo de nuevo!",
    "correction_error": "😔 No pude recalcular. ¡Describe con más detalle!",
    "corrected_prefix": "✅ *¡Corregido!*\n\n",

    # ── Meal summary ──────────────────────────────────────────────
    "meal_summary_header": "🍽️ *{food}*\n\n🔥 *{cal} kcal*\n🥩 Proteína: *{protein} g*\n🧈 Grasa: {fat} g\n🍞 Carbos: {carbs} g\n\n💬 _{comment}_\n\n📊 *Resumen de hoy:*\n🔥 {total_cal} kcal (~{day_pct}% de la norma)  🥩 proteína: *{total_protein} g*",
    "meal_remaining_profile": "\n\n🎯 Para llegar al objetivo: *~{cal_left} kcal* y *~{prot_left} g proteína*\n_(objetivo: {cal_low}–{cal_high} kcal/día)_",
    "meal_on_target_profile": "\n\n✅ ¡Dentro del objetivo! ({cal_low}–{cal_high} kcal/día)",
    "meal_over_target_profile": "\n\n⚠️ Por encima del objetivo en ~*{over} kcal*",
    "meal_remaining_default": "\n\n🎯 Para llegar a la norma media: *~{cal_left} kcal* y *~{prot_left} g proteína*",
    "meal_on_target_default": "\n\n✅ ¡Norma media alcanzada!",
    "meal_over_target_default": "\n\n⚠️ Por encima de la norma media en *{over} kcal*",

    # ── Meal keyboard ─────────────────────────────────────────────
    "btn_meal_confirm": "✅ Correcto",
    "btn_meal_edit": "✏️ Editar",
    "btn_meal_delete": "🗑️ Eliminar",
    "edit_prompt": "✏️ Escribe la corrección — recalcularé:",
    "quick_add_prompt": "📸 Envía una foto de tu comida o descríbela — ¡la calculo!",
    "menu_add_prompt": "📸 Envía una foto de tu comida o descríbela — ¡la calculo!",

    # ── Short input hint ──────────────────────────────────────────
    "short_input_hint": "📸 Envía una foto o describe tu comida — ¡cuento las calorías!\n\nPor ejemplo: *«un plato de sopa y pan»* o *«2 huevos, café con leche»*",

    # ── Profile ───────────────────────────────────────────────────
    "profile_not_set": "📋 *Perfil no configurado*\n\nCompleta tu perfil — calcularé con más precisión tu norma de calorías y progreso.",
    "btn_edit_profile": "✏️ Editar perfil",
    "profile_goal_lose": "Perder peso 🥦",
    "profile_goal_maintain": "Mantener peso ⚖️",
    "profile_goal_gain": "Ganar músculo 💪",
    "profile_activity_sedentary": "Sedentario 🪑",
    "profile_activity_light": "Ligera 🚶",
    "profile_activity_moderate": "Moderada 🏃",
    "profile_activity_active": "Alta 💪",
    "profile_view": "👤 *Tu perfil*\n\n🎯 Objetivo: {goal}\n⚡ Actividad: {activity}\n📏 Altura: {height} cm\n⚖️ Peso: {weight} kg\n",
    "profile_last_weight": "📅 Último peso: *{w} kg* ({day})\n",
    "profile_weight_goal_reached": "🏁 Peso objetivo: *{target} kg* — ¡alcanzado! 🎉\n",
    "profile_weight_to_goal": "🏁 Para llegar al objetivo ({target} kg): *{diff} kg*\n",
    "profile_norm": "\n🔥 Norma: *{low}–{high} kcal/día*\n🥩 Proteína: *{protein} g/día*\n📊 Comido hoy: *{today_cal} kcal*",

    # ── Onboarding / Profile flow ─────────────────────────────────
    "profile_prompt_title": "📊 *Vamos a ajustar las calorías a ti y tu objetivo*\n\nResponde 4 preguntas — el cálculo será más preciso\nMenos de 30 segundos",
    "btn_profile_yes": "👉 Vamos",
    "btn_profile_skip": "Omitir",
    "ask_goal": "¿Cuál es tu objetivo?",
    "ask_sex": "¿Tu sexo?",
    "ask_activity": "¿Tu nivel de actividad?",
    "ask_age": "¿Cuántos años tienes?\n\nEscribe un número, ej.: *28*",
    "ask_height": "¿Tu altura?\n\nEn centímetros, ej.: *178*",
    "ask_weight": "¿Tu peso actual?\n\nEn kilogramos, ej.: *75*",
    "ask_target_weight": "¿Tienes un peso objetivo?",
    "btn_set_target_yes": "✏️ Sí, lo indico",
    "btn_skip": "Omitir",
    "ask_target_weight_enter": "Escribe el peso objetivo en kg, ej.: *70*",
    "age_bad": "Escribe la edad como número, ej.: *28*",
    "height_bad": "Escribe la altura en cm, ej.: *178*",
    "weight_bad": "Escribe el peso en kg, ej.: *75*",
    "target_weight_bad": "Escribe el peso en kg, ej.: *70*",
    "target_weight_critical_onb": "❌ El peso objetivo *{target} kg* — IMC *{bmi}*, críticamente peligroso.\nPeso mínimo seguro para {height} cm: *{min_weight} kg*.\n\nEscribe otro peso objetivo:",
    "btn_target_confirm_onb": "✅ Establecer de todas formas",
    "btn_target_change_onb": "✏️ Cambiar objetivo",
    "target_change_onb_prompt": "Escribe otro peso objetivo en kg, ej.: *70*",

    # goal labels (used in _finish_profile)
    "goal_label_lose": "Perder peso",
    "goal_label_maintain": "Mantener peso",
    "goal_label_gain": "Ganar músculo",

    # ── Profile goal buttons ──────────────────────────────────────
    "btn_goal_lose": "📉 Perder peso",
    "btn_goal_maintain": "⚖️ Mantener peso",
    "btn_goal_gain": "📈 Ganar músculo",
    "btn_sex_male": "👨 Masculino",
    "btn_sex_female": "👩 Femenino",
    "btn_activity_sedentary": "🪑 Sedentario (oficina, sin deporte)",
    "btn_activity_light": "🚶 Ligera (1–2 veces/semana)",
    "btn_activity_moderate": "🏃 Moderada (3–5 veces/semana)",
    "btn_activity_active": "💪 Alta (todos los días)",

    # ── Finish profile ────────────────────────────────────────────
    "profile_done": "✅ *¡Todo listo!*\n\n🎯 Objetivo: *{goal}*\n🔥 Calorías: *{low}–{high} kcal/día*\n🥩 Proteína: *~{protein} g/día*{target_line}\n\nDespués de cada comida te mostraré cuántas calorías te quedan 🎯",
    "profile_target_line_remaining": "\n⚖️ Peso objetivo: *{target} kg* (~{diff} kg restantes)",
    "profile_target_line_reached": "\n⚖️ Peso objetivo: *{target} kg* — ¡ya alcanzado! 🏆",
    "ask_timezone": "🔔 *¡Configuremos recordatorios de comidas!*\n\nTe recordaré registrar tus comidas — solo envía una foto o describe lo que comiste.\n\n¿Qué hora es ahora para ti? ej.: *23:15*",

    # ── Notifications ─────────────────────────────────────────────
    "notify_header": "⏰ *Configuración de recordatorios*\n\n🌍 Zona horaria: {tz} (ahora {time})\n\n☕ Desayuno — {b_time} ({b})\n🍲 Almuerzo — {l_time} ({l})\n🍽️ Cena — {d_time} ({d})\n\n⚠️ Recomendamos mantener al menos 1 recordatorio activado",
    "btn_notif_all_on": "✅ Activar todos",
    "btn_notif_all_off": "❌ Desactivar todos",
    "btn_notif_change_tz": "🌍 Cambiar zona horaria",
    "notif_enabled": "✅",
    "notif_disabled": "❌",
    "notif_breakfast": "☕ Desayuno",
    "notif_lunch": "🍲 Almuerzo",
    "notif_dinner": "🍽️ Cena",
    "notif_time_prompt": "⏰ Escribe la nueva hora de recordatorio para *{meal}*\n\nFormato: *HH:MM*, ej.: *08:30*",
    "notif_timezone_prompt": "🕐 Escribe qué hora es ahora para ti, ej.: *23:15*\n\nDeterminaré la zona horaria automáticamente.",
    "notif_timezone_updated": "✅ Zona horaria actualizada: UTC{sign}{offset}\n\n",
    "notif_time_updated": "✅ Hora de recordatorio ({meal}) actualizada: *{time}*\n\n",
    "notif_time_bad": "❌ No entendí la hora. Escríbela en formato *HH:MM*, ej.: *08:30*",
    "timezone_bad": "No entendí 🤔 Escribe la hora en formato *HH:MM*, ej.: *23:15*",
    "meal_name_breakfast": "desayuno",
    "meal_name_lunch": "almuerzo",
    "meal_name_dinner": "cena",
    "notif_tz_saved": "🔔 *¡Recordatorios activados!*\n\n🌍 Zona horaria: {tz}\n☕ Desayuno — 9:00\n🍲 Almuerzo — 13:00\n🍽️ Cena — 19:00\n\nConfigurar: /notify",
    "onb_tz_saved": "🔔 *¡Recordatorios activados!*\n\n🌍 Zona horaria: {tz}\n☕ Desayuno — 9:00\n🍲 Almuerzo — 13:00\n🍽️ Cena — 19:00\n\nConfigurar: /notify",
    "onb_tz_skip": "OK, sin recordatorios 👌\nActivar en cualquier momento: /notify",
    "notif_snooze_done": "✅ Recordatorio de {meal} desactivado.\nReactivar: /notify",

    # ── Timezone city names ───────────────────────────────────────
    "tz_kyiv": "🇺🇦 Kiev",
    "tz_moscow": "🇷🇺 Moscú",
    "tz_baku": "🇦🇿 Bakú",
    "tz_almaty": "🇰🇿 Almaty",
    "tz_tashkent": "🇺🇿 Taskent",
    "tz_novosibirsk": "Novosibirsk",
    "tz_irkutsk": "Irkutsk",
    "tz_vladivostok": "Vladivostok",
    "tz_skip": "❌ Omitir",

    # ── Trial / Paywall ───────────────────────────────────────────
    "trial_exhausted": "❌ *Análisis gratuitos agotados* (15 de 15)\n\nSuscríbete para seguir contando calorías 👇",
    "trial_last_1": "⚠️ Queda *1 análisis gratuito* de {limit} → /subscribe",
    "trial_last_few": "⚠️ Quedan *{left} análisis gratuitos* de {limit} → /subscribe",
    "trial_some_left": "🎁 {left} análisis gratuitos restantes de {limit} → /subscribe",
    "trial_many_left": "🎁 Análisis gratuitos: {left} de {limit}",
    "btn_subscribe": "💳 Suscribirse",
    "subscribe_remaining": "🎁 Análisis gratuitos restantes: *{left} de {limit}*\n\n",
    "subscribe_exhausted": "❌ Análisis gratuitos agotados\n\n",
    "subscribe_header": "💳 *Suscripción Meal Scan*\n\nElige un plan:",
    "subscribe_header_full": "💳 *Suscripción Meal Scan*\n\nConteo ilimitado de calorías de fotos y texto\n\nElige un plan:",
    "subscribe_active": "✅ *Suscripción activa hasta {expires}*\n\nPuedes renovar anticipadamente — el tiempo se añadirá al período actual:",
    "payment_success": "🎉 *¡Suscripción activada por {label}!*\n\nCuenta calorías sin límites 🍽️\nEnvía una foto o describe tu comida ↓",
    "sub_1m_label": "1 mes",
    "sub_3m_label": "3 meses",
    "sub_invoice_title_1m": "Suscripción Meal Scan — 1 mes",
    "sub_invoice_title_3m": "Suscripción Meal Scan — 3 meses",
    "sub_invoice_desc": "Conteo ilimitado de calorías y macros de fotos y texto",
    "sub_invoice_error": "❌ Error al crear la factura: {e}",

    # ── Delete command ────────────────────────────────────────────
    "delete_no_num": "❌ Indica el número de comida.\nEjemplo: `/delete 2`\n\nLista de hoy: /today",
    "delete_bad_num": "❌ El número debe ser entero. Por ejemplo: `/delete 2`",
    "delete_no_meals": "📭 No hay comidas registradas hoy.",
    "delete_out_of_range": "❌ No hay comida #{num}. Entradas de hoy: {total}.\n\nVer lista: /today",
    "delete_done": "🗑️ Eliminado: *{food}* ({cal} kcal)\n\n📊 Restante hoy: *{total_cal} kcal* ({n} comidas)",

    # ── Edit command ──────────────────────────────────────────────
    "edit_no_args": "✏️ Formato: `/edit número nueva descripción`\nEjemplo: `/edit 2 borscht de ternera 400g`\n\nLista de hoy: /today",
    "edit_bad_num": "❌ Indica primero el número. Por ejemplo: `/edit 2 sopa 400g`",
    "edit_no_meals": "📭 No hay comidas registradas hoy.",
    "edit_out_of_range": "❌ No hay comida #{num}. Entradas de hoy: {total}.",
    "edit_done": "✅ *Comida #{num} actualizada*\n\n🍽️ {food}\n🔥 {cal} kcal | 🥩 {protein} g | 🧈 {fat} g | 🍞 {carbs} g\n\n📊 Hoy: *{total_cal} kcal* / 🥩 *{total_protein} g proteína*",

    # ── Delete from diary (callback) ──────────────────────────────
    "diary_deleted": "🗑️ Entrada eliminada.\n\n📊 Comido hoy: *{cal} kcal* / 🥩 *{protein} g proteína* ({n} comidas)\n{remaining}",
    "diary_cal_left": "🎯 Para llegar al objetivo: *{cal_left} kcal* y *{prot_left} g proteína*",
    "diary_cal_done": "✅ ¡Objetivo calórico alcanzado!",
    "diary_cal_over": "⚠️ Objetivo superado en *{over} kcal*",

    # ── Reminders ─────────────────────────────────────────────────
    "reminder_text": "{emoji} ¡No olvides contarme qué comiste en el {meal}!\nObjetivo: {goal_cal} kcal. Hoy: {total_cal} kcal\n\n📸 Solo envía una foto o escríbelo",
    "btn_reminder_add": "🍽️ Añadir comida",
    "btn_reminder_snooze": "❌ No recordar el {meal}",

    # ── Weight tip ────────────────────────────────────────────────
    "weight_tip": "⚖️ *Consejo: sigue tu peso*\n\nPuedes registrar tu peso cada mañana — el bot te mostrará la evolución y el progreso hacia tu objetivo.\n\nEscribe /weight e introduce tu peso actual.\nGráfico de progreso: /progress",

    # ── Admin ─────────────────────────────────────────────────────
    "resetme_done": "✅ Todos los datos eliminados. Escribe /start para empezar de nuevo.",
    "gift_usage": "Uso: /gift <user_id>",
    "gift_bad_id": "❌ user_id debe ser un número",
    "gift_done": "✅ Usuario {uid} con acceso permanente.",
    "error_terms": "❌ Error: {e}",
    "error_invoice": "❌ Error al crear la factura: {e}",
}
