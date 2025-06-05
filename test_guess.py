import pytest
import random
from guess import think_of_number, make_guess, check_guess

def test_think_of_number_returns_int(monkeypatch):
    """
    Tests that think_of_number returns an integer type.
    """

    number = think_of_number()
    assert isinstance(number, int)

def test_think_of_number_returns_expected_value(monkeypatch):
    """
    Tests that function calls random.randint and returns its result.
    """

    expected_number = 42

    monkeypatch.setattr(random, 'randint', lambda a, b: expected_number)
    result = think_of_number()
    assert result == expected_number

def test_think_of_number_calls_randint_with_correct_args(monkeypatch):
    """
    Tests that think_of_number calls random.randint with arguments 1 and 100.
    """
    mock_randint_called_with = None

    def mock_randint(a, b):
        nonlocal mock_randint_called_with
        mock_randint_called_with = (a, b)
        return 50
    
    monkeypatch.setattr(random, 'randint', mock_randint)

    think_of_number()

    assert mock_randint_called_with == (1, 100)


def test_make_guess_valid_input(monkeypatch):
    """
    Tests that make_guess returns a valid number when correct input is provided.
    """
    
    monkeypatch.setattr('builtins.input', lambda _: '50')
    assert make_guess() == 50

def test_make_guess_lower_bound_input(monkeypatch):
    """
    Tests that make_guess returns 1 when 1 is provided.
    """

    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert make_guess() == 1

def test_make_guess_upper_bound_input(monkeypatch):
    """
    Tests that make_guess returns 100 when 100 is provided.
    """

    monkeypatch.setattr('builtins.input', lambda _: '100')
    assert make_guess() == 100

def test_make_guess_invalid_then_valid_out_of_range_low(monkeypatch, capsys):
    """
    Tests that make_guess handles out-of-range low input, prints error,
    and then accepts valid input.
    """

    inputs = iter(['0', '50']) 
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_guess()
    assert result == 50
    
    captured = capsys.readouterr()
    assert "ERROR" not in captured.out 


def test_make_guess_invalid_then_valid_out_of_range_high(monkeypatch, capsys):
    """
    Tests that make_guess handles out-of-range high input, prints error,
    and then accepts valid input.
    """

    inputs = iter(['101', '75'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_guess()

    assert result == 75
    
    captured = capsys.readouterr()
    assert "ERROR" not in captured.out

def test_check_guess_correct(capsys):
    """
    Tests that check_guess correctly identifies a correct guess,
    prints the win message, and returns True for end_game.
    """

    user_guess, sphinx_number, attempts_left = 50, 50, 5

    new_attempts, end_game = check_guess(user_guess, sphinx_number, attempts_left)

    assert new_attempts == attempts_left  # Attempts should not decrease on correct guess
    assert end_game is True

    captured = capsys.readouterr()
    assert f"You got it! The answer was {sphinx_number}." in captured.out

def test_check_guess_too_high(capsys):
    """
    Tests that check_guess correctly identifies a 'too high' guess,
    prints the message, decreases attempts, and returns False for end_game.
    """

    user_guess, sphinx_number, attempts_left = 75, 50, 5

    new_attempts, end_game = check_guess(user_guess, sphinx_number, attempts_left)

    assert new_attempts == attempts_left - 1
    assert end_game is False

    captured = capsys.readouterr()
    assert "Too high." in captured.out

def test_check_guess_too_low(capsys):
    """
    Tests that check_guess correctly identifies a 'too low' guess,
    prints the message, decreases attempts, and returns False for end_game.
    """

    user_guess, sphinx_number, attempts_left = 25, 50, 5

    new_attempts, end_game = check_guess(user_guess, sphinx_number, attempts_left)

    assert new_attempts == attempts_left - 1
    assert end_game is False

    captured = capsys.readouterr()
    assert "Too low." in captured.out

def test_check_guess_last_attempt_too_high(capsys):
    """
    Tests that if attempts_left becomes 0 after a 'too high' guess,
    end_game is True.
    """

    user_guess, sphinx_number, attempts_left = 75, 50, 1

    new_attempts, end_game = check_guess(user_guess, sphinx_number, attempts_left)

    assert new_attempts == 0
    assert end_game is True # Game should end

    captured = capsys.readouterr()
    assert "Too high." in captured.out

def test_check_guess_last_attempt_too_low(capsys):
    """
    Tests that if attempts_left becomes 0 after a 'too low' guess,
    end_game is True.
    """

    user_guess, sphinx_number, attempts_left = 25, 50, 1

    new_attempts, end_game = check_guess(user_guess, sphinx_number, attempts_left)

    assert new_attempts == 0
    assert end_game is True # Game should end

    captured = capsys.readouterr()
    assert "Too low." in captured.out

def test_check_guess_multiple_attempts_remain(capsys):
    """
    Tests that if attempts_left is > 0 after a wrong guess,
    end_game is False.
    """

    user_guess, sphinx_number, attempts_left = 40, 50, 2

    new_attempts, end_game = check_guess(user_guess, sphinx_number, attempts_left)

    assert new_attempts == 1
    assert end_game is False

    captured = capsys.readouterr()
    assert "Too low." in captured.out