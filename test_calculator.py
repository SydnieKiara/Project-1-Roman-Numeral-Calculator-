# tests/test_calculator.py
import pytest
from src.calculator import evaluate_expression

def test_addition():
    assert evaluate_expression("V + V") == "X"

def test_subtraction():
    assert evaluate_expression("X - V") == "V"

def test_multiplication():
    assert evaluate_expression("(X + V) * II") == "XXX"

def test_invalid_roman():
    assert evaluate_expression("IIII") == "Error: Invalid Roman numeral character: I"

def test_out_of_range():
    assert evaluate_expression("MMM + M") == "You're going to need a bigger calculator."

def test_fractional_result():
    assert evaluate_expression("V / II") == "There is no concept of a fractional number in Roman numerals."
