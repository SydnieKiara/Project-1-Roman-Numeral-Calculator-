# src/main.py

# src/main.py

import re
import sys

roman_numerals = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

def roman_to_int(s):
    """
    Convert a Roman numeral to an integer.
    """
    total = 0
    prev_value = 0
    for char in reversed(s):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.
    """
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
    Calculate the result of a mathematical expression in Roman numerals.
    """
    # Remove spaces from the expression
    expression = expression.replace(" ", "")

    # Regex to split Roman numerals and operators (+, -, *, /)
    tokens = re.findall(r'[IVXLCDM]+|\+|\-|\*|\/', expression)

    # Convert Roman numerals to integers and keep track of operations
    operands = []
    operators = []

    for token in tokens:
        if token in roman_numerals:  # It's a Roman numeral
            operands.append(roman_to_int(token))
        else:  # It's an operator
            operators.append(token)

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
            result //= operands[i + 1]  # Use floor division to avoid decimals

    # Convert the result back to a Roman numeral
    return int_to_roman(result)

if __name__ == "__main__":
    expression = " ".join(sys.argv[1:])
    result = calculate(expression)
    print(result)

