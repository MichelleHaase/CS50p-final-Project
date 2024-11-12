from project import get_level, get_word, guessing, graphics
import pytest


def test_get_level(monkeypatch):
    # the monkey patch overrides the builtin input function which allows to test it.
    monkeypatch.setattr("builtins.input", lambda _: "1")
    result = get_level()
    assert result == "1"

    monkeypatch.setattr("builtins.input", lambda _: "2")
    result = get_level()
    assert result == "2"

    monkeypatch.setattr("builtins.input", lambda _: "3")
    result = get_level()
    assert result == "3"

    # inputs is a list of wrong inputs where the function should repromt the user ending in a right input, only if
    # after each wrong input the function reprompts the last(right) input is reached and the test evaluates to True
    inputs = iter(
        ["a", "one", "yes", "?", ",.", "Michelle", "[]", "()", 4, 126384, "1"]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_level()
    assert result == "1"


def test_get_word():
    # results saves the random word and the number of tries and is idexable
    # since the word is random i only check if it's a str of the wanted lenght
    result = get_word("1")
    assert isinstance(result[0], str)
    assert len(result[0]) > 3 and len(result[0]) < 6
    assert result[1] == 10

    result = get_word("2")
    assert isinstance(result[0], str)
    assert len(result[0]) > 5 and len(result[0]) < 9
    assert result[1] == 12

    result = get_word("3")
    assert isinstance(result[0], str)
    assert len(result[0]) > 8 and len(result[0]) < 13
    assert result[1] == 15

    with pytest.raises(UnboundLocalError):
        get_word(2)

    with pytest.raises(UnboundLocalError):
        get_word(24554)

    with pytest.raises(UnboundLocalError):
        get_word("lala")


def test_guessing(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "banana")
    with pytest.raises(SystemExit) as text:
        guessing("banana", 1, 10)
    assert text.value.code == "banana is right!!\n🎉🎉🎉 !!You Won!! 🥳 🎉🎉🎉"

    inputs = iter(["b", "n", "a"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SystemExit) as text:
        guessing("banana", 1, 10)
    assert text.value.code == "banana is right!!\n🎉🎉🎉 !!You Won!! 🥳 🎉🎉🎉"


def test_graphics():
    assert (
        graphics(1, "1")
        == """
    ____|_____"""
    )
    assert (
        graphics(1, "2")
        == """
    ____|_____"""
    )
    assert (
        graphics(1, "3")
        == """
    ____|_____"""
    )
    assert (
        graphics(10, "1")
        and graphics(12, "2")
        and graphics(15, "3")
        == """
        ________
        |       |
        |       0
        |      /|\\
        |       |
        |      / \\
    ____|_____ """
    )

    assert graphics(12, "1") == None
    assert graphics(14, "2") == None
    assert graphics(16, "3") == None

    assert graphics(16, 3) == None
    assert graphics("Lala", "LULU") == None
    assert graphics(16, "5") == None
    with pytest.raises(TypeError):
        graphics(12)
    with pytest.raises(TypeError):
        graphics()
    with pytest.raises(TypeError):
        graphics(12, 5, 13)
