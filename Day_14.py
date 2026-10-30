# Day 14 - Python Programming Course

# Today we will cover useful tools for working with sequences: enumerate(),
# zip(), and sorted(). These built-in functions make common loops clearer.

# enumerate() gives each item a number as you loop through it.

fruits = ["apple", "banana", "cherry"]

for item_number, fruit in enumerate(fruits, start=1):
	print(f"{item_number}. {fruit}")

# zip() walks through two sequences together. It stops when the shorter
# sequence runs out of items.

students = ["Ali", "Sara", "Omar"]
scores = [88, 94, 79]

for student, score in zip(students, scores):
	print(f"{student} scored {score}.")

# sorted() returns a new sorted list and leaves the original list unchanged.

numbers = [7, 2, 9, 1, 5]
print("Sorted numbers:", sorted(numbers))
print("Sorted from largest to smallest:", sorted(numbers, reverse=True))
print("Original numbers:", numbers)

# Day 14 Project: Match each student's name with their score and show the
# results from highest score to lowest score. The key function tells sorted()
# to compare each pair using its score.

def score_key(result):
	return result[1]

results = list(zip(students, scores))
results_by_score = sorted(results, key=score_key, reverse=True)

for student, score in results_by_score:
	print(f"{student}: {score}")
