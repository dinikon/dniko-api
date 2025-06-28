language_timezone_mapping = {
    "en-US": "America/New_York",
    "ru-RU": "Europe/Moscow",
    "uk-UA": "Europe/Kyiv",
    "pl-PL": "Europe/Warsaw",
}

languages = list(language_timezone_mapping.keys())


def supported_language(lang):
    if lang in languages:
        return lang

    error = "{lang} is not a valid language.".format(lang=lang)
    raise ValueError(error)
