import collections

# Creating a chain map

dict1 = {'day1':'Mon', 'day2': 'Tue'}

dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary

print(res.maps, end='\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

# Print all the elements from the result
print('elements:')
for key, value in res.items():
    print('{} = {}'.format(key, value))

print()

# Find a specific value in the result

print('day3 in res: {}'.format(('day3' in res)))

print('day4 in res: {}'.format(('days4' in res)))

# Map Reordering
print()
print('Map Reordering')
dict_1 = {'day_1': 'Mon', 'day_2': 'Tue'}

dict_2 = {'day_3':'Wed', 'day_4': 'Thu'}

res1 = collections.ChainMap(dict_1, dict_2)
print(res1.maps, end='\n')

res2 = collections.ChainMap(dict_2,dict_1)

print(res2.maps, '\n')

# Updating Map

print()

print('Updating Map')

dict_11 = {'day1':'Mon', 'day': 'Tue'}

dict_12 = {'day3': 'Wed', 'day4': 'Thu'}

res4 = collections.ChainMap(dict_11, dict_12)

print(res4.maps, end='\n')

dict_12['day4'] = 'Fri'
print(res4.maps, end='\n')





