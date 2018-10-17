from array import *


array1 = array('i',[10,20,30,40,50])

for x in array1:
    print(x)



# Accessing array element

array2 = array('I',[1,2,3,4,5,6,7,8,9])


print(array2[0])

print(array2[2])


#Insertion Operation

array3 = array('i', [100,200,300,400,-500])

array3.insert(1, -100)

print("Printing content of array3")
for x in array3:
    print(x)


# Deletion Operation

array4 = array('i',[2,4,6,8,10])

array4.remove(array4[3])

array4.remove(4)


print("Printing the content of array 4")
for x in array4:
    print(x)


# Search Operation

array5 = array('i',[1,3,5,7,11])

search = array5.index(7)
print("Printing the content of array 5")
print(search)


# Update Operation

array6 = array('i', [11,12,13,14,15,16,17,18,19,])

array6[2]= 130
print("Printing the content of array 6")
for x in array6:
    print(x)