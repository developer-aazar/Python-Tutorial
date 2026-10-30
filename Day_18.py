# Day 18 - Python Programming Course

# Today we will add methods to classes. A method is a function defined inside
# a class. An instance method uses self to work with one object's data.

class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height

	def describe(self):
		return f"A {self.width} by {self.height} rectangle"


rectangle = Rectangle(5, 3)
print(rectangle.describe())
print("Area:", rectangle.area())

# Each object stores its own values, but uses the same methods from its class.

another_rectangle = Rectangle(4, 4)
print(another_rectangle.describe())
print("Area:", another_rectangle.area())

# A class can provide a clear text representation with the __str__ method.

class Student:
	def __init__(self, name, course):
		self.name = name
		self.course = course

	def __str__(self):
		return f"{self.name} is studying {self.course}."


print(Student("Mina", "Python"))

# Day 18 Project: Make a simple bank account that can deposit and withdraw.

class BankAccount:
	def __init__(self, owner, balance=0):
		self.owner = owner
		self.balance = balance

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			return True
		return False

	def withdraw(self, amount):
		if 0 < amount <= self.balance:
			self.balance -= amount
			return True
		return False


account = BankAccount("Omar", 50)
account.deposit(25)
account.withdraw(10)
print(f"{account.owner}'s balance: ${account.balance:.2f}")
