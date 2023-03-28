"""
    what is a dictionary?
        Hash - Ruby, HashMaps - Java, Hash Tables - C++
        
        a dictionary is a different kind of list,
            you can access it with an "index" we'll call it a key
            the key doesn't have to be an integer, only has to be immutable
            immutables = int, float, bool, strings
            
            usually you're going to use strings as the keys
            
        To create a dictionary you can use the {} or dict()
"""

my_first_dictionary = {}
# to insert something into a dictionary, access it and assign the first time
my_first_dictionary["hello"] = 5
my_first_dictionary["rabbit"] = 17
my_first_dictionary["salmon"] = 24
my_first_dictionary["zebra"] = -7
print(my_first_dictionary)
# keys are paired with the values in order to access a specific value
#   you use the key for it.

# dictionaries map keys to values
print(my_first_dictionary["salmon"], my_first_dictionary["zebra"])

grades = {'Eric': [92, 85, 91], 'Lisa': [84, 99, 97]}
# keys have to be IMMutable but the values can be anything
print(grades)
grades['Eric'].append(81)
grades['Lisa'].append(77)
print(grades, grades['Eric'][2])

other_dict = {5: 'Hi', 17: 'Flour', 31: 'Flower', 77: 'fluffy'}
print(other_dict)
"""
    if this were a list, you'd start at 0, and you'd go up to index = len - 1
    index 5, 17, 31, 77 exist, none of the other do
"""

"""
    in keyword checks KEYS not VALUES

    not in also works
"""

x = input('Tell me an index: ')
while x != 'quit':
    x = int(x)
    if x in other_dict:
        print('Your key is', x, 'and has value', other_dict[x])
    else:
        print('Your key was not in the dictionary.')
    
    x = input('Tell me an index: ')

"""
    Each key is unique (values don't have to be unique)
    
    elements in lists are not always unique:
    
        [5, 5, 6, 5, 5, 8, 5, 5, 6
"""

my_favorites = {}
my_favorites['happy'] = 'turtle'
my_favorites['happy'] = 'lambda'
print(my_favorites)

"""
With lists:
    del list[index] removes the list at the index
    list.remove(value) removes the first time we find value
    
How to remove a key?
    del dict[key]

"""

# values are NOT unique, because you're not looking up things by value
my_sample = {'a': 5, 'b': -3, 'd': 7, 'e': 7, 'f': 4, 'c': 5}
print(my_sample)
del my_sample['c']
print(my_sample)

delete_keys = []
for key in my_sample:
    # print(key, my_sample[key])
    if my_sample[key] == 7:
        delete_keys.append(key)

for key in delete_keys:
    del my_sample[key]
print(my_sample)

my_sample_list = [2, 6, 6, 5, 4, 3, 6, 3, 3, 5, 3, 2]
"""
this code doesn't really work because it will fail to remove all the 6's
    and also will IndexError

print(my_sample_list)
for x in range(len(my_sample_list)):
    if my_sample_list[x] == 6:
        del my_sample_list[x]
        print(my_sample_list)
        
print(my_sample_list)
"""

while 6 in my_sample_list:
    my_sample_list.remove(6)
    
print(my_sample_list)

my_sample_list = [2, 6, 6, 5, 4, 3, 6, 3, 3, 5, 3, 2]

print(my_sample_list)
six_count = 0
for x in range(len(my_sample_list)):
    if my_sample_list[x] == 6:
        six_count += 1

for i in range(six_count):
    my_sample_list.remove(6)

print(my_sample_list)



"""
This is totally legal in 201, and in python but don't do it.

weird_dict = {'hello': 14, 'robot': 3, True: 7, 3.812: 15, 13: 13}
for key in weird_dict:
    print(key.capitalize(), weird_dict[key])
"""
bool_dict = {True: 'hi there', False: 'we are done'}
# most of your keys should be ints or strings
# avoid using floats
"""
    float = mantissa * (2 ** exponent)
"""

print(5/3, 1/3)

x = 1/3
y = 5/3

if 5 * x == y:
    print('Yep')
else:
    print('huh?')
    
print(3 * x, 5 * x, y - 5 * x)

floaty_dict = {5 * x: 'hi', y: 'robot'}
print(floaty_dict)

"""
    Yes datetimes
    tuples
"""

my_tuple_dict = {(5, 3): 'hi', (2, 4): 'pool'}
print(my_tuple_dict)
# this is why keys have to be immutable
# my_list_dict = {[5, 3]: 'hi',[2, 4]: 'pool'}
# print(my_list_dict)