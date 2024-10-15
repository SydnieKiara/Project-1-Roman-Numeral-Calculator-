# tests/test_main.py

from main import roman_to_int, int_to_roman, calculate

def test_roman_to_int():
    """
    Test the roman_to_int function.
    """
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994

def test_int_to_roman():
    """
    Test the int_to_roman function.
    """
    assert int_to_roman(3) == "III"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(9) == "IX"
    assert int_to_roman(58) == "LVIII"
    assert int_to_roman(1994) == "MCMXCIV"


