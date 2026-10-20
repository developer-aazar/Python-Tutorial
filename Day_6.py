# Day 6 - Python Programming Course

# Today we will cover lists in Python. A list stores multiple values in one variable.
# Lists are ordered, and you can change them after creating them.

fruits = ["apple", "banana", "cherry"]

# List indexes start at 0, just like string indexes.

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("All fruits:", fruits)

# You can change an item by assigning a new value at its index.

fruits[1] = "orange"
print("After changing the second fruit:", fruits)

# append() adds an item to the end of a list. insert() adds an item at an index.

fruits.append("mango")
fruits.insert(0, "grape")
print("After adding fruits:", fruits)

# remove() removes a matching value, and pop() removes an item by its index.

fruits.remove("cherry")
removed_fruit = fruits.pop()
print("After removing items:", fruits)
print("Fruit removed by pop():", removed_fruit)

# A for loop can visit every item in a list.

for fruit in fruits:
	print("I like", fruit)

# len() tells you how many items are in a list.

print("Number of fruits:", len(fruits))

# Day 6 Project: Make a shopping list by asking the user to enter three items.

shopping_list = []

for item_number in range(1, 4):
	item = input(f"Enter shopping item {item_number}: ")
	shopping_list.append(item)

print("Your shopping list:")
for item_number, item in enumerate(shopping_list, start=1):
	print(f"{item_number}. {item}")
