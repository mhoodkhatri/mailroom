# mailroom.py: functions for reading subscribers, and a small command.
# Run it:  uv run python mailroom.py subscribers
import sys


def read_subscribers(path: str) -> str:
    with open(path, encoding="utf-8") as file:
        text = file.read()
    return text


def count_emails(text: str) -> int:
    count = 0
    for line in text.splitlines():
        if line.strip():
            count = count + 1
    return count - 1


def count_in_group(text: str, group: str) -> int:
    count = 0
    for line in text.splitlines():
        if line.strip():
            parts = line.split(",")
            if parts[3] == group:
                count = count + 1
    return count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please type a command, for example: subscribers")
    elif sys.argv[1] == "subscribers":
        text = read_subscribers("data/subscribers.csv")
        print("Total emails:")
        print(count_emails(text))
        for group in ["daily-drinkers", "tea-curious", "gift-buyers"]:
            print(group)
            print(count_in_group(text, group))
    else:
        print("Unknown command")
