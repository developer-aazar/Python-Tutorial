# Day 7 - Python Programming Course

# Today we will cover tuples in Python. A tuple stores multiple values in one
# variable, like a list, but its items cannot be changed after it is created.

colors = ("red", "green", "blue")

# Tuples are ordered, so you can access their items using indexes.

print("First color:", colors[0])
print("Last color:", colors[-1])
print("All colors:", colors)
print("Number of colors:", len(colors))

# You can loop through a tuple just as you loop through a list.

for color in colors:
	print("Color:", color)

# A tuple cannot be changed. For example, colors[0] = "yellow" would cause
# a TypeError. Use a list instead when you need to add, remove, or change items.

# Tuple unpacking assigns each item to its own variable.

student = ("Aazar", 25, "Python")
student_name, student_age, student_course = student

print("Student:", student_name)
print("Age:", student_age)
print("Course:", student_course)

# A tuple with one item needs a comma after the item so Python recognizes it
# as a tuple rather than a value inside parentheses.

single_item_tuple = ("beginner",)
print("One-item tuple:", single_item_tuple)

# Day 7 Project: Store a location as a tuple and display its coordinates.
# Tuples are useful here because the coordinates belong together as one value.

location = (24.8607, 67.0011)
latitude, longitude = location

print("Location:", location)
print("Latitude:", latitude)
print("Longitude:", longitude)
