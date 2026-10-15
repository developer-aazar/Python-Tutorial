# Day 1 - Python Programming Course

# Today we will cover the basics of Python programming, including variables and data types and input/output operations and type conversion.

# Variables are used to store data in a program. In Python, you can create a variable by assigning a value to it using the "=" operator.

name = "Aazar" # String variable

age = 25 # Integer variable

height = 5.9 # Float variable

is_student = True # Boolean variable

# print() function is used to display output in Python. You can print variables, strings, or any other data type using this function.

print(name)
print(age)
print(height)
print(is_student , "\n") # The "\n" is used to add a new line after the output.

# You can also use the input() function to get user input in Python. The input() function takes a prompt string as an argument and returns the user's input as a string.

user_name = input("Enter your name: ")
print("Hello, " + user_name, "\n") # The + operator is used to concatenate or add strings in Python.

# Use "," to separate multiple values in a print statement

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Type conversion is the process of converting a value from one data type to another. In Python, you can use the int(), float(), and str() functions to convert values between different data types.

# Here's an example of type conversion:

number_str = "10" # String variable
number_int = int(number_str) # Convert string to integer

print("String:", number_str)
print("Integer:", number_int, "\n")

# Same way you can convert integer to float and float to string and other data types as well.


# Day 1 - Project: Create a simple program that takes user input for their name, age, and height, and then prints out a summary of the information.

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_height = float(input("Enter your height (in feet): "))    

print("Name:", user_name)
print("Age:", user_age)
print("Height:", user_height)   