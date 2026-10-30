# Day 27 - Python Programming Course

# Today we will cover type hints and docstrings. Type hints describe the kinds
# of values a function expects and returns. Python does not enforce them at
# runtime, but editors and type-checking tools can use them.


def calculate_area(width: float, height: float) -> float:
	"""Return the area of a rectangle."""
	return width * height


print("Area:", calculate_area(4.5, 3))

# Use -> None when a function does not return a value.

def show_message(message: str) -> None:
	"""Print a message for the learner."""
	print(message)


show_message("Type hints help explain how a function should be used.")

# A function can use a union type when it accepts more than one type.

def format_score(score: int | float) -> str:
	"""Return a score with a label."""
	return f"Score: {score}"


print(format_score(95))
print(format_score(87.5))

# Day 27 Project: Convert a distance in kilometers to miles.

def kilometers_to_miles(kilometers: float) -> float:
	"""Convert kilometers to miles using the standard conversion factor."""
	return kilometers * 0.621371


distance = float(input("Enter a distance in kilometers: "))
print(f"{distance} km is {kilometers_to_miles(distance):.2f} miles.")
