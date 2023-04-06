"""
    What is recursion?
        recursion is when a function calls itself.
        
        russian nesting dolls are sort of recursive
        
    last one is called the base case
    need base cases for two reasons
        1) if we weren't in python, we would exhaust memory or go on forever
        2) python has a hard limit of 1000 (about 1000) recursions
            RecursionError
"""

"""
    fib(n) = fib(n - 1) + fib(n - 2)
    fib(1) == fib(0) == 1
"""

def fibonacci(n):
    print(f'fib {n}')
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


"""
Example: a's and b's
    we are going to make all of the combinations of a's and b's of length n

    n = 0 '' only one, empty
    n = 1
        a   b
    n = 2
        aa ab
        ba bb
    n = 3
        aaa aab
        aba abb
        baa bab
        bba bbb
        [ the answer at length n is the 'a' + answer at length n - 1
                                        'b' + answer at length n - 1]
    n = 4:
        aaaa aaab
        aaba aabb
        abaa abab
        abba abbb
        baaa baab
        baba babb
        bbaa bbab
        bbba bbbb

"""

def as_and_bs(n, current):
    if n == 0:
        print(current)
        return ''
    
    as_and_bs(n - 1, current + 'a')
    as_and_bs(n - 1, current + 'b')
    


"""
    list all the a's and b's of a certain length with exactly k a's
"""


# n is the amount of string we need, k is the number of a's that we need
def as_and_bs_exact_k(n, k, current):
    if n == 0:
        if k == 0:
            print(k, current)
        return
    
    if k > 0:
        as_and_bs_exact_k(n - 1, k - 1, current + 'a')
    
    as_and_bs_exact_k(n - 1, k, current + 'b')


n = int(input("Enter the length: "))
k = int(input("Enter the number of a's: "))
as_and_bs_exact_k(n, k, '')


"""
    pathfinding on a grid
    
    * _ s *
    * _ * e
    _ _ _ _
    * _ _ *
    
    depth first search

    build a grid
"""


import random

def build_grid(height, width, prob):
    my_grid = []
    for i in range(height):
        new_row = []
        for j in range(width):
            # floating point number between [0, 1]
            if random.random() < prob:
                new_row.append('*')
            else:
                new_row.append(' ')
        my_grid.append(new_row)
    return my_grid

def display_grid(the_grid):
    for row in the_grid:
        print(''.join(row))


the_grid = build_grid(10, 10, 0.25)
display_grid(the_grid)

