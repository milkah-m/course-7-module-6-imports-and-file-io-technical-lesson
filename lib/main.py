# lib/main.py

import argparse
from logger import log_action, search_logs

# If you run `python lib/main.py`, you should see a list of the commands you can run:
# * log
# * search

# Try running these in the terminal, such as:
# `python lib/main.py log "testing code"`
# `python lib/main.py log "deploying code"`
# `python lib/main.py log "patching code"`

# If you search for 'code'you should see all of these printed to the terminal:
# `python lib/main.py search "code"`

# If you search for 'deploying' or 'testing' however, you will only see the one that includes that word.

# You should also be able to view your logs in `data/user_logs.txt`
def main():
    parser = argparse.ArgumentParser(description="User Log Management CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Log subcommand
    log_parser = subparsers.add_parser("log", help="Log a user action")
    log_parser.add_argument("action", type=str, help="The action to log")

    # Search subcommand
    search_parser = subparsers.add_parser("search", help="Search log file")
    search_parser.add_argument("keyword", type=str, help="Keyword to search in logs")

    args = parser.parse_args()

    if args.command == "log":
        log_action(args.action)
    elif args.command == "search":
        search_logs(args.keyword)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# git checkout -b feature-logging-system