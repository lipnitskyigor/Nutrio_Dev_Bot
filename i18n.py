from locales import SUPPORTED, DEFAULT_LANG


def detect_lang(language_code: str | None) -> str:
    if not language_code:
        return DEFAULT_LANG
    if language_code.startswith("ru"):
        return "ru"
    if language_code.startswith("de"):
        return "de"
    if language_code.startswith("pl"):
        return "pl"
    if language_code.startswith("es"):
        return "es"
    if language_code.startswith("pt"):
        return "pt"
    if language_code.startswith("ar"):
        return "ar"
    return DEFAULT_LANG


def t(lang: str, key: str, **kwargs) -> str:
    texts = SUPPORTED.get(lang, SUPPORTED[DEFAULT_LANG])
    text = texts.get(key) or SUPPORTED[DEFAULT_LANG].get(key) or key
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, ValueError):
            pass
    return text
