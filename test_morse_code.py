from main import text_to_morse, morse_to_text


def test_text_to_morse():
    assert text_to_morse("Python") == ".--. -.-- - .... --- -."
    assert text_to_morse("@#^ Test 42") == ".--.-. ? ? / - . ... - / ....- ..---"


def test_morse_to_text():
    assert morse_to_text(".--. -.-- - .... --- -.") == "PYTHON"
    assert morse_to_text(".--.-. / - . ... - / ....- ..---") == "@ TEST 42"
