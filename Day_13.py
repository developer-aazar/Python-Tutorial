# Day 13 - Python Programming Course

# Today we will cover list comprehensions. A list comprehension is a concise
# way to create a new list from an existing sequence.

numbers = [1, 2, 3, 4, 5]
squared_numbers = [number ** 2 for number in numbers]

print("Numbers:", numbers)
print("Their squares:", squared_numbers)

# Add an if condition to include only selected values.

even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)

# An if-else expression can choose the value for each item.

labels = ["even" if number % 2 == 0 else "odd" for number in numbers]
print("Number labels:", labels)

# A comprehension can also transform strings.

names = ["aazar", "sara", "mina"]
capitalized_names = [name.title() for name in names]
print("Capitalized names:", capitalized_names)

# Keep comprehensions readable. Use a regular for loop when the expression
# becomes long or contains several conditions.

# Day 13 Project: Make a list of the squares of odd numbers from 1 to 20.

odd_squares = [number ** 2 for number in range(1, 21) if number % 2 != 0]
print("Squares of odd numbers:", odd_squares)
