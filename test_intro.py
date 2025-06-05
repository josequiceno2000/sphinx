import pytest
from intro import choose_difficulty

def test_choose_difficulty_easy(monkeypatch):
    """
    Tests that choose_difficulty returns 'eas'y when the user inputs 'easy'.
    """

    monkeypatch.setattr('builtins.input', lambda _: 'easy')
    assert choose_difficulty() == 'easy'
    
def test_choose_difficulty_hard(monkeypatch):
    """
    Tests that choose_difficulty returns 'hard' when the user inputs 'hard'.
    """

    monkeypatch.setattr('builtins.input', lambda _: 'hard')
    assert choose_difficulty() == 'hard'

def test_choose_difficulty_invalid_then_valid(monkeypatch, capsys):
    """
    Tests that choose_difficulty handles invalid input followed by valid input, and prints the correct error message for invalid input.
    """

    inputs = iter(['poopfart', 'easy'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = choose_difficulty()

    assert result == 'easy'

    captured = capsys.readouterr()
    assert "\nINVALID: you must type either 'easy' or 'hard'\n" in captured.out