# Day 3 - Python Programming Course

# Today we will cover control flow in Python, which allows you to make decisions in your code based on certain conditions.

# Control flow is achieved using conditional statements, such as if, elif, and else.

# if statement: It allows you to execute a block of code only if a certain condition is true.

# Here's a simple example:

x = 10

if x > 5:
    print("x is greater than 5")

# elif statement: It allows you to check multiple conditions. If the first condition is false, it checks the next one.

elif x == 5:
    print("x is equal to 5")


# else statement: It allows you to execute a block of code if none of the previous conditions are true.

else:
    print("x is less than 5")

# You can also use logical operators (and, or, not) to combine multiple conditions in your if statements.

# Here's an example using logical operators:

y = 15

if y > 10 and y < 20:
    print("y is between 10 and 20")

elif y <= 10 or y >= 20:
    print("y is not between 10 and 20")

elif not (y > 10 and y < 20):
    print("y is not in the range of 10 to 20")


# Day 3 Project: Create a simple number guessing game where the user has to guess a randomly generated number between 1 and 100.

import random  # We will use the random module to generate a random number. 

# Don't worry we will cover Modules in detail in the upcoming days.

random_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")

print("I have generated a random number between 1 and 100. Can you guess it?")

while True:
    user_guess = int(input("Enter your guess: "))

    if user_guess < random_number:
        print("Too low! Try again.")

    elif user_guess > random_number:
        print("Too high! Try again.")

    else:
        print("Congratulations! You guessed the correct number:", random_number)
        break  # Exit the loop if the user guesses correctly.
        print("Thank you for playing the Number Guessing Game!")


