# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html

import math

sq_root = math.sqrt(25)
print("Square root ", sq_root)

round_up = math.ceil(4.5)
print("Round up: ", round_up)

round_down  =math.floor(4.8)
print(f"Round down: {round_down}" )

exponent  = math.pow(2, 5)
print(f"Exponent: {exponent}")

#CONSTANT

cat = "Cat"
# CONSTANTS are variables that NEVER change. They are written in ALL CAPS


PI = math.pi
print(PI)

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2

diameter = 14
radius = diameter / 2
circle_area = PI*math.pow(radius, 2)
print(f"Area: {circle_area}")

# PYTHON RANDOM LIBRARY

# Python's library is a Pseudorandom Number Generator 

# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.0. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float UP to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10. 
print()

import random

seed = 9000.9
step1 = seed /6.7
(step1)
step2 = step1 -800
(step2)
step3 = step2%10
(step3)
result = math.ceil(step3)
print(result)

seed = 76743



for i in range(5):
    calcs = seed + 2234 * 22 / 3
    randint  = math.ceil(calcs) 
    print(f"Simple random num gen: {randint % 10}")
    seed += 1

#Pythons random library

import random

random_integer  = random.randint(1,100)
print (random_integer)

random_float = random.random()
print(random_float)

my_list = ["taco", "burrito", "enchilada", "quesadilla"]
random_selection = random.choice(my_list)
print(random_selection)

random.shuffle(my_list)
print(my_list)

# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it.

print()
print("Challenge 2:")
die_roll = random.randint(1,6)
print(die_roll)

# Challenge 3: Random Square Root
# Use random.randint() to pick a number between 1 and 100. Store it in "num".
# Use math.sqrt() to find its square root.
# Print the number, its square root, and the square root rounded UP with math.ceil().

num = random.randint(1,100)
sqrt_num = math.sqrt(num)
round_up_num = math.ceil(sqrt_num)
print(f"Number: {num}\nSqrt of Number: {sqrt_num}\nRounded up Number {round_up_num}")

# Challenge 4: Power Roll
# Roll two dice with the random library: one is the "base," one is the "exponent."
# Use math library to raise the base to the exponent. (ie, based to the POWer of exponent)
# Print both rolls and the result as an integer (hint: int() removes the .0).
print()
base = random.randint(1,6)
exponent = random.randint(1,6)
number  = math.pow(base, exponent)
print(int(number))































































