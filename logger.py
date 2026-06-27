from datetime import datetime

HISTORY_FILE = "history.txt"
ERROR_FILE = "error_log.txt"


def log_history(expression, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{datetime.now()} | {expression} = {result}\n")


def log_error(error_message):
    with open(ERROR_FILE, "a") as file:
        file.write(f"{datetime.now()} | {error_message}\n")


def view_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            data = file.read()
            if data.strip():
                print("\n===== Calculation History =====")
                print(data)
            else:
                print("\nNo calculation history found.")
    except FileNotFoundError:
        print("\nHistory file not found.")


def view_errors():
    try:
        with open(ERROR_FILE, "r") as file:
            data = file.read()
            if data.strip():
                print("\n===== Error Report =====")
                print(data)
            else:
                print("\nNo errors recorded.")
    except FileNotFoundError:
        print("\nError log file not found.")