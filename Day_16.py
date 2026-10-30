# Day 16 - Python Programming Course

# Today we will cover JSON, a text format commonly used to store and exchange
# structured data. Python's json module converts between JSON and Python values.

import json

student = {
	"name": "Aazar",
	"course": "Python",
	"completed_lessons": 15,
	"is_active": True,
}

# json.dumps() converts a Python value into a JSON string.

student_json = json.dumps(student, indent=4)
print("JSON text:")
print(student_json)

# json.loads() converts JSON text back into Python values.

loaded_student = json.loads(student_json)
print("Student name:", loaded_student["name"])

# Use json.dump() and json.load() to save JSON data in a file and read it back.

with open("day16_progress.json", "w", encoding="utf-8") as file:
	json.dump(student, file, indent=4)

with open("day16_progress.json", "r", encoding="utf-8") as file:
	progress = json.load(file)

print("Saved progress:", progress)

# JSON supports strings, numbers, booleans, lists, dictionaries, and None.
# Python converts True, False, and None to their JSON equivalents.

# Day 16 Project: Save a small book collection as JSON and read it back.

books = [
	{"title": "Python Basics", "read": True},
	{"title": "Learning Data", "read": False},
]

with open("day16_books.json", "w", encoding="utf-8") as file:
	json.dump(books, file, indent=4)

with open("day16_books.json", "r", encoding="utf-8") as file:
	loaded_books = json.load(file)

for book in loaded_books:
	status = "finished" if book["read"] else "not finished"
	print(f"{book['title']}: {status}")
