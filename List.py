# Creating a list


list1 = ['Monday', 'Tuesday', 'Wednesday', 1980, 1970, 2015]

list2 = [1,2,3,4,5,6,7,8,9,10]

list3 = ['Tameara','Justin','Joshua','Madison']

# Accessing Values in a list

print("The value at index 0 in list 1 = ", list1[0])

print("Print a range of values in list 2 = ", list2[1:7])

#Updating a list

list2[0]=100

print("The new value at index 0 = ", list2[0])


# Deleting List Elements

del list2[0]

print("After deleting value at index 0: = ", list2[0])


# Loop through a list

for x in list2:
    print(x)

print("List 1 loop starts here!!!!")
for x in range(len(list1)):
    print(list1[:x+1])