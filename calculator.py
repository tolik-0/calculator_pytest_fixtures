from __future__ import annotations


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers (a - b)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers (a / b).

    Raises:
        ZeroDivisionError: If the second argument is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def int_divide(a: int, b: int) -> int:
    """Return the integer division result of two numbers (a // b).

    Raises:
        ZeroDivisionError: If the second argument is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Integer division by zero is not allowed.")
    return a // b


def modulo(a: int, b: int) -> int:
    """Return the remainder of integer division (a % b).

    Raises:
        ZeroDivisionError: If the second argument is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Modulo by zero is not allowed.")
    return a % b


def main() -> None:
    """Simple CLI for interacting with the calculator."""
    print("Calculator CLI. Type 'quit' to exit.")
    print("Supported operators: +, -, *, /, //, %")
    while True:
        expression = input("Enter expression (a op b): ").strip()
        if expression.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        try:
            a_str, op, b_str = expression.split()
            a = float(a_str)
            b = float(b_str)
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            elif op == "//":
                result = int_divide(int(a), int(b))
            elif op == "%":
                result = modulo(int(a), int(b))
            else:
                print("Unsupported operator. Use +, -, *, /, // or %.")
                continue
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Use format: number operator number")
        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()