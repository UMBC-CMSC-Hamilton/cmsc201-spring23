if False:
    """
    Expressions - boolean expression, expression
    
        operator precedence = order of operations
    
            PEDMAS
            BODMAS all of this applies in programming as well
    """

    my_number = 3 + 2 * 5
    another_number = (2 + my_number) * 4
    print(my_number)
    print(another_number)
    print(5 - 3 - 2)
    print(5 ** 2)  # do not use the caret
    print(49 ** (1/2))
    print(49 ** 1/2) # always add another set of parentheses if you think there may be an issue

    """
        1) arithmetic operators (num op num) -> num
        2) comparison operators (expr == expr) -> True/False
            ==, <=, >=, <, >, !=, in
        3) logical operators
            not
            and
            or
    """

    # assignment operator = instead of comparing this just assigns the variable, doesn't return
    # True or False
    my_new_var = "hello there"

    print(my_number == 13, my_number * 2 < 50, my_number - 3 == 5)

    print("hello" in my_new_var, 'ht' in my_new_var, 'eh' in my_new_var)
    print('asdf' not in my_new_var)

    print(my_number * (2 < 50))
    print(True * True)
    print(True - 1)

    """
        Logical Operators
        
        not - unary operator
        and - binary operators
        or
        
        A       not A
        True    False
        False   True
        
        
        and operator
        
        A and B = requires both to be true
        
        A       B       A and B
        True    True    True
        True    False   False
        False   True    False
        False   False   False
    """
    a = True
    b = False
    print(a, not a, b, not b)

    print(a and not b, not a and not b)
    # not has a higher precedence than and / or operations
    # notice here that not a and not b
    # not a first, then not b then the and evaluates

    """
        or
        
        A or B = inclusive or
        
        A       B       A or B
        True    True    True
        True    False   True
        False   True    True
        False   False   False
    """

    print(False or (True and not False), True and (not True and False))
    print((not True or not False) and (True or False))

    """
        if statements...
        
        syntax:
                            the colon is part of the syntax
        if expression_here : 
            code must be tabbed in one level
            this code also must be tabbed in
            so must this code
        
        this is outside of the if statement, code will always run, if statement is over 
    """

    password = input('Enter the secret password: ')
    if password == 'asdf1234':
        print('You have logged in to the secret server.')
        print('This also is inside the if statement')
    else:
        print('You did not log in successfully')

    print('This is outside of the if statement')

    a_number = int(input('Enter a number: '))
    if a_number % 2 == 1:
        print('a number is odd')

    if a_number % 2 == 0:
        print('a number is even')

    a_word = input('Tell me a word: ')
    if 'a' in a_word:
        print('There is an a in that word')
    else:
        print('there is no a in the word')

    new_number = int(input('Enter some new number: '))

    if 'e' in a_word and new_number > 100:
        print('Both were true')
    else:
        print('one of them wasn\'t true')

"""
elif = else if

kind of like else in that it will execute if the original if statement was false
needs a condition
"""

"""
    How many elifs can you have?
        as many as you can type = any number
    How many elifs will ever execute?
        at most 1, (1 or 0)
"""
my_favorite_num = int(input('Num: '))
if 1 <= my_favorite_num <= 10:
    print('Your number is between 1 and 10')
elif my_favorite_num == 0:
    print('Your favorite number may not even exist, what is zero really?')
elif my_favorite_num <= 0:
    print('They used to call me imaginary but now i am just negative')
else:
    print('I am too big')

"""
    You dont need an else statement but you're always allowed to use one if you want
"""