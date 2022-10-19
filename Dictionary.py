# Learning Dictionary
var1 = {'1901080': ['Eunice', 'Fayokemi', 'Dee'], '1901290': 'Daniel'}
# print(var1['1901080'])
# print(var1.get('1901290'))
# print(var1.get('1900243'))
# print(var1.get('1900243', 'Justin'))

# Getting all keys in the dictionary
# print(var1.keys())

# Getting all values in the dictionary
# print(var1.values())

# Getting all items in the dictionary
# print(var1.items())

# Updating a dictionary
# var1['1900147'] = 'Soma'
# print(var1)

# for i in var1.keys():
#     print(f'{i} is a key')

# for i in var1.values():
#     print(f'{i} is a value')

for i, j in var1.items():
    print(i, j)