# src/main.py
import sys
from calculator import evaluate_expression

def main():
    """Main function to take input and calculate the result."""
    if len(sys.argv) < 2:
        print("I don’t know how to read this.")
        return

    # Join command line arguments into a single expression string
    expression = " ".join(sys.argv[1:])
    result = evaluate_expression(expression)
    print(result)

if __name__ == "__main__":
    main()
