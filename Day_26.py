# Day 26 - Python Programming Course

# Today we will cover automated tests with unittest. A test checks whether a
# small part of a program behaves as expected.

import unittest


def add(first_number, second_number):
	return first_number + second_number


def is_even(number):
	return number % 2 == 0


# Test methods must begin with test_. unittest runs these methods and reports
# which expectations passed or failed.

class TestMathFunctions(unittest.TestCase):
	def test_add_returns_sum(self):
		self.assertEqual(add(2, 3), 5)

	def test_add_with_negative_number(self):
		self.assertEqual(add(-2, 3), 1)

	def test_even_number(self):
		self.assertTrue(is_even(8))

	def test_odd_number(self):
		self.assertFalse(is_even(7))


# This guard allows the file to be imported without starting the test runner.

if __name__ == "__main__":
	unittest.main()
