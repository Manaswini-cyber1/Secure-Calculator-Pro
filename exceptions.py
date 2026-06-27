# exceptions.py

class CalculatorError(Exception):
    """Base class for calculator exceptions."""
    pass


class InvalidChoiceError(CalculatorError):
    """Raised when the user enters an invalid menu choice."""
    def __init__(self, message="Invalid menu choice! Please choose a valid option."):
        super().__init__(message)


class InvalidNumberError(CalculatorError):
    """Raised when the user enters an invalid number."""
    def __init__(self, message="Invalid number entered!"):
        super().__init__(message)


class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted."""
    def __init__(self, message="Division by zero is not allowed!"):
        super().__init__(message)