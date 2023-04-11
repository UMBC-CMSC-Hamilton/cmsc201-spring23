"""
    What is a for loop?

    A way to repeat code based on some 'iterable'
        = something that has the next object, until you get to the end
        iteration = stepping through an iterable object, item by item
"""

# starts at the first index, goes up to (not including) the last index (end)
for i in range(5, 20):
    print(i)

"""
Harmonic series:
1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 ...
"""
n = int(input('What number do you want to go up to for the harmonic sum? '))
total = 0
for k in range(1, n + 1):
    total += 1/k

print(total)

n = int(input('What number do you want to go up to for the Basel sum? '))
# 1 + 1/4 + 1/9 + 1/16 + 1/25 + ... = pi^2 / 6 weird
total = 0
for k in range(1, n + 1):
    total += 1 / k ** 2

print(total)

"""
range(stop) = range(start = 0, stop, step = 1)
    range(10) = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

range(start, stop) = range(start, stop, step = 1)
    range(5, 10) = 5, 6, 7, 8, 9

range(start, stop, step)
    The step argument is a way to jump by a certain fixed amount

"""

for i in range(1, 100, 7):
    # notice here I used end = " ", normally end = "\n"
    print(i, end=" ")

print()

for i in range(2, 200, 37):
    print(i, end=" ")

print()
"""
    
"""
a_list = [2, 5, 3, 2, 7, 9, 12, 13, 19, 3, 4, 8]
for x in range(0, len(a_list), 2):
    print(f'({x}, {a_list[x]})', end=' ')
print()

"""
    Negative steps
"""

for i in range(10, 0, -1):
    print(i, end=' : ')

print('\n I am about to do something')
for k in range(0, 100, -3):
    print(k)
print('I have done something')


print(list(range(0, 100, -3)))
# range rejects impossible choices/ranges 0 -> 100 by -3s isnt going to happen

print(list(range(17, 2000, 44)))
print(range(17, 3000, 434))

# range is lazy
print(range(1, 100000000000000000))
# this tries to allocate will die
# print(list(range(1, 1000000000000)))

print(list(range(1, 11)))

"""
    palindrome example
        if you reverse a string, it is the same
        racecar
        tacocat
        amanaplanacanalpanama
    
        a is a palindrome
        '' is a palindrome

        abccba
        012345
        len(this thing) = 6
        index 0 == index 5 = 6 - 1
        index 1 == index 4 = 6 - 2
        index 2 == index 3 = 6 - 3
        index 3 == index 2 = 6 - 4
        index 4 == index 1 = 6 - 5
        index 5 == index 0 = 6 - 6
        
        better 
        
"""
the_palindrome = input('Tell me a palindrome: ')
is_palindrome = True

for i in range(len(the_palindrome)):
    # do i need this as equals or not equals?
    if the_palindrome[i] != the_palindrome[len(the_palindrome) - 1 - i]:
        # the_palindrome[6 - i] want but it produces numbers that are 1 too big
        # so we'll correct by subtracting 1 from the index
        is_palindrome = False

if is_palindrome:
    print(the_palindrome, 'is a palindrome' )
else:
    print(the_palindrome, 'is not a palindrome')


"""
    is prime example
    
    only divisible by 1 and itself
        what about 1? it's an exception = edge cases
    
"""

is_prime = True
the_number = int(input('Enter a number and i will tell you if it is prime: '))
for d in range(2, the_number):
    if the_number % d == 0:
        is_prime = False

if the_number == 1:
    is_prime = False

if is_prime:
    print(the_number, 'is prime')
else:
    print(the_number, "is not prime")


height = int(input('Tell me height: '))
width = int(input('Tell me width: '))

for h in range(height):
    for w in range(width):
        print("*", end="")
    print()
