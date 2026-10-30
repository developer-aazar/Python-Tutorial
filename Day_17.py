# Day 17 - Python Programming Course

# Today we will introduce object-oriented programming. A class describes a kind
# of thing, and an object is one specific thing created from that class.

class Dog:
	pass


# Create two objects from the Dog class. Each object can have its own attributes.

first_dog = Dog()
first_dog.name = "Buddy"
first_dog.age = 3

second_dog = Dog()
second_dog.name = "Luna"
second_dog.age = 5

print(first_dog.name, "is", first_dog.age, "years old.")
print(second_dog.name, "is", second_dog.age, "years old.")

# __init__ runs when a new object is created. self refers to the object being
# created, so it lets us store information on that particular object.

class Student:
	def __init__(self, name, course):
		self.name = name
		self.course = course


student = Student("Sara", "Python")
print(f"{student.name} is learning {student.course}.")

# Day 17 Project: Create a book class and make two book objects.

class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author


first_book = Book("Python Basics", "A. Jatoi")
second_book = Book("Learning Python", "S. Example")

print(f"{first_book.title} by {first_book.author}")
print(f"{second_book.title} by {second_book.author}")
