# Day 10 - Python Programming Course

# Today we will cover functions in Python. A function is a reusable block of
# code that runs when you call it.

# def starts a function definition. The indented lines belong to the function.

def greet():
	print("Hello! Welcome to Python.")


# Call the function by writing its name followed by parentheses.

greet()

# A parameter is a variable listed in a function definition. An argument is
# the value you pass to that parameter when you call the function.

def greet_student(name):
	print(f"Hello, {name}!")


greet_student("Aazar")

# A function can have more than one parameter.

def show_student(name, course):
	print(f"{name} is learning {course}.")


show_student("Sara", "Python")

# return sends a result back to the code that called the function.

def add(number_1, number_2):
	return number_1 + number_2


sum_result = add(5, 3)
print("The sum is:", sum_result)

# A default parameter value is used when you do not provide an argument.

def make_greeting(name, greeting="Hello"):
	return f"{greeting}, {name}!"


print(make_greeting("Mina"))
print(make_greeting("Omar", "Good morning"))

# Day 10 Project: Build a calculator by placing each operation in a function.

def calculator(number_1, number_2, operator):
	if operator == "+":
		return number_1 + number_2
	elif operator == "-":
		return number_1 - number_2
	elif operator == "*":
		return number_1 * number_2
	elif operator == "/":
		if number_2 != 0:
			return number_1 / number_2
		return "Error: Division by zero is not allowed."
	else:
		return "Invalid operator."


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
chosen_operator = input("Enter an operator (+, -, *, /): ")

result = calculator(first_number, second_number, chosen_operator)
print("Result:", result)
