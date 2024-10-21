def replace_letters(raw_text: str) -> str:
    '''Replace english letters in text to russian letters'''
    replacements = {
        "a": "а",
        "b": "в",
        "c": "с",
        "e": "е",
        "h": "н",
        "k": "к",
        "m": "м",
        "o": "о",
        "p": "р",
        "t": "т",
        "y": "у",
        "x": "х",
    }

    translation_table = str.maketrans(replacements)
    return raw_text.translate(translation_table)