# tests/test_main.py

import pytest
from main import roman_to_int, int_to_roman, calculate

def test_roman_to_int_basic():
    """
    Test basic conversion from Roman numeral to integer.
    """
    assert roman_to_int("I") == 1
    assert roman_to_int("V") == 5
    assert roman_to_int("X") == 10

def test_int_to_roman_basic():
    """
    Test basic conversion from integer to Roman numeral.
    """
    assert int_to_roman(1) == "I"
    assert int_to_roman(5) == "V"
    assert int_to_roman(10) == "X"

# I used " python -m pytest " to run the tests in the terminal
