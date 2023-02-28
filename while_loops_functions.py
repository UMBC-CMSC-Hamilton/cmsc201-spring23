"""
    what is a for loop?
        a for loop is a loop where you 'know' the number of iterations
            range(10) or range(len(a_list)), a_string, etc
            
        for-each = gives you elements, remember that you can't modify the
            elements
            
        for-i[ndex] loop = it's a loop where you can operate on the indices
            of a list, or string, if a list you can modify the elements
    
    while loops are if statements on repeat
        while [condition] is true we will repeat the loop
        
        user input validation
        main loops (GUI programs, servers, game loops)
"""

a_string = input('Enter a string: ')
"""
    Goal: find 3 a's if there are any in the string.
"""
current_index = 0
a_count = 0
while current_index < len(a_string) and a_count < 3:
    print(a_count, current_index, a_string[current_index])
    if a_string[current_index] == 'a':
        a_count += 1
    
    # avoids infinite loops
    current_index += 1

print(a_count, current_index)

if a_count == 3:
    print(a_string, 'has at least 3 a\'s')
else:
    print(a_string, 'doesn\'t have 3 a\'s')

"""
    User Validation Example
    
    A user should enter an even number that is between 0 and 100
    
"""
# priming input
the_num = int(input('Enter a number that is even and between 0 and 100: '))
# number is odd (not even) OR not between 0 and 100
# the_num % 2 == 0 then that's actually what you want, you DONT want to loop
while not (0 <= the_num <= 100) or the_num % 2 == 1:
    if the_num % 2 == 1:
        print('This number was odd you must enter an even number')
    else:
        print('This number was not in the correct range. ')
    
    the_num = int(input('Enter a number that is even and between 0 and 100: '))

print(the_num, 'was correct')

"""
    0  1  2  3  4  5  6   7   8 ...
    1  2  3  4  5  6  7   8   9 ...
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
    
    hint: remember at least two previous, make a list as you go
                    we're using this one
    F_1 = 1         F_0 = 1
    F_2 = 1         F_1 = 1
    F_3 = 2         F_2 = 2
    F_4 = 3         F_3 = 3
    ...             ...
"""

"""
    s_n = 3 * s_{n - 1} + 2 * s_{n - 2} + s_{n - 3}

    s_0 = 1, s_1 = 1, s_2 = 2
    s_3 = 3 * s_2 + 2 * s_1 + s_0 = 3(2) + 2(1) + 1 = 9
"""

my_seq = [1, 1, 2]
for i in range(10):
    if i < len(my_seq):
        print(my_seq[i])
    else:
        # -1 or len(my_sequence) - 1
        # next_element = 3 * my_seq[-1] + 2 * my_seq[-2] + my_seq[-3]
        next_element = 3 * my_seq[len(my_seq) - 1] + \
                       2 * my_seq[len(my_seq) - 2] + \
                       my_seq[len(my_seq) - 3]
        
        my_seq.append(next_element)
        print(my_seq[-1])

"""
    what if we try to find the first element that is bigger than
        100,000
    combinatorics = advanced counting math 475
"""

previous_3 = 1
previous_2 = 1
previous_1 = 2
current = 0

seq_ind = 3

while current < 100000:
    current = 3 * previous_1 + 2 * previous_2 + previous_3
    previous_3 = previous_2
    previous_2 = previous_1
    previous_1 = current
    print(seq_ind, current)
    seq_ind += 1

test_string = 'aaaabbbbbbbaaabbaaabbbaabbaaaaabbbabbabab'
"""
    Find the longest consecutive sequence of the same letter and
        tell me it's length
"""
test_string = input("Enter the test string: ")

seq_char = ''
seq_count = 0

max_char = ''
max_count = -1

for the_char in test_string:
    # print(seq_char, seq_count, the_char)
    if seq_char == the_char:
        seq_count += 1
    else:
        if seq_count > max_count:
            max_count = seq_count
            max_char = seq_char
        
        '...bbbbbbbbbbbb..baaaaab...'
        seq_char = the_char  # needs to happen every time the letter changes
        seq_count = 1  # because we already found one

print(max_char, max_count)


str_index = 0
seq_char = ''
seq_count = 0

max_char = ''
max_count = -1

while str_index < len(test_string):
    if test_string[str_index] == seq_char:
        seq_count += 1
    else:
        if seq_count > max_count:
            max_count = seq_count
            max_char = seq_char
        seq_char = test_string[str_index]
        seq_count = 1
    
    str_index += 1

print(max_char, max_count)

str_index = 0
seq_char = ''
seq_count = 0

max_char = ''
max_count = -1

while str_index < len(test_string):
    while str_index < len(test_string) and \
            test_string[str_index] == seq_char:
        seq_count += 1
        str_index += 1
    if seq_count > max_count:
        max_count = seq_count
        max_char = seq_char
    if str_index < len(test_string):
        seq_char = test_string[str_index]
        seq_count = 0


print(max_char, max_count)