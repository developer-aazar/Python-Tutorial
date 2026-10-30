# Day 20 - Python Programming Course

# Today we will cover iterators and generators. An iterator gives values one
# at a time. A for loop uses an iterator behind the scenes.

colors = ["red", "green", "blue"]
color_iterator = iter(colors)

print(next(color_iterator))
print(next(color_iterator))
print(next(color_iterator))

# Calling next() after the last value raises StopIteration. A for loop handles
# this automatically, which is why it is the usual way to process an iterator.

# A generator function uses yield to produce values one at a time.

def count_up_to(limit):
	current_number = 1
	while current_number <= limit:
		yield current_number
		current_number += 1


for number in count_up_to(5):
	print("Generated:", number)

# Generators can be useful when producing a long sequence because they do not
# need to build a list containing every value first.

# Day 20 Project: Generate the first few multiples of a number.

def multiples(number, count):
	for multiplier in range(1, count + 1):
		yield number * multiplier


chosen_number = int(input("Which number's multiples should I show? "))
for multiple in multiples(chosen_number, 10):
	print(multiple)
