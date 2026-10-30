# Day 21 - Python Programming Course

# Today we will cover decorators. A decorator is a function that takes another
# function and returns a new function with extra behavior.

def announce(function):
	def wrapper():
		print("Starting the function...")
		function()
		print("Function finished.")
	return wrapper


# The @ syntax applies a decorator when the function is defined.

@announce
def say_hello():
	print("Hello!")


say_hello()

# A decorator can also pass arguments and return values through to the original
# function. *args and **kwargs collect positional and named arguments.

def show_call(function):
	def wrapper(*args, **kwargs):
		print(f"Calling {function.__name__}")
		return function(*args, **kwargs)
	return wrapper


@show_call
def multiply(first_number, second_number):
	return first_number * second_number


print("Product:", multiply(4, 5))

# Day 21 Project: Decorate a greeting function so it prints a welcome message
# before the personalized greeting.

def welcome_message(function):
	def wrapper(name):
		print("Welcome to the Python club!")
		return function(name)
	return wrapper


@welcome_message
def greet_member(name):
	print(f"Nice to meet you, {name}.")


greet_member("Aazar")
