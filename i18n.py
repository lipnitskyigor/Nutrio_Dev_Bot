from locales import SUPPORTED, DEFAULT_LANG


def detect_lang(language_code: str | None) -> str:
    if language_code and language_code.startswith("ru"):
        return "ru"
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
