# report.py

from collections import Counter

HISTORY_FILE = "history.txt"
ERROR_FILE = "error_log.txt"


class Report:

    def generate_report(self):
        total_calculations = 0
        total_errors = 0
        error_types = []

        # Count calculations
        try:
            with open(HISTORY_FILE, "r") as file:
                history = file.readlines()
                total_calculations = len(history)
        except FileNotFoundError:
            total_calculations = 0

        # Count errors
        try:
            with open(ERROR_FILE, "r") as file:
                errors = file.readlines()
                total_errors = len(errors)

                for line in errors:
                    parts = line.strip().split("|")
                    if len(parts) > 1:
                        error_types.append(parts[-1].strip())

        except FileNotFoundError:
            total_errors = 0

        print("\n========== REPORT ==========")
        print(f"Total Calculations : {total_calculations}")
        print(f"Total Errors       : {total_errors}")

        if error_types:
            common = Counter(error_types).most_common(1)[0]
            print(f"Most Common Error  : {common[0]}")
        else:
            print("Most Common Error  : None")

        print("============================\n")