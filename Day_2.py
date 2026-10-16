# Day 2 - Python Programming Course

# Today we will cover operators in Python, which are used to perform operations on variables and values.

# There are several types of operators in Python, including:

# 1. Arithmetic Operators: Used to perform mathematical operations.
#    - Addition (+): Adds two values together.
#    - Subtraction (-): Subtracts one value from another.
#    - Multiplication (*): Multiplies two values together.
#    - Division (/): Divides one value by another and returns a float.
#    - Floor Division (//): Divides one value by another and returns the largest integer less than or equal to the result.
#    - Modulus (%): Returns the remainder of a division operation.


# Example of using arithmetic operators in Python:

x = 10
y = 3

print(x + y)  # Output: 13
print(x - y)  # Output: 7
print(x * y)  # Output: 30
print(x / y)  # Output: 3.3333333333333335
print(x // y) # Output: 3
print(x % y)  # Output: 1


# 2. Comparison Operators: Used to compare two values and return a Boolean result (True or False).
#    - Equal to (==): Returns True if the values are equal.
#    - Not equal to (!=): Returns True if the values are not equal. 
#    - Greater than (>): Returns True if the left value is greater than the right value.
#    - Less than (<): Returns True if the left value is less than the right value.
#    - Greater than or equal to (>=): Returns True if the left value is greater than or equal to the right value.
#    - Less than or equal to (<=): Returns True if the left value is less than or equal to the right value.

# Example of using comparison operators in Python:

x = 10
y = 3

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: True
print(x < y)   # Output: False
print(x >= y)  # Output: True
print(x <= y)  # Output: False


# 3. Logical Operators: Used to combine conditional statements and return a Boolean result.
#    - and: Returns True if both statements are true.
#    - or: Returns True if at least one of the statements is true.
#    - not: Returns True if the statement is false.

# Example of using logical operators in Python:

x = True
y = False

print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False


# Day 2 Project: Create a simple calculator that takes two numbers and an operator as input and performs the corresponding operation.

# Simple Calculator

number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

operator = input("Enter an operator (+, -, *, /, //, %): ")

if operator == "+":
    result = number_1 + number_2

elif operator == "-":
    result = number_1 - number_2

elif operator == "*":
    result = number_1 * number_2    

elif operator == "/":
    if number_2 != 0:
        result = number_1 / number_2
    else:
        result = "Error: Division by zero is not allowed."

else:
    result = "Invalid operator."