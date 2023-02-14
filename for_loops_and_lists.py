"""
for loops and lists

what is a for loop?
    our first way to repeat code that we may want to do more than once

"""
if False:
    first_num = int(input('Tell me the first number: '))
    second_num = int(input('Tell me the second number: '))
    third_num = int(input('Tell me the third number: '))
    fourth_num = int(input('Tell me the fourth number: '))
    fifth_num = int(input('Tell me the fifth number: '))

    the_sum = first_num + second_num + third_num + fourth_num + fifth_num
    print('The total is', the_sum)

    """
        range(5)
        starts at 0 and gives us each number in order increment of +1 until we get upto but
            NOT INCLUDING 5
    """
    new_sum = 0
    for index in range(20):
        # += is the same as
        new_sum = new_sum + int(input('Tell me the next number: '))

    print('The new sum is', new_sum)


    """
        Gauss sum
        
        Favorite sum (not really but for 201 purposes it is)
        1 + 2 + 3 + 4 + 5 + 6 + ... + n
        
        let's try to do this with a for loop
    """
    n = int(input('How far do you want to add? '))

    gauss_sum = 0
    for count in range(n + 1):
        gauss_sum += count  #  += same as gauss_sum = gauss_sum + count
        # ++ doesnt exist in python

    print(gauss_sum)
    """
        To annoy Gauss he was given these problems
        he figured out that the answer is:
        n(n + 1) // 2
    """

    """
        Factorial
            instead of the gauss sum which adds:
            1 + 2 + 3 + ... + n
            it is the product from 1 to n
            n! = 1 * 2 * 3 * ... * n
            0! = 1
    """

    n = int(input('What factorial do you want? '))

    fact = 1
    for count in range(n + 1):
        if count > 0:
            fact *= count  #  += same as gauss_sum = gauss_sum + count
        # ++ doesnt exist in python

    print(fact)


    """
    Lists are the corresponding object for the for loop to act on
    
    a list is a collection of variables that we can access by their index
    """
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
    # for each loop, which takes each element and sets it into the index variable
    for vowel in vowel_list:
        print('One of the vowels is', vowel)

    """
        How do we access individual elements out of a list?
        
        We use the array brackets/list brackets
        
            [index]
            index either be a literal or a variable, or an expression that evaluates to int
    """
    print(vowel_list[2], vowel_list[4])
    print(vowel_list)
    # print(vowel_list[17]) IndexError

    movie_list = []
    for i in range(7):
        movie_name = input('Tell me a movie: ')
        movie_list.append(movie_name)
        print(movie_list)

    print('Our movies are: ', movie_list)

number_list = [3, 7]
for i in range(5):
    my_num = int(input('Tell me a number: '))
    number_list.append(my_num)

print(number_list)
a = int(input('Tell me the index: '))
b = int(input('Tell me another index'))

print(number_list[a], number_list[b], number_list[a] + number_list[b])

a_count = 0
my_string = input('Tell me a string: ')
for char in my_string:
    if char.lower() == 'a':
        a_count += 1

print(f'We found {a_count} a\'s in the string {my_string}')

"""
We want to detect if two A's are next to each other.

0 1 2 3 4 5 6 7 8 9 10 11 12
a p p l e a a r d v a  r  k
"""

for i in range(len(my_string) - 1):
    # if i < len(my_string) - 1 and my_string[i] == my_string[i + 1]:
    if my_string[i] == my_string[i + 1]:
        print(f'There are two {my_string[i]} at {i} and {i + 1}')