# main.py

from calculator import Calculator, get_number
from logger import view_history, view_errors, log_error
from report import Report
from exceptions import (
    InvalidChoiceError,
    InvalidNumberError,
    DivisionByZeroError
)


def menu():
    print("\n========== Secure Calculator Pro ==========")
    print("1. Perform Calculation")
    print("2. View Calculation History")
    print("3. View Error Report")
    print("4. Generate Summary Report")
    print("5. Exit")
    print("===========================================")


def perform_calculation():
    calc = Calculator()

    print("\nOperations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        operation = input("Choose operation (1-4): ")

        if operation not in ["1", "2", "3", "4"]:
            raise InvalidChoiceError()

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if operation == "1":
            result = calc.add(num1, num2)

        elif operation == "2":
            result = calc.subtract(num1, num2)

        elif operation == "3":
            result = calc.multiply(num1, num2)

        else:
            result = calc.divide(num1, num2)

    except InvalidChoiceError as e:
        print(e)
        log_error(str(e))

    except InvalidNumberError as e:
        print(e)
        log_error(str(e))

    except DivisionByZeroError as e:
        print(e)
        log_error(str(e))

    except Exception as e:
        print("Unexpected Error:", e)
        log_error(str(e))

    else:
        print("Result =", result)

    finally:
        print("Operation Completed.\n")


def main():

    report = Report()

    while True:

        menu()

        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                perform_calculation()

            elif choice == "2":
                view_history()

            elif choice == "3":
                view_errors()

            elif choice == "4":
                report.generate_report()

            elif choice == "5":
                print("\nThank you for using Secure Calculator Pro.")
                break

            else:
                raise InvalidChoiceError()

        except InvalidChoiceError as e:
            print(e)
            log_error(str(e))

        finally:
            print("-" * 45)


if __name__ == "__main__":
    main()