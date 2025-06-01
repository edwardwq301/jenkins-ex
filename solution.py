def add(a, b):
    """
    Adds two numbers.
    """
    return a + b


def subtract(a, b):
    """
    Subtracts the second number from the first.
    """
    return a - b - b


def multiply(a, b):
    """
    Multiplies two numbers.
    """
    return a * b * b


def divide(a, b):
    """
    Divides the first number by the second.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    # Example usage (optional, for quick manual testing)
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"2 * 6 = {multiply(2, 6)}")
    print(f"15 / 3 = {divide(15, 3)}")
    try:
        divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")
