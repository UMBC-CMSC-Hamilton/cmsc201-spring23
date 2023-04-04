"""
    To understand the project
    
    a program in a file (text)
    a number
    python3 retriever_asm.py
    which program do you want to run?  the_program.ret 10 = MEM_SIZE

    Step 0:
        create a list of zeros of size MEM_SIZE = 10 (whatever it is)
        
    Step 1:
        Implement the mov command
        mov [2] 17
        # 17 is just 17
        #[2] is actually slot 2
        
        [3, 0, 17, 0, 0, 3, 21, 0, 0, 0]
        mov [5], 3
        mov [6], 21
        
        mov [0] [5]
        # this one is impossible, can't do this
        mov 12 [3]
        mov dest, src
   
        print out the entire list to make sure the right things
            are happening
        
        add, sub, mul, div, mod
        [3, 0, 17, 0, 0, 3, 21, 0, 0, 0]
        add [1] [0] [2]
        stick the answer in slot [1]
        3 + 17 = 20 -> [1]
        [3, 20, 17, 51, 0, 3, 21, 0, 0, 0]
        mul [3] [2] [0]
        17 * 3 -> [3]
        
        next time:
            jumps, cmp, int (print, input)
            
            nop or blank line
            hlt = stops the program
"""

"""
Recursion
    a function which calls itself
    
    
    a recursion stack:
    
    countdown(0)
    countdown(1)
    ...
    countdown(7)
    countdown(8)
    countdown(9)
    countdown(10)
"""


def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)


def smart_countdown(n):
    for i in range(n, -1, -1):
        print(i)


countdown(10)

"""
x = 1
while x > 0:
    print(x)
    x += 1
"""

"""
n! = n * (n - 1)! = n * factorial(n - 1) if n > 0
     1 if n == 0

n! = n (n - 1)(n - 2)(n - 3) ... 4.3.2.1
5! = 5 * 4 * 3 * 2 * 1 = 120
4! = 4 * 3 * 2 * 1 = 24
3! = 3 * 2 * 1 = 6
2! = 2 * 1 = 2
1! = 1 = 1
0! = 1

C(n, k) = n choose k = how many ways can i select k items out of
    a bag of n items?
    n!/ (k! (n - k)!)
C(n, 0) = well it's not exactly the formula you use some other thing
sum from 0 to infinity f^(n) (x_0)(x - x_0)^n / n!

factorial(5) calls, returns 5 * 24
factorial(4) calls, return 4 * 6
factorial(3) calls, return 3 * 2
factorial(2) calls, return 2 * 1
factorial(1) calls, returns 1 * 1
factorial(0) returns 1
"""


def factorial(n):
    if n > 0:
        k = n * factorial(n - 1)
        print("current value is", k)
        return k
    else:
        return 1


def non_rec_factorial(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


def count_as(a_string):
    # now that i've taught you slices and you can slice off the first letter
    # if i ask you to count the number of a's in a string maybe you can
    # use this idea...
    # if the first character is an 'a' add one to the count
    # else just strip it off
    if not a_string:  # if the string is empty
        print('empty string, returning 0')
        return 0
    
    if a_string[0].lower() == 'a':
        x = 1 + count_as(a_string[1:len(a_string)])
        print('Found an a', a_string)
        return x
    else:
        x = count_as(a_string[1:len(a_string)])
        print('no a', a_string)
        return x


x = int(input('>> '))
while x >= 0:
    print(factorial(x))
    x = int(input('>> '))

"""
allay
1 + count(llay)
0 + count(lay)
0 + count(ay)
1 + count(y)
0 + count('')
0
"""

"""
What is a palindrome?
    racecar
    taco cat
    a man a plan a canal panama
"""


def iter_palindrome(a_string):
    for i in range(len(a_string) // 2):
        if a_string[i] != a_string[len(a_string) - 1 - i]:
            return False
    
    return


def is_palindrome(a_string):
    # racecar -> aceca -> cec -> e
    if not a_string:
        # is '' a palindrome?
        return True
    
    # -1 == len(a_string) - 1, last element
    if a_string[0] == a_string[-1]:
        return is_palindrome(a_string[1: -1])
    else:
        return False


# counting my_string[1:len(my_string)] (just the first gets stripped)
# palindrome my_string[1: len(my_string) - 1] (both first and last get stripped)
#            my_string[1: -1]

my_string = input('str: ')
while my_string != 'quit':
    my_string = ''.join(my_string.split())
    print(my_string)
    print(is_palindrome(my_string))
    my_string = input('str: ')

"""
    fibonacci numbers
    0, 1, 2, 3, 4, 5, 6,  7,   8,  9, 10,  11
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
    
    fib(n) = fib(n - 1) + fib(n - 2)
    Base case:
        if n == 0 or 1
            return 1
"""

quatloos = 100
print(f'You have {quatloos} left')
print('You have', quatloos, 'left')


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
