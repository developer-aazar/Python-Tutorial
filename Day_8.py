# Day 8 - Python Programming Course

# Today we will cover sets in Python. A set stores unique values, so duplicate
# values are removed automatically. Sets are unordered and do not use indexes.

numbers = {1, 2, 2, 3, 4, 4}
print("Set with duplicate values removed:", numbers)

# Use add() to add an item and remove() to remove an item from a set.

numbers.add(5)
numbers.remove(1)
print("After adding 5 and removing 1:", numbers)

# Use in to check whether an item is in a set.

print("Is 3 in the set?", 3 in numbers)

# Sets are useful for comparing groups of values.

class_a = {"Ali", "Sara", "Mina"}
class_b = {"Sara", "Omar", "Mina"}

# The union contains every unique item from both sets.

print("Students in either class:", class_a | class_b)

# The intersection contains only items that appear in both sets.

print("Students in both classes:", class_a & class_b)

# The difference contains items from the first set that are not in the second.

print("Students only in class A:", class_a - class_b)

# An empty set must be created with set(). Empty braces {} create a dictionary.

empty_set = set()
print("An empty set:", empty_set)

# Day 8 Project: Find the unique words in a sentence entered by the user.

sentence = input("Enter a sentence: ")
words = sentence.lower().split()
unique_words = set(words)

print("Words in the sentence:", words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
