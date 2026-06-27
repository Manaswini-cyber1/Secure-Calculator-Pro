# calculator.py

from exceptions import InvalidNumberError, DivisionByZeroError
from logger import log_history


class Calculator:

    def add(self, num1, num2):
        result = num1 + num2
        log_history(f"{num1} + {num2}", result)
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        log_history(f"{num1} - {num2}", result)
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        log_history(f"{num1} * {num2}", result)
        return result

    def divide(self, num1, num2):
        if num2 == 0:
            raise DivisionByZeroError()

        result = num1 / num2
        log_history(f"{num1} / {num2}", result)
        return result


def get_number(message):
    """
    Validate numeric input.
    """
    while True:
        try:
            value = float(input(message))
            return value

        except ValueError:
            raise InvalidNumberError("Please enter a valid numeric value.")