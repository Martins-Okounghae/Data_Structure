# Two dimension array
from array import *

print("----------------------------------------------------------------")

print("Declaring values in a 2D array")

print("----------------------------------------------------------------")
Temp = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 5], [12, 15, 8, 6]]

print("The values in 2D Array Temp = ", Temp)
print("----------------------------------------------------------------")
# Accessing values in 2D Array

print("Accessing values in 2D Array")
print("----------------------------------------------------------------")
print("The values in Temp[0] = ", Temp[0])
print("The values in Temp[1][2] = ", Temp[1][2])
print("----------------------------------------------------------------")
# Looping through a 2D Array
print(" Looping through a 2D Array")
print("----------------------------------------------------------------")

for r in Temp:
    for c in r:
        print(c, end=" ")
    print()
print("----------------------------------------------------------------")
# Inserting values in 2D Array

Temp.insert(2, [0,5,11,13,6])

# Looping through a 2D Array after insertion


print("Looping through a 2D Array after insertion")
print("----------------------------------------------------------------")

for r in Temp:
    for c in r:
        print(c, end=" ")
    print()

print("----------------------------------------------------------------")

print("Updating values in a 2D Array")

print("----------------------------------------------------------------")

Temp[2] = [11,9]

Temp[0][3] = 7

Temp[3] = [100,200,300,400]

Temp[3][3] = 900
for r in Temp:
    for c in r:
        print(c, end=" ")
    print()


print("----------------------------------------------------------------")

print("Deleting the values in 2D array")

print("----------------------------------------------------------------")

Temp_2 = [[110, 120, 50, 20], [150, 600, 100], [100, 800, 50], [1200, 15000, 80, 600]]

del Temp_2[2]

print("----------------------------------------------------------------")

print("Printing the 2D array values after deletion")

print("----------------------------------------------------------------")

for r in Temp_2:
    for c in r:
        print(c, end=" ")
    print()