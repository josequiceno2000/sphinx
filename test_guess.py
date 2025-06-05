import pytest
import random
from guess import think_of_number

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