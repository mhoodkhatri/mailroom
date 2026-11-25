# check.py: tests for the functions in mailroom.py
from mailroom import read_subscribers, count_emails, count_in_group

text = read_subscribers("data/subscribers.csv")

assert isinstance(text, str)

assert count_emails(text) == 24
assert count_in_group(text, "daily-drinkers") == 8
assert count_in_group(text, "tea-curious") == 8
assert count_in_group(text, "gift-buyers") == 8

# count_emails must give the same answer with or without a newline at the end
assert count_emails("header\nAyesha\nTom") == 2
assert count_emails("header\nAyesha\nTom\n") == 2

print("All checks passed")
