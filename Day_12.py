# Day 12 - Python Programming Course

# Today we will cover exceptions in Python. An exception is an error that
# happens while a program is running. try and except let you handle expected
# errors so the program can continue gracefully.

# Converting invalid text to a number raises a ValueError.

try:
	age = int("twenty")
except ValueError:
	print("That text is not a valid whole number.")

# You can use else for code that should run only when no exception occurred.

try:
	age = int(input("Enter your age: "))
except ValueError:
	print("Please enter your age using digits.")
else:
	if age >= 18:
		print("You are an adult.")
	else:
		print("You are under 18.")

# Use finally for cleanup code that should run whether an error happened or not.

try:
	print("Starting a small calculation...")
	answer = 10 / 2
except ZeroDivisionError:
	print("A number cannot be divided by zero.")
else:
	print("Answer:", answer)
finally:
	print("Calculation finished.")

# Catch specific exceptions instead of hiding every possible problem with a
# bare except. This makes errors easier to understand and fix.

# Day 12 Project: Divide two numbers and handle invalid input and division by 0.

try:
	first_number = float(input("Enter the first number: "))
	second_number = float(input("Enter the second number: "))
	result = first_number / second_number
except ValueError:
	print("Please enter valid numbers.")
except ZeroDivisionError:
	print("The second number cannot be zero.")
else:
	print("Result:", result)
