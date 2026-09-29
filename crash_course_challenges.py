#1 - Done
import math
bill = 50
tip = 0.2 * bill
total = bill + tip
print() 
# f"the tip is{bill *= 0.2}"

print(f"Tip: ${tip}")
print(f"Total: ${total}")

#2 - Done
import math
 
students = 23
slices_per_student = 2
slices_per_pizza = 8

#slices_needed at least = 46
#total_slices we have right = 48
slices_needed = students * slices_per_student
a_number = slices_needed / slices_per_pizza
pizzas = math.ceil(a_number)
total_slices = pizzas * slices_per_pizza
remainder_slices = total_slices - slices_needed
print(f"Order {pizzas} pizzas")
print(f"Extra slices: {remainder_slices}")

#3 - Done
fahrenheit = 212

a = fahrenheit - 32
b = 5/9
c = a*b
print(f"212 F is {c} C")

#4 - Done
score = 84
 
if score >= 90:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
else:
    print("F")

#5 - Done after solution was shown in class
password = "csaea2026"
attempt = "CSAEA2026"

if attempt == "csaea2026":
    print("Access granted")
else:
    print("Access denied")

#6 - Done
plate = 4827

remainder = plate % 2
if remainder == 0:
    print("Park on the east side")
else:
    print("Park on the west side")

#7 - Don't know/Skip
height = 50
age = 8
has_adult = True
 
if height < 48:
    print("You may not ride")
elif height >= 48 and age >= 10 or has_adult:
    print("You may ride!")
else:
    print("You may not ride")

#8 - Stuck
first = "Ada"
last = "Lovelace"
school = "CSAEA"

end = first + last + school
end += "Hello, my name is "
print(end)

#9
cart = [12, 5, 30, 8]
# <Your Code Here>
print()


#10



#11 - Done
start = 10
for start in range(10,0,-1):
    print(start)

print("Liftoff!")




#12


#13 - Done
savings = 0
weekly_deposit = 15
goal = 100
 
while savings < 100:
    savings += weekly_deposit
    print(savings)
x = goal/weekly_deposit
weeks = math.ceil(x)
print("$105")
print(f"Weeks: {weeks}")

#16 - Done
import math
 
area = 49
side_length = math.sqrt(area)
perimeter = side_length * 4
print(f"Fencing needed: {perimeter}ft ")


#17 - Done
import math
 
minutes_parked = 50
block_length = 15
cost_per_block = 1

block = minutes_parked / block_length
cost = math.ceil(block)
print(f"You owe ${cost}")

#18 - Done
playlist = ["Intro", "Song A", "Song B", "Finale"]
playlist[0] = "Finale"
playlist[-1] = "Intro"
print(playlist)

print()


#20 - Done
speed_limit = 55
speed = 71
if speed <= speed_limit:
    print("Fine: Nothing")
elif speed > speed_limit and speed <= speed_limit +10:
    print("Fine: Warning")
elif speed >= speed_limit +10 and speed <= speed_limit +20:
    print("Fine: $100")
else:
    print("Fine: $250")











