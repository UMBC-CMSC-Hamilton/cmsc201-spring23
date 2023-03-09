"""
    Exam is going to be Thursday next week in class
    MCQ, short answers, code evaluations (5 lines of code, tell us what prints)
    Debugging (you find errors in the code)
    1-2 Short Coding problems (you'll write between 10-15 lines of code)
        easier than the HW problems in general
        Goal: solve them in about 10 minutes each.
            What if I forget a colon?  Don't worry.
            Indicate tab levels with arrows
            -->
    Try to bring a pencil (you don't want to write in pen in case you need to erase)

    Material will be up to function (maybe super basic function stuff)
        variables, order of operations/operator precedence
         if statements, elif, else,
         for while
         lists (append, remove, del, indexes)
         functions (very basic)
"""

"""
    talk about what a function is
    
        it's a way that we can repeat code by jumping to a certain
            "subroutine" or "block" and we execute that block
            
        you repeat functionality quite a lot in a lot of programs
            as soon as you find yourself copy pasting code in 3+ places
        
        this is what indicates you want to put it into a function
            1) if you make a change to one of the blocks, you have to remember
                to make the same change to all of them
            2) it allows you to segment off functionality.
                keep pieces of code separate so that we understand what they're
                    doing.

"""

def is_prime(x):
    """
    :param x: an integer which we will test for being prime
    :return: True if x is prime else False
    """
    if x == 1 or x == 0:
        return False
    
    for i in range(2, x):
        """
            This loop will only run until it finds a false
            once you know that 15 % 3 == 0, you don't need to check 4, 5, 6..
            The only time that this loop will actually finish is when
                the number is prime
        """
        if x % i == 0:
            return False
    
    """
        After none of these x % i are true, it will return True
    """
    return True


def distance(x_1, y_1, x_2, y_2):
    """
        notice here that we need 4 paramaters
        
        sqrt((x_2 - x_1)^2 + (y_2 - y_1^2))
    """
    return ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** (1/2)
    

def all_uppercase(my_string):
    """
        every character MUST BE an upper case letter
        
        DIFFERENT THAN THE INBUILT PYTHON VERSION
    """
    for char in my_string:
        if not('A' <= char <= 'Z'):
            return False
        
    return True


def list_of_multiples(length, multiple):
    """
        Starting at 1, multiply by the multiple and make a list of "length"
    """
    new_list = [1]
    for i in range(length - 1):
        new_list.append(new_list[-1] * multiple)
        
    # the new_list is a local variable so it will die as soon as this function ends
    return new_list


def is_blackjack(card_1, card_2):
    """
        Ace = 11 points
        10, J, Q, K counts as 10 points
        Can't have two aces
        value, type = 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A
        suit = C, S, D, H
        2H, 3S = nothing
        AD, TC = blackjack
    """
    if card_1[0] == 'A':
        if card_2[0] in ['T', 'J', 'Q', 'K']:
            return True
    elif card_2[0] == 'A':
        if card_1[0] in ['T', 'J', 'Q', 'K']:
            return True
        
    return False

def test_other_things():
    print(__name__)
    i = int(input('Tell me an integer (-1 to exit): '))
    
    while i != -1:
        print(is_prime(i))
        i = int(input('Tell me an integer (-1 to exit): '))
    
    print(distance(0, 0, 10, 0))
    print(distance(0, 5, 0, 0))
    print(distance(0, 4, 3, 0))
    print(distance(0, 0, 2, 2))
    
    a_string = 'THIS IS A STRING 123..%^&'
    print(a_string.isupper())
    
    the_string = input('Tell me a string of uppers: ')
    while the_string.lower() != 'quit':
        print(all_uppercase(the_string))
        the_string = input('Tell me a string of uppers: ')


if __name__ == '__main__':
    print(__name__)
    import string_functions
    print(string_functions.__name__)
    my_list = list_of_multiples(10, 2)
    three_list = list_of_multiples(13, 3)
    five_list = list_of_multiples(5, 5)
    
    print(my_list)
    print(three_list)
    print(five_list)
    
    print(is_blackjack('AD', 'TH'))
    print(is_blackjack('QC', 'AS'))
    print(is_blackjack('7D', '2C'))

    print('jello', end='')
    print('\rhi', end='')