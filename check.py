# check.py: tests for reading data/subscribers.csv
# The tests are written BEFORE the code. The functions do not exist yet.


def read_subscribers(path: str) -> str:
    with open(path, encoding="utf-8") as file:
        text = file.read()
    return text


def count_emails(text: str) -> int:
    lines = text.split("\n")
    return len(lines) - 1


def count_in_group(text: str, group: str) -> int:
    count = 0
    for line in text.split("\n"):
        parts = line.split(",")
        if parts[3] == group:
            count = count + 1
    return count

text = read_subscribers("data/subscribers.csv")

assert isinstance(text, str)

assert count_emails(text) == 24
assert count_in_group(text, "daily-drinkers") == 8
assert count_in_group(text, "tea-curious") == 8
assert count_in_group(text, "gift-buyers") == 8

print("All checks passed")
