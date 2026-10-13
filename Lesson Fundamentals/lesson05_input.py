import math
import random
# USER INPUT IN PYTHON
#print ("<PROMPT>")
print()

# name = input("Enter your name:")
# print(f"Hello {name}")

# print(type(name))

# age  = input("Enter your age:")
# print(f"Your age is {age}")

# print(type(age))

# age_converted = int(age)
# print(type(age_converted))

# height = float(input("Enter your height: "))
# print(f"You are {height} meters tall")
# print (height+1)

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

color  = input("What is your favorite color?:\n")
print(f"Your favorite color is {color}.")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

number1 = input("Give me a number.\n")
number2 = input("Give me another number.\n")
num1 = int(number1)
num2 = int(number2)
print(f"{number1} + {number2} = {num1+num2}")

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
# pi radius squared 

dia = input("Give me the diameter of a circle.\n")
pi = 3.14
diameter = int(dia)
r = diameter/2
area = pi*r**2
print(f"The area of your circle is {area} units")


# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

sides = input("How many sides do you want the die to have?\n")
number = int(sides)
die_roll = random.randint(1, number)
print(f"You rolled a {die_roll}.")












