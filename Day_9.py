# Day 9 - Python Programming Course

# Today we will cover dictionaries in Python. A dictionary stores information
# as key-value pairs. Each key is used to find its corresponding value.

student = {
	"name": "Aazar",
	"age": 25,
	"course": "Python",
}

# Use a key inside square brackets to get its value.

print("Name:", student["name"])
print("Age:", student["age"])

# You can add a new key-value pair or update a value using assignment.

student["city"] = "Karachi"
student["age"] = 26
print("Updated student:", student)

# get() also looks up a value. It can return a default value when a key is
# missing instead of causing a KeyError.

print("Course:", student.get("course"))
print("Email:", student.get("email", "No email provided"))

# Use keys(), values(), or items() to loop through dictionary information.

for key, value in student.items():
	print(f"{key}: {value}")

# A dictionary can contain another dictionary as a value.

book = {
	"title": "Python Basics",
	"author": "A. Jatoi",
	"details": {
		"pages": 180,
		"language": "English",
	},
}

print("Book title:", book["title"])
print("Number of pages:", book["details"]["pages"])

# Day 9 Project: Create a small contact card using information from the user.

contact = {
	"name": input("Enter the contact's name: "),
	"phone": input("Enter the contact's phone number: "),
	"email": input("Enter the contact's email: "),
}

print("Contact card:")
for key, value in contact.items():
	print(f"{key.title()}: {value}")
