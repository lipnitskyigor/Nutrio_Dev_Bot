texts = {
    # ── Menu buttons ──────────────────────────────────────────────
    "menu_diary": "📔 Diário",
    "menu_profile": "👤 Perfil",
    "menu_help": "❓ Ajuda",
    "menu_add": "🍽️ Adicionar refeição",
    "input_placeholder": "Envie uma foto ou descreva o que comeu...",

    # ── Language switching ────────────────────────────────────────
    "choose_language": "Escolha o idioma:",
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
    "claude_lang": "em português brasileiro",

    # ── Terms ─────────────────────────────────────────────────────
    "terms_greeting": "👋 Olá, {name}!\n\nAntes de começar, leia isto importante:\n\n⚠️ Meal Scan é um assistente para contar calorias e macronutrientes.\nNão é um app médico. O bot não substitui médico,\nnutricionista ou dietista.\n\n📄 Termos de uso: mealscan.org/terms.html\n\nAo tocar no botão abaixo você concorda com os termos de uso.",
    "btn_accept_terms": "✅ Aceito os termos",

    # ── Start / Welcome ───────────────────────────────────────────
    "welcome_back": "Bem-vindo de volta, {name}! 👋\n\n📸 Envie uma foto da sua refeição ou descreva o que comeu — eu conto.",
    "welcome_new": "Ajudo você a monitorar sua alimentação — conto calorias e macros de fotos ou texto.\n\n📸 *Envie a foto de qualquer refeição*\n✏️ Ou escreva o que comeu\n\nExperimente agora ↓\n\n———\nℹ️ Meal Scan é um assistente nutricional, não um app médico. Se tiver problemas de saúde ou quiser mudar sua dieta, consulte um médico ou nutricionista.",
    "default_friend": "amigo",

    # ── Help ──────────────────────────────────────────────────────
    "help_text": (
        "🤖 *Como usar o bot:*\n\n"
        "📸 Envie foto de comida — conto calorias e macros\n"
        "✏️ Descreva sua refeição — também conto\n"
        "Por exemplo: _«frango com arroz 300g»_\n\n"
        "📊 *Calorias e nutrição:*\n"
        "/today — resumo de hoje (calorias, proteína, gordura, carboidratos)\n"
        "/history — histórico dos últimos 7 dias\n"
        "/goal 2000 150 — definir meta diária de calorias e proteína\n"
        "/goal — ver meta atual\n"
        "/reset — apagar registros de hoje\n\n"
        "⚖️ *Peso e progresso:*\n"
        "/weight 80.5 — registrar peso (faça todo dia)\n"
        "/weight — ver último peso registrado\n"
        "/target 75 — definir peso alvo\n"
        "/target — ver peso alvo e quanto falta\n"
        "/progress — evolução do peso em 7 dias com 🟢🔴\n\n"
        "💡 Dica: quanto mais nítida a comida na foto, mais preciso o resultado!\n\n"
        "🔔 *Lembretes:*\n"
        "/notify — configurar lembretes de refeições\n\n"
        "💬 *Suporte:*\n"
        "/support — contato com suporte"
    ),

    # ── Support ───────────────────────────────────────────────────
    "support_text": "💬 *Suporte Meal Scan*\n\nDúvidas ou problemas? Escreva para nós:\n\n👉 @Meal\_Scan\_Support",

    # ── Today ─────────────────────────────────────────────────────
    "today_empty": "📭 Nenhuma refeição registrada hoje.\nEnvie uma foto para começar a contar!",
    "today_header": "📊 *Resumo de hoje — {name}*\n",
    "today_meal_line": "{i}. {food} — {cal} kcal ({time})",
    "today_total_cal": "\n🔥 *Total: {cal} kcal*",
    "today_macros": "🥩 Proteína: {protein} g  🧈 Gordura: {fat} g  🍞 Carboidratos: {carbs} g",
    "today_cal_left": "\n🎯 Para atingir a meta: *{cal_left} kcal* e *{prot_left} g proteína*",
    "today_cal_done": "\n✅ *Meta calórica do dia atingida!*",
    "today_cal_over": "\n⚠️ Meta superada em *{over} kcal*",

    # ── History ───────────────────────────────────────────────────
    "history_empty": "📭 Sem dados dos últimos 7 dias.\nEnvie uma foto para começar!",
    "history_header": "📅 *Histórico 7 dias — {name}*\n",
    "history_entry": "📆 {day}: *{cal} kcal* ({n} refeição{suffix})",
    "history_meals_suffix_1": "",
    "history_meals_suffix_other": "ões",

    # ── Reset ─────────────────────────────────────────────────────
    "reset_done": "🗑️ Dados de hoje excluídos!",

    # ── Goal ──────────────────────────────────────────────────────
    "goal_current": "🎯 *Sua meta diária:*\n🔥 Calorias: {cal} kcal\n🥩 Proteína: {protein} g\n\nAlterar: `/goal 2000 150`",
    "goal_not_set": "🎯 Sem meta definida.\n\nDefina assim: `/goal calorias proteína`\nEx.: `/goal 2000 150`",
    "goal_saved": "✅ *Meta definida!*\n🔥 Calorias: {cal} kcal/dia\n🥩 Proteína: {protein} g/dia",
    "goal_bad_format": "❌ Formato incorreto. Use: `/goal 2000 150`",

    # ── Weight ────────────────────────────────────────────────────
    "weight_last": "⚖️ *Último peso:* {weight} kg ({day})\n\nPara registrar um novo: `/weight 80.5`",
    "weight_not_set": "⚖️ Nenhum peso registrado ainda.\n\nRegistre assim: `/weight 80.5`",
    "weight_saved": "⚖️ *Peso registrado:* {weight} kg\n",
    "weight_to_goal": "\n🎯 Para o objetivo ({target} kg): *{diff} kg* restantes\n",
    "weight_almost": "💪 Quase lá! Você está tão perto do objetivo!",
    "weight_great_progress": "🔥 Ótimo progresso, continue assim!",
    "weight_good_start": "💪 Bom começo! Cada dia te aproxima mais do objetivo.",
    "weight_goal_reached": "\n🏆 Objetivo atingido! Você está {diff} kg abaixo do seu peso alvo!",
    "weight_on_goal": "\n🎯 Você está exatamente no seu peso alvo! Excelente!",
    "weight_set_target_hint": "\n💡 Defina um peso alvo com `/target 75`",
    "weight_bad_format": "❌ Formato incorreto. Use: `/weight 80.5`",

    # ── Progress ──────────────────────────────────────────────────
    "progress_empty": "⚖️ Sem dados de peso.\n\nRegistre seu peso todo dia com `/weight 80.5` — vou mostrar a evolução!",
    "progress_header": "📈 *Evolução do peso:*\n",
    "progress_entry_first": "📅 {day}: *{w} kg*",
    "progress_entry_down": "📅 {day}: *{w} kg* (🟢 {diff} kg)",
    "progress_entry_up": "📅 {day}: *{w} kg* (🔴 +{diff} kg)",
    "progress_entry_same": "📅 {day}: *{w} kg* (➡️ sem mudança)",
    "progress_total_down": "\n📉 No período: *{diff} kg* — ótimo resultado!",
    "progress_total_up": "\n📈 No período: *+{diff} kg*",
    "progress_total_stable": "\n➡️ No período: peso estável",
    "progress_to_goal": "🎯 Para o objetivo ({target} kg): *{diff} kg* restantes",
    "progress_goal_reached": "🏆 Objetivo {target} kg — *atingido!*",

    # ── Target ────────────────────────────────────────────────────
    "target_current": "🎯 *Peso alvo:* {target} kg\n",
    "target_remaining": "📍 Peso atual: {current} kg — *{diff} kg* restantes",
    "target_reached": "🏆 Peso atual: {current} kg — objetivo atingido!",
    "target_change_hint": "\n\nAlterar: `/target 70`",
    "target_not_set": "🎯 Peso alvo não definido.\n\nDefina assim: `/target 75`",
    "target_bad_format": "❌ Formato incorreto. Use: `/target 75`",
    "target_need_profile": "📋 Para verificar a segurança do objetivo é necessário um perfil (altura, idade, sexo, atividade).\n\nConfigure seu perfil — vou verificar se seu objetivo é seguro.",
    "btn_setup_profile": "👉 Configurar perfil",
    "target_safe_set": "✅ *Objetivo definido: {target} kg*\n\n📊 Calorias recomendadas: *{cal} kcal/dia*\n",
    "target_min_cal_warn": "⚠️ _Calorias mínimas seguras: {min_cal} kcal/dia_\n",
    "target_weeks": "⏱ Tempo estimado: *{weeks} semanas*",
    "target_warn_low_bmi": "⚠️ O peso alvo *{target} kg* resulta em IMC *{bmi}* — abaixo do normal.\nPeso mínimo recomendado para sua altura: *{min_weight} kg*.\n\nConsulte um especialista antes de começar.",
    "target_danger_bmi": "🚨 Peso alvo *{target} kg* — IMC *{bmi}*, perigosamente baixo.\nMínimo recomendado para {height} cm: *{min_weight} kg*.\n\nRecomendamos fortemente consultar um médico.",
    "target_critical_bmi": "❌ Não é possível definir o objetivo *{target} kg*.\nIMC *{bmi}* é criticamente baixo e coloca a vida em risco.\n\nPeso mínimo seguro para sua altura: *{min_weight} kg*.\nPor favor consulte um médico ou nutricionista.",
    "btn_target_confirm": "✅ Definir mesmo assim",
    "btn_target_confirm_warn": "⚠️ Definir mesmo assim (não recomendado)",
    "btn_target_change": "✏️ Alterar objetivo",
    "target_confirmed_msg": "✅ Peso alvo *{target} kg* definido.\n\n⚠️ Lembre-se da recomendação de consultar um especialista.",
    "target_change_prompt": "Digite um novo peso alvo: `/target 70`",

    # ── Meal analysis ─────────────────────────────────────────────
    "analyzing_photo": "🔍 Analisando foto...",
    "counting_calories": "🔍 Calculando calorias...",
    "recalculating": "🔍 Recalculando...",
    "analysis_error_parse": "😔 Não consegui processar a resposta. Tente novamente ou tire uma foto mais nítida.",
    "analysis_error_photo": "😔 Erro ao analisar a foto. Tente novamente!",
    "analysis_error_text": "😔 Não entendi. Tente descrever com mais detalhes!",
    "analysis_error_generic": "😔 Ocorreu um erro. Tente novamente!",
    "correction_error": "😔 Não consegui recalcular. Descreva com mais detalhes!",
    "corrected_prefix": "✅ *Corrigido!*\n\n",

    # ── Meal summary ──────────────────────────────────────────────
    "meal_summary_header": "🍽️ *{food}*\n\n🔥 *{cal} kcal*\n🥩 Proteína: *{protein} g*\n🧈 Gordura: {fat} g\n🍞 Carboidratos: {carbs} g\n\n💬 _{comment}_\n\n📊 *Resumo de hoje:*\n🔥 {total_cal} kcal (~{day_pct}% da norma)  🥩 proteína: *{total_protein} g*",
    "meal_remaining_profile": "\n\n🎯 Para atingir a meta: *~{cal_left} kcal* e *~{prot_left} g proteína*\n_(meta: {cal_low}–{cal_high} kcal/dia)_",
    "meal_on_target_profile": "\n\n✅ Dentro da meta! ({cal_low}–{cal_high} kcal/dia)",
    "meal_over_target_profile": "\n\n⚠️ Acima da meta em ~*{over} kcal*",
    "meal_remaining_default": "\n\n🎯 Para a norma média: *~{cal_left} kcal* e *~{prot_left} g proteína*",
    "meal_on_target_default": "\n\n✅ Norma média atingida!",
    "meal_over_target_default": "\n\n⚠️ Acima da norma média em *{over} kcal*",

    # ── Meal keyboard ─────────────────────────────────────────────
    "btn_meal_confirm": "✅ Correto",
    "btn_meal_edit": "✏️ Editar",
    "btn_meal_delete": "🗑️ Excluir",
    "edit_prompt": "✏️ Escreva a correção — vou recalcular:",
    "quick_add_prompt": "📸 Envie uma foto da sua refeição ou descreva o que comeu — calculo!",
    "menu_add_prompt": "📸 Envie uma foto da sua refeição ou descreva o que comeu — calculo!",

    # ── Short input hint ──────────────────────────────────────────
    "short_input_hint": "📸 Envie uma foto ou descreva sua refeição — conto as calorias!\n\nPor exemplo: *«um prato de sopa e pão»* ou *«2 ovos, café com leite»*",

    # ── Profile ───────────────────────────────────────────────────
    "profile_not_set": "📋 *Perfil não configurado*\n\nPreencha seu perfil — vou calcular com mais precisão sua norma de calorias e progresso.",
    "btn_edit_profile": "✏️ Editar perfil",
    "profile_goal_lose": "Emagrecer 🥦",
    "profile_goal_maintain": "Manter peso ⚖️",
    "profile_goal_gain": "Ganhar massa 💪",
    "profile_activity_sedentary": "Sedentário 🪑",
    "profile_activity_light": "Leve 🚶",
    "profile_activity_moderate": "Moderada 🏃",
    "profile_activity_active": "Alta 💪",
    "profile_view": "👤 *Seu perfil*\n\n🎯 Objetivo: {goal}\n⚡ Atividade: {activity}\n📏 Altura: {height} cm\n⚖️ Peso: {weight} kg\n",
    "profile_last_weight": "📅 Último peso: *{w} kg* ({day})\n",
    "profile_weight_goal_reached": "🏁 Peso alvo: *{target} kg* — atingido! 🎉\n",
    "profile_weight_to_goal": "🏁 Para o objetivo ({target} kg): *{diff} kg*\n",
    "profile_norm": "\n🔥 Norma: *{low}–{high} kcal/dia*\n🥩 Proteína: *{protein} g/dia*\n📊 Comido hoje: *{today_cal} kcal*",

    # ── Onboarding / Profile flow ─────────────────────────────────
    "profile_prompt_title": "📊 *Vamos ajustar as calorias para você e seu objetivo*\n\nResponda 4 perguntas — o cálculo ficará mais preciso\nMenos de 30 segundos",
    "btn_profile_yes": "👉 Vamos lá",
    "btn_profile_skip": "Pular",
    "ask_goal": "Qual é o seu objetivo?",
    "ask_sex": "Seu sexo?",
    "ask_activity": "Seu estilo de vida?",
    "ask_age": "Quantos anos você tem?\n\nDigite um número, ex.: *28*",
    "ask_height": "Sua altura?\n\nEm centímetros, ex.: *178*",
    "ask_weight": "Seu peso atual?\n\nEm quilogramas, ex.: *75*",
    "ask_target_weight": "Tem um peso alvo?",
    "btn_set_target_yes": "✏️ Sim, vou definir",
    "btn_skip": "Pular",
    "ask_target_weight_enter": "Digite o peso alvo em kg, ex.: *70*",
    "age_bad": "Digite a idade como número, ex.: *28*",
    "height_bad": "Digite a altura como número em cm, ex.: *178*",
    "weight_bad": "Digite o peso como número em kg, ex.: *75*",
    "target_weight_bad": "Digite o peso como número em kg, ex.: *70*",
    "target_weight_critical_onb": "❌ Peso alvo *{target} kg* — IMC *{bmi}*, criticamente perigoso.\nPeso mínimo seguro para {height} cm: *{min_weight} kg*.\n\nDigite outro peso alvo:",
    "btn_target_confirm_onb": "✅ Definir mesmo assim",
    "btn_target_change_onb": "✏️ Alterar objetivo",
    "target_change_onb_prompt": "Digite outro peso alvo em kg, ex.: *70*",

    # goal labels (used in _finish_profile)
    "goal_label_lose": "Emagrecer",
    "goal_label_maintain": "Manter peso",
    "goal_label_gain": "Ganhar massa",

    # ── Profile goal buttons ──────────────────────────────────────
    "btn_goal_lose": "📉 Emagrecer",
    "btn_goal_maintain": "⚖️ Manter peso",
    "btn_goal_gain": "📈 Ganhar massa",
    "btn_sex_male": "👨 Masculino",
    "btn_sex_female": "👩 Feminino",
    "btn_activity_sedentary": "🪑 Sedentário (escritório, sem esporte)",
    "btn_activity_light": "🚶 Leve (1–2x por semana)",
    "btn_activity_moderate": "🏃 Moderada (3–5x por semana)",
    "btn_activity_active": "💪 Alta (todos os dias)",

    # ── Finish profile ────────────────────────────────────────────
    "profile_done": "✅ *Tudo pronto!*\n\n🎯 Objetivo: *{goal}*\n🔥 Calorias: *{low}–{high} kcal/dia*\n🥩 Proteína: *~{protein} g/dia*{target_line}\n\nApós cada refeição mostrarei quantas calorias ainda restam 🎯",
    "profile_target_line_remaining": "\n⚖️ Peso alvo: *{target} kg* (~{diff} kg restantes)",
    "profile_target_line_reached": "\n⚖️ Peso alvo: *{target} kg* — já atingido! 🏆",
    "ask_timezone": "🔔 *Vamos configurar lembretes de refeições!*\n\nVou te lembrar de registrar suas refeições — basta enviar uma foto ou descrever o que comeu.\n\nQue horas são aí agora? ex.: *23:15*",

    # ── Notifications ─────────────────────────────────────────────
    "notify_header": "⏰ *Configurações de lembretes*\n\n🌍 Fuso horário: {tz} (agora {time})\n\n☕ Café da manhã — {b_time} ({b})\n🍲 Almoço — {l_time} ({l})\n🍽️ Jantar — {d_time} ({d})\n\n⚠️ Recomendamos manter pelo menos 1 lembrete ativado",
    "btn_notif_all_on": "✅ Ativar todos",
    "btn_notif_all_off": "❌ Desativar todos",
    "btn_notif_change_tz": "🌍 Alterar fuso horário",
    "notif_enabled": "✅",
    "notif_disabled": "❌",
    "notif_breakfast": "☕ Café da manhã",
    "notif_lunch": "🍲 Almoço",
    "notif_dinner": "🍽️ Jantar",
    "notif_time_prompt": "⏰ Digite o novo horário de lembrete para *{meal}*\n\nFormato: *HH:MM*, ex.: *08:30*",
    "notif_timezone_prompt": "🕐 Digite que horas são aí agora, ex.: *23:15*\n\nVou determinar o fuso horário automaticamente.",
    "notif_timezone_updated": "✅ Fuso horário atualizado: UTC{sign}{offset}\n\n",
    "notif_time_updated": "✅ Horário de lembrete ({meal}) atualizado: *{time}*\n\n",
    "notif_time_bad": "❌ Não entendi o horário. Digite no formato *HH:MM*, ex.: *08:30*",
    "timezone_bad": "Não entendi 🤔 Digite o horário no formato *HH:MM*, ex.: *23:15*",
    "meal_name_breakfast": "café da manhã",
    "meal_name_lunch": "almoço",
    "meal_name_dinner": "jantar",
    "notif_tz_saved": "🔔 *Lembretes ativados!*\n\n🌍 Fuso horário: {tz}\n☕ Café da manhã — 9:00\n🍲 Almoço — 13:00\n🍽️ Jantar — 19:00\n\nConfigurar: /notify",
    "onb_tz_saved": "🔔 *Lembretes ativados!*\n\n🌍 Fuso horário: {tz}\n☕ Café da manhã — 9:00\n🍲 Almoço — 13:00\n🍽️ Jantar — 19:00\n\nConfigurar: /notify",
    "onb_tz_skip": "OK, sem lembretes 👌\nAtive quando quiser: /notify",
    "notif_snooze_done": "✅ Lembrete de {meal} desativado.\nReativar: /notify",

    # ── Timezone city names ───────────────────────────────────────
    "tz_kyiv": "🇺🇦 Kiev",
    "tz_moscow": "🇷🇺 Moscou",
    "tz_baku": "🇦🇿 Baku",
    "tz_almaty": "🇰🇿 Almaty",
    "tz_tashkent": "🇺🇿 Tashkent",
    "tz_novosibirsk": "Novosibirsk",
    "tz_irkutsk": "Irkutsk",
    "tz_vladivostok": "Vladivostok",
    "tz_skip": "❌ Pular",

    # ── Trial / Paywall ───────────────────────────────────────────
    "trial_exhausted": "❌ *Análises gratuitas esgotadas* (15 de 15)\n\nAssine para continuar contando calorias 👇",
    "trial_last_1": "⚠️ Resta *1 análise gratuita* de {limit} → /subscribe",
    "trial_last_few": "⚠️ Restam *{left} análises gratuitas* de {limit} → /subscribe",
    "trial_some_left": "🎁 {left} análises gratuitas restantes de {limit} → /subscribe",
    "trial_many_left": "🎁 Análises gratuitas: {left} de {limit}",
    "btn_subscribe": "💳 Assinar",
    "subscribe_remaining": "🎁 Análises gratuitas restantes: *{left} de {limit}*\n\n",
    "subscribe_exhausted": "❌ Análises gratuitas esgotadas\n\n",
    "subscribe_header": "💳 *Assinatura Meal Scan*\n\nEscolha um plano:",
    "subscribe_header_full": "💳 *Assinatura Meal Scan*\n\nContagem ilimitada de calorias de fotos e texto\n\nEscolha um plano:",
    "subscribe_active": "✅ *Assinatura ativa até {expires}*\n\nVocê pode renovar antecipadamente — o tempo será adicionado ao período atual:",
    "payment_success": "🎉 *Assinatura ativada por {label}!*\n\nConte calorias sem limites 🍽️\nEnvie uma foto ou descreva sua refeição ↓",
    "sub_1m_label": "1 mês",
    "sub_3m_label": "3 meses",
    "sub_invoice_title_1m": "Assinatura Meal Scan — 1 mês",
    "sub_invoice_title_3m": "Assinatura Meal Scan — 3 meses",
    "sub_invoice_desc": "Contagem ilimitada de calorias e macros de fotos e texto",
    "sub_invoice_error": "❌ Erro ao criar a fatura: {e}",

    # ── Delete command ────────────────────────────────────────────
    "delete_no_num": "❌ Indique o número da refeição.\nExemplo: `/delete 2`\n\nLista de hoje: /today",
    "delete_bad_num": "❌ O número deve ser inteiro. Por exemplo: `/delete 2`",
    "delete_no_meals": "📭 Sem refeições registradas hoje.",
    "delete_out_of_range": "❌ Sem refeição #{num}. Registros de hoje: {total}.\n\nVer lista: /today",
    "delete_done": "🗑️ Excluído: *{food}* ({cal} kcal)\n\n📊 Restante hoje: *{total_cal} kcal* ({n} refeições)",

    # ── Edit command ──────────────────────────────────────────────
    "edit_no_args": "✏️ Formato: `/edit número nova descrição`\nExemplo: `/edit 2 frango grelhado 400g`\n\nLista de hoje: /today",
    "edit_bad_num": "❌ Indique o número primeiro. Por exemplo: `/edit 2 sopa 400g`",
    "edit_no_meals": "📭 Sem refeições registradas hoje.",
    "edit_out_of_range": "❌ Sem refeição #{num}. Registros de hoje: {total}.",
    "edit_done": "✅ *Refeição #{num} atualizada*\n\n🍽️ {food}\n🔥 {cal} kcal | 🥩 {protein} g | 🧈 {fat} g | 🍞 {carbs} g\n\n📊 Hoje: *{total_cal} kcal* / 🥩 *{total_protein} g proteína*",

    # ── Delete from diary (callback) ──────────────────────────────
    "diary_deleted": "🗑️ Registro excluído.\n\n📊 Comido hoje: *{cal} kcal* / 🥩 *{protein} g proteína* ({n} refeições)\n{remaining}",
    "diary_cal_left": "🎯 Para atingir a meta: *{cal_left} kcal* e *{prot_left} g proteína*",
    "diary_cal_done": "✅ Meta calórica atingida!",
    "diary_cal_over": "⚠️ Meta superada em *{over} kcal*",

    # ── Reminders ─────────────────────────────────────────────────
    "reminder_text": "{emoji} Não esqueça de me contar o que comeu no {meal}!\nMeta: {goal_cal} kcal. Hoje: {total_cal} kcal\n\n📸 Envie uma foto ou escreva",
    "btn_reminder_add": "🍽️ Adicionar refeição",
    "btn_reminder_snooze": "❌ Não lembrar do {meal}",

    # ── Weight tip ────────────────────────────────────────────────
    "weight_tip": "⚖️ *Dica: monitore seu peso*\n\nVocê pode registrar seu peso toda manhã — o bot mostrará a evolução e o progresso em direção ao objetivo.\n\nDigite /weight e insira seu peso atual.\nGráfico de progresso: /progress",

    # ── Admin ─────────────────────────────────────────────────────
    "resetme_done": "✅ Todos os dados excluídos. Digite /start para começar de novo.",
    "gift_usage": "Uso: /gift <user_id>",
    "gift_bad_id": "❌ user_id deve ser um número",
    "gift_done": "✅ Usuário {uid} recebeu acesso permanente.",
    "error_terms": "❌ Erro: {e}",
    "error_invoice": "❌ Erro ao criar a fatura: {e}",
}
