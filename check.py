# check.py: tests for reading data/subscribers.csv
# The tests are written BEFORE the code. The functions do not exist yet.


def read_subscribers(path: str) -> str:
    with open(path, encoding="utf-8") as file:
        text = file.read()
    return text

text = read_subscribers("data/subscribers.csv")

assert isinstance(text, str)

assert count_emails(text) == 24
assert count_in_group(text, "daily-drinkers") == 8
assert count_in_group(text, "tea-curious") == 8
assert count_in_group(text, "gift-buyers") == 8

print("All checks passed")
