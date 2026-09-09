from datetime import datetime
import os

LOG_PATH = "data/user_logs.txt"

def log_action(action, log_file=LOG_PATH):
    """Append a user action with a timestamp to the log file."""
    timestamp = datetime.now().strftime("%Y-&m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"[{timestamp}] {action}\n")

def search_logs(keyword, log_file=LOG_PATH):
    """Search the log file for lines that match a keyword."""
    pass

log_action("User logged in")
log_action("User updated profile")