#Accessing values in dictionary
print("----------------------------------")
print("Declaring a dictionary")
print("------------------------------------")


dict = {'Name':'Zara', 'Age': 7, 'Class': 'First'}

print("----------------------------------")
print("Accessing the dictionary with its key")
print("------------------------------------")

# Accessing the dictionary with its key

print("dict['Name']: ", dict['Name'])

print("dict['Age']: ", dict['Age'])


print("----------------------------------")
print("Updating Dictionary")
print("------------------------------------")
# Updating Dictionary

dict = {"Name" : "Zara", "Age":"7", "Class": "First"}


dict['Age'] = 8 # updating a dictionary

dict['School'] = "DPS School"  # Add new entry

print("dict['Age']: ", dict['Age'])

print("dict['School']: ", dict['School'])


# Delete Dictionary Elements

dict2 = {"Name":"Zar", "Age":7, "Class": "First"}

del dict2['Name'] # remove entry with key 'Name'



print("dict2", dict2)

dict2.clear() # remove all entries in dict
del dict2 # delete entire dictionary











