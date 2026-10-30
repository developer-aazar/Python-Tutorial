# Day 19 - Python Programming Course

# Today we will cover inheritance. Inheritance lets a new class reuse and
# customize behavior from an existing class.

class Animal:
	def __init__(self, name):
		self.name = name

	def speak(self):
		return "The animal makes a sound."


# Dog inherits the name attribute and methods from Animal.

class Dog(Animal):
	def speak(self):
		return "Woof!"


class Cat(Animal):
	def speak(self):
		return "Meow!"


dog = Dog("Buddy")
cat = Cat("Luna")
print(f"{dog.name} says {dog.speak()}")
print(f"{cat.name} says {cat.speak()}")

# super() calls a method from the parent class. This is useful when the child
# class needs extra setup but should keep the parent's setup too.

class GuideDog(Dog):
	def __init__(self, name, owner):
		super().__init__(name)
		self.owner = owner


guide_dog = GuideDog("Max", "Sara")
print(f"{guide_dog.name} helps {guide_dog.owner} and says {guide_dog.speak()}")

# Day 19 Project: Create a general employee and a manager with an extra field.

class Employee:
	def __init__(self, name, job_title):
		self.name = name
		self.job_title = job_title

	def introduce(self):
		return f"{self.name} works as a {self.job_title}."


class Manager(Employee):
	def __init__(self, name, team_size):
		super().__init__(name, "manager")
		self.team_size = team_size

	def introduce(self):
		return f"{super().introduce()} They lead a team of {self.team_size}."


manager = Manager("Ali", 4)
print(manager.introduce())
