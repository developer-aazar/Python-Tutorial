# Day 4 - Python Programming Course

# Today we will cover loops in Python, which allow you to execute a block of code multiple times.

# There are two main types of loops in Python: for loops and while loops.

# For loop: It is used to run a block of code a specific number of times, usually when you know beforehand how many times you want to iterate.

# Here's a simple example:

for i in range(6):  # This will iterate 6 times, with i taking values from 0 to 5.
    print("Iteration:", i)

# Another usecase of for loop is to iterate over a sequence (like a list, tuple, or string).

# Here's an example of iterating over a list:

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)

# While loop: It is used to run a block of code as long as a certain condition is true.

# Here's a simple example:

count = 0

while count < 5:  # This will continue to run as long as count is less than 5.
    print("Count is:", count)
    count += 1  # Increment count by 1 to avoid an infinite loop.

# You can also use break and continue statements in loops.

# The break statement is used to exit a loop prematurely when a certain condition is met.

for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break  # Exit the loop when i is 5.
    print("i is:", i)

# The continue statement is used to skip the current iteration of the loop and move on to the next one.

for i in range(10):
    if i % 2 == 0:  # Check if i is even.
        continue  # Skip the rest of the loop for even numbers.
    print("i is odd:", i)  # This will only print for odd values of i.


# Day 4 Project: Create a simple program that generates multiplication tables for a given number using loops.

n = int(input("Enter a number to generate its multiplication table: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Using While loop to generate multiplication table

number_1 = int(input("Enter a number to generate its multiplication table using while loop: "))
count = 1

while count <= 10:
    print(f"{number_1} x {count} = {number_1 * count}")
    count += 1



