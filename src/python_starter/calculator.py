import sys


def evaluate(expression: str) -> int:
    """Evaluate a mathematical expression and return the result."""
    return 0


def main():
    input = " ".join(sys.argv[1:])
    print(f"{input} = {evaluate(input)}")
