# src/main.py

import re
import sys

roman_numerals = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

def roman_to_int(s):
    """
    Convert a Roman numeral string to its integer equivalent.

    Args:
        s (str): A string representing a Roman numeral (e.g., 'X', 'IV', 'MMCDXL').

    Returns:
        int: The integer equivalent of the Roman numeral.

    Raises:
        ValueError: If the input contains an invalid Roman numeral character.

    Example:
        roman_to_int('X') -> 10
        roman_to_int('IV') -> 4
    """
    total = 0
    prev_value = 0
    for char in reversed(s):
        value = roman_numerals.get(char, None)
        if value is None:
            raise ValueError(f"Invalid Roman numeral character: {char}")
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

def int_to_roman(num):
    """
    Convert an integer to its Roman numeral string equivalent.

    Args:
        num (int): An integer to be converted (must be between 1 and 3999).

    Returns:
        str: The Roman numeral representation of the integer.

    Raises:
        ValueError: If the number is outside the valid range (1 to 3999).

    Example:
        int_to_roman(10) -> 'X'
        int_to_roman(1994) -> 'MCMXCIV'
    """
    if num < 1 or num > 3999:
        raise ValueError("Integer out of range (must be between 1 and 3999)")

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def calculate(expression):
    """
    Evaluate a mathematical expression where Roman numerals are used instead of integers.

    This function parses an expression containing Roman numerals and basic arithmetic
    operators (+, -, *, /), calculates the result, and returns the result in Roman numeral form.

    Args:
        expression (str): A mathematical expression using Roman numerals (e.g., 'X + V - II').

    Returns:
        str: The result of the expression, represented as a Roman numeral.

    Raises:
        ValueError: If the expression is empty or contains invalid Roman numerals or operators.
        ZeroDivisionError: If a division by zero occurs in the expression.

    Example:
        calculate('X + V') -> 'XV'
        calculate('X * II') -> 'XX'
    """
    # Remove spaces from the expression
    expression = expression.replace(" ", "")

    # Regex to split Roman numerals and operators (+, -, *, /)
    tokens = re.findall(r'[IVXLCDM]+|\+|\-|\*|\/', expression)

    if not tokens:
        raise ValueError("Invalid or empty expression")

    # Convert Roman numerals to integers and keep track of operations
    operands = []
    operators = []

    for token in tokens:
        if token in roman_numerals or re.match(r'[IVXLCDM]+', token):  # It's a Roman numeral
            operands.append(roman_to_int(token))
        elif token in ['+', '-', '*', '/']:  # It's an operator
            operators.append(token)
        else:
            raise ValueError(f"Invalid token in expression: {token}")

    if not operands:
        raise ValueError("No Roman numerals in expression")

    if len(operands) - 1 != len(operators):
        raise ValueError("Mismatched number of operands and operators")

    # Start with the first operand
    result = operands[0]

    # Perform operations in order of appearance (for simplicity)
    for i, operator in enumerate(operators):
        if operator == '+':
            result += operands[i + 1]
        elif operator == '-':
            result -= operands[i + 1]
        elif operator == '*':
            result *= operands[i + 1]
        elif operator == '/':
            if operands[i + 1] == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result //= operands[i + 1]  # Use floor division to avoid decimals

    # Convert the result back to a Roman numeral
    return int_to_roman(result)

if __name__ == "__main__":
    """
    Main function to run the script from the command line. 
    It expects a Roman numeral expression as an argument.

    Usage:
        python main.py "X + V"
    
    Args:
        expression (str): A Roman numeral expression passed from the command line.

    Example:
        python main.py "X + II" -> XV
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py '<expression>'")
        sys.exit(1)

    expression = " ".join(sys.argv[1:])
    try:
        result = calculate(expression)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

