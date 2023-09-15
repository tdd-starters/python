"""String calculator."""
import sys


def evaluate(expression: str) -> int:
    """Evaluate a mathematical expression and return the result."""
    return 0


def main() -> None:
    """Calculate the value of a mathematical expression."""
    expression = " ".join(sys.argv[1:])
    print(f"{expression} = {evaluate(input)}")
