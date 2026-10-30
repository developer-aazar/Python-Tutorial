# Day 22 - Python Programming Course

# Today we will cover regular expressions. The re module can search text for
# patterns such as digits, words, or email-like text.

import re

message = "Call 555-0134 or 555-0198 after 5 pm."

# findall() returns every match for a pattern. \d means a digit, and {4}
# means exactly four repetitions.

phone_numbers = re.findall(r"\d{3}-\d{4}", message)
print("Phone numbers:", phone_numbers)

# search() returns the first match, or None when there is no match.

match = re.search(r"\d+ pm", message)
if match:
	print("Time mentioned:", match.group())

# sub() replaces text that matches a pattern.

hidden_numbers = re.sub(r"\d", "*", message)
print("Hidden numbers:", hidden_numbers)

# Raw strings (starting with r) make patterns with backslashes easier to read.

# Day 22 Project: Find email-shaped strings in a line of text.

text = input("Enter text that may contain email addresses: ")
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
email_addresses = re.findall(email_pattern, text)

if email_addresses:
	print("Email addresses found:", email_addresses)
else:
	print("No email addresses found.")
