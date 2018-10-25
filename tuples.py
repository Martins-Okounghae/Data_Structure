# Creating tuples

tup_1 = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday', 1980,1975, 2015)


tup_2 = (100,200,300,400,500,600)


tup_3 = "a","b","c","d","e"


# Empty tuple

empty_tup=()


# Tuple with a single value

single_val_tup = (50,)


# Accessing values in Tuples

print(tup_1[0:])

print(tup_2[1:5])

# Looping through a tuple
print("\nPrinting the loop")
for x in tup_1:
    print(x,sep=str(","), end=str('\n'))


#  Tuples are immutable - Meaning tuples can't be change after creation
#  Tuple can only be created from existing tuples

tup_4 = tup_1 + tup_2

print(tup_4, sep=',')

print('\n Looping through tup_4')

for x in tup_4:
    print(str(x) + str(","))


# Delete Tuples Elements
print('Printing tup_4')
print(tup_4)


# del tup_4

print("After deleting tup_4")

print(tup_4)

# Repetition

grettings = ('Hi',)*4

print(grettings)


# Membership

list_of_num = (1, 2, 3, 4, 5, 6, 7, 8, 9)

check_num = 0 in list_of_num

print(check_num)
