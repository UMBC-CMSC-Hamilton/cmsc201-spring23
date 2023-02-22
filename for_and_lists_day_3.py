"""
    for [variable] in [iterable]:
        do something with that variable
"""
if False:
    my_list = [1, 2, 8, 5, 9, 10, 3]
    
    # for-i construction - NOT BECAUSE the variable is i
    # it's because it's an index
    for i in range(len(my_list)):
        yes_no = input(f'Do you want to change the element {my_list[i]}? ')
        # i is the index into the list
        if yes_no == 'yes':
            my_list[i] = int(input('Tell me a new value: '))
    
    print(my_list)
    
    # element is actually a copy of the thing inside the list
    # not the list element itself
    # for each construction - when the variable in the loop
    # is an element of the list / iterable not an index
    for element in my_list:
        yes_no = input(f'Do you want to change the element {element}? ')
        if yes_no == 'yes':
            element = int(input('Tell me a new value: '))
    
    print(my_list)

"""
Mutability:
    ints, strings, floats, and bools are considered "immutable"
    
    You can't actually change a string
    
"""

# because you're not allowed to modify a string
my_string = "abjdef"
# my_string[2] = 'c', type error

"""
    When you're creating lists you can use either
    new_list = []
    new_list = list() both create an empty list
"""
new_list = list()
print(new_list)
other_lists = ['abc', 3, 3.2, False, True, 'def', 5]
# it's not the greatest thing to do, avoid it unless you know
# what you're doing
print(other_lists)

#            ---0-----  -----1---  ----2----
a_2d_list = [[1, 2, 3], [5, 6, 7], [9, 8, 3]]
print(a_2d_list[0])
print(a_2d_list[1])
print(a_2d_list[0][1], a_2d_list[1][2])

# this will be on your test
for i in range(4):
    print(a_2d_list[(2 * i) % 3][(7 * i + 1) % 3])
    # a_2d_list[0][1] = 2 for i = 0
    # a_2d_list[1][2] = 7 for i = 1
    # a_2d_list[1][0] = 5 for i = 2
    # a_2d_list[0][1] = 2 for i = 3

"""
    Nesting Loops again, put a loop inside of a loop
"""

height = int(input('Tell me height: '))
width = int(input('Tell me width: '))

for y in range(height):
    for x in range(width):
        if y == 0 or y == height - 1:
            print('*', end="")
        elif x == 0 or x == width - 1:
            print('*', end="")
        else:
            print(' ', end="")
    print()

"""
for y in range(height):
    for x in range(width):
        if x <= y <= width - x or y % 2 == 0:
            print('*', end="")
        else:
            print(' ', end="")
    print()
"""

for y in range(height):
    for x in range(width):
        # width - 1 - x (reverse a list)
        # reverses the x coordinate
        if width - x - 1 <= y:
            print('*', end="")
        else:
            print(' ', end="")
    print()


b_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# i = 0, 1, 2, 3, 4, 5, 6, 7
# this is the trick to count backwards / reverse a list
for i in range(len(b_list)):
    print(i, len(b_list) - 1 - i, b_list[len(b_list) - 1 - i])

for i in range(len(b_list) - 1, -1, -1):
    print(b_list[i], end=" ")

print(b_list)

"""
    say i want to reverse a list
        1) idea 1 - make a new list in reversed order
"""

reversed_list = []
for i in range(len(b_list)):
    reversed_list.append(b_list[len(b_list) - 1 - i])
    
print(reversed_list)

# this works but let's say we don't want to create a new list

# generic swap mechanic
"""
memorize this:

temp = a
a    = b
b    = temp

temp_val = b_list[0]
b_list[0] = b_list[len(b_list) - 1]
b_list[len(b_list) - 1] = temp_val

"""
print("starting... in place list reverse")
for i in range(len(b_list) // 2):
    temp_val = b_list[i]
    b_list[i] = b_list[len(b_list) - 1 - i]
    b_list[len(b_list) - 1 - i] = temp_val
    print(b_list)

print(b_list)

print('going again')
for i in range(len(b_list)):
    if i < len(b_list) // 2:
        temp_val = b_list[i]
        b_list[i] = b_list[len(b_list) - 1 - i]
        b_list[len(b_list) - 1 - i] = temp_val
    print(b_list)
    
"""
    What if we want to go through a string and replace all of the
    'a's with 'z's for no reason
"""
a_string = input('Tell me a string: ')
the_letters_list = list(a_string)
for i in range(len(the_letters_list)):
    if the_letters_list[i].lower() == 'a':
        the_letters_list[i] = 'z'

print(the_letters_list)

new_string = ''
for x in the_letters_list:
    new_string += x
print(new_string)

"""

the join function

    a built in function for strings
    separator.join(a_list_of_characters_or_strings)
"""
print(''.join(the_letters_list))
