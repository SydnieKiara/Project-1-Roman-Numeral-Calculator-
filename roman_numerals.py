# src/roman_numerals.py

class RomanNumeralError(Exception):
    """Custom exception for invalid Roman numeral operations."""
    pass

roman_to_int_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

int_to_roman_map = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

def roman_to_int(roman):
    """Convert a Roman numeral to an integer."""
    total = 0
    prev_value = 0

    for char in reversed(roman):
        if char not in roman_to_int_map:
            raise RomanNumeralError(f"Invalid Roman numeral character: {char}")
        
        value = roman_to_int_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

def int_to_roman(num):
    """Convert an integer to a Roman numeral."""
    if num <= 0 or num > 3999:
        raise RomanNumeralError(f"Value out of range: {num}. Must be between 1 and 3999.")

    result = []
    for value, symbol in int_to_roman_map:
        while num >= value:
            result.append(symbol)
            num -= value

    return ''.join(result)
