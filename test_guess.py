import pytest
import random
from guess import think_of_number, make_guess

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

