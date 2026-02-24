
from datetime import datetime


LOG_PATH = "../data/user_logs.txt"

def log_action(action, log_file=LOG_PATH):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"[{timestamp}] {action}\n")

    # print(log_action("User logged in"))
    # print(log_action("User updated profile"))


def search_logs(keyword, log_file=LOG_PATH):
    try:
        with open(log_file, "r") as file:
            matches = [line.strip() for line in file if keyword.lower() in line.lower()]
            if matches:
                print("\nFiltered Logs:")
                for match in matches:
                    print(match)
            else:
                print("No matching log entries found.")
    except FileNotFoundError:
        print("Log file not found.")