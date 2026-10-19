# Day 5 - Python Programming Course

# Today we will cover strings in Python. A string is a sequence of characters
# written inside single or double quotation marks.

message = "Python is fun to learn"

# You can find the number of characters in a string with len().

print("Message:", message)
print("Number of characters:", len(message))

# Each character has an index. Python starts counting indexes from 0.

print("First character:", message[0])
print("Last character:", message[-1])

# Slicing lets you get part of a string. The ending index is not included.

print("First six characters:", message[0:6])
print("Every second character:", message[::2])

# Strings have useful methods for changing letter case and replacing text.
# These methods return a new string; they do not change the original string.

print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Replace a word:", message.replace("fun", "great"))

# The in keyword checks whether some text appears inside a string.

print("Does the message contain 'learn'?:", "learn" in message)

# An f-string lets you place variables directly inside a string.

student_name = "Aazar"
lesson_number = 5
print(f"{student_name} is learning Python on day {lesson_number}.")

# Day 5 Project: Create a simple word analyzer that displays information
# about a word entered by the user.

user_word = input("Enter a word: ")

print("Your word is:", user_word)
print("Number of characters:", len(user_word))
print("Uppercase:", user_word.upper())
print("Lowercase:", user_word.lower())
print("First character:", user_word[0])
print("Last character:", user_word[-1])