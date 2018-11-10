# Defining a dictionary
# Accessing Values in Dictionary

dict_1 = {'Name':'Zara', 'Age':'7', 'Class':'First'}

print(dict_1)

print("dictionary 1 ['Age'] = ", dict_1['Age'])

print("dictionary 1 ['Name'] is ", dict_1['Name'])

print("ditionary 1 ['Class'] is ", dict_1['Class'])

# Updating Dictionary

dict_1['Age'] = 23

dict_1['Status'] = 'Married'

dict_1['School'] = 'DBS'


print(dict_1)

# Delete Dictionary Elements

del dict_1['Name']

dict_1.clear()

#del dict_1

<<<<<<< HEAD
dict_2 = {('First Name', 'Last Name'): 'Gold  ' 'Land', 'Age':101}
=======
dict_2 = {('First Name', 'Last Name'): 'Gold  ' 'Land ', 'Age':100}
>>>>>>> 2a07e55966381045636a2707f27d4a1b0a8251ae

print(dict_1)

print(dict_2)
