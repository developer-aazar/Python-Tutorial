# Day 11 - Python Programming Course

# Today we will cover modules in Python. A module is a file that contains
# reusable Python code. Python includes many useful modules in its standard
# library, so you can use them without installing anything.

# import loads a module. Use the module name before one of its functions.

import math

print("Square root of 25:", math.sqrt(25))
print("Rounded up:", math.ceil(4.2))
print("Rounded down:", math.floor(4.8))

# You can import one function directly from a module.

from random import randint

print("A random number from 1 to 10:", randint(1, 10))

# The as keyword gives a module a shorter alias.

import statistics as stats

test_scores = [78, 85, 92, 85, 90]
print("Average test score:", stats.mean(test_scores))
print("Middle test score:", stats.median(test_scores))

# Day 11 Project: Roll a pair of dice and display their total.

die_1 = randint(1, 6)
die_2 = randint(1, 6)

print("First die:", die_1)
print("Second die:", die_2)
print("Total:", die_1 + die_2)
