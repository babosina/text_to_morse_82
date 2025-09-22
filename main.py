from constants import MORSE_CODE_DICT, FROM_MORSE_CODE_DICT


def text_to_morse(text: str) -> str:
    """
    Converts text to a morse code string

    Arguments:
        text {string} -- text to convert

    Returns:
        str -- morse code string
    """
    morse_code = []
    for char in text.upper():
        if char not in MORSE_CODE_DICT:
            morse_code.append('?')
        else:
            morse_code.append(MORSE_CODE_DICT.get(char))

    return " ".join(morse_code)


def morse_to_text(text: str) -> str:
    """
    Converts morse code string to text

    Arguments:
        text {string} -- morse code string

    Returns:
        str -- text converted from morse code string
    """
    from_morse = text.split(" ")
    result = []
    for char in from_morse:
        if char in FROM_MORSE_CODE_DICT:
            result.append(FROM_MORSE_CODE_DICT.get(char))
        else:
            result.append(char)
    return "".join(result)
