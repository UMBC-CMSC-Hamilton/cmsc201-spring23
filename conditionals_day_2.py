"""
if - original if statement, takes an expression that it can evaluate to True False
elif - also takes an expression it evaluates if it's the first elif that's true
    as many elifs as you can write
    only one will ever execute (maybe zero)
else
    if none of the statements if/elifs execute then the else will
    else is not required
"""
if False:
    my_num = int(input('Tell me your favorite number: '))
    if my_num == 3:
        print('Three is a good number')
    elif my_num == 7:
        print('Seven is a lucky number')
    elif my_num == 13:
        print('Oh are you sure that seems unlucky?')
    else:
        print(f'I am sure that {my_num} is great but I dont know anything about it')


    if my_num == 0:
        print('Your number is zero')

    if my_num % 2 == 0:
        print('Your number is even')

    """
    if my_num == 0:
        print('Your number is zero')
    elif my_num % 2 == 0:
        print('Your number is even')
    """


    """
    What is nesting in computer science?
        Idea that you can put if statements inside of if statements
            for loops inside of other blocks, while loops inside of block
    """

    the_secret_password = 'most secure ever1'
    password_entry = input('Password please: ')

    if the_secret_password == password_entry:
        yes_no = input('You have logged in, you wish to delete the GL server? ')
        if yes_no.lower() == 'y' or yes_no.lower() == 'yes':
            # there is also a .upper() function that you can use
            # linux is also case sensitive be careful
            print('All things have been deleted, yay')
        else:
            print('Did not delete')
    else:
        print('You have not logged in, try again later')

    """
        Every letter in a computer is encoded as a number
        ASCII codes, unicode (extended character set)
    """

    """
    The simpsons "20 questions
    """
    skateboard = input('Do you ride a skateboard? ')
    if skateboard.lower() == 'yes':
        print('You are Bart')
    else:
        nuclear = input('Do you work at a nuclear power plant? ')
        if nuclear.lower() == 'yes':
            pink_frosted_sprinkled = input('Do you like pink frosted sprinkled donuts? ')
            if pink_frosted_sprinkled.lower() == 'yes':
                print('You are homer')
            else:
                print('You are lenny')
        else:
            tower_blue = input('Do you have a tower of blue hair? ')
            if tower_blue.lower() == 'yes':
                print('You are Marge')
            else:
                saxophone = input('Do you play the saxophone? ')
                if saxophone.lower() == 'yes':
                    print('You are Lisa')
                else:
                    print('I dont know are you Willie the Groundskeeper?')


"""
    Talk about mod
    
    modulus or mod is calculating a remainder of an integer division
    
    integer division and floating point division
    a/b = floating point division -> outputs a float regardless of what the input is
    
    a // b = integer division
    5 // 3 = 1 remainder of 2
            the one is the output of the division
"""

print(5 / 3, 5 // 3, 1 // 2)
# 1 // 2 = 0 R 1
print(5 // 7)
print(12 // 5)

print(12 % 5)
print(13 % 5)

print(17 % 4, 18 % 7, 31 % 9, 35 % 7)

day_of_month = int(input('What day of Feb is it? '))
if 1 <= day_of_month <= 28:
    if day_of_month % 7 == 1:
        print('The day is Wednesday')
    elif day_of_month % 7 == 2:
        print('The day is Thursday')
    elif day_of_month % 7 == 3:
        print('The day is Friday')
    elif day_of_month % 7 == 4:
        print('The day is Saturday')
    elif day_of_month % 7 == 5:
        print('The day is Sunday')
    elif day_of_month % 7 == 6:
        print('The day is Monday')
    elif day_of_month % 7 == 0:
        print('The day is Tuesday')
else:
    print(f'{day_of_month} is not valid')

"""
    be careful with mods of negatives
        in python you dont have to worry
        in other languages, C/C++ worry a little

    N = q * d + r
    0 <= r < d
    
    -5 // 2 => (-3) * 2 + 1 => Mathematically and Pythonically Correct
    -5 // 2 => (-2) * 2 - 1 => C/C++ does this
"""

print(-5 // 2, -5 % 2)
print(-23 // 8, -23 % 8)
print(-243 // 10, -243 % 10)