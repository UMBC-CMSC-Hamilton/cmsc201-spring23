"""
    Midterm 2 next thursday, I'll send out a practice test
        within a day or two.
    Everything up to sorting, functions, parameters, arguments
        lists, dictionaries, fileIO (review that lecture)

    Sorting:
        It's our first examination of algorithms.
        CMSC 341 Data Structures
        CMSC 441 Algorithms
        
        Sorting using comparisons is "Solved"
        
    Quadratic Sorts:
        Bubble Sort
            Idea:
                compare items next to each other in a list
                if they're in the wrong order, swap them
            First Iteration:
                [5 7 3 9 4 1]
                [5 3 7 9 4 1]
                [5 3 7 4 9 1]
                [5 3 7 4 1 9]
            Second Iteration:
                [3 5 7 4 1 9]
                [3 5 4 7 1 9]
                [3 5 4 1 7 9]
            Third Iteration:
                [3 4 5 1 7 9]
                [3 4 1 5 7 9]
            Fourth Iteration:
                [3 1 4 5 7 9]
            Fifth Iteration:
                [1 3 4 5 7 9]
                
            [5 4 3 2 1]
            First:
            [4 5 3 2 1]
            [4 3 5 2 1]
            [4 3 2 5 1]
            [4 3 2 1 5]
            Second:
            [3 4 2 1 5]
            [3 2 4 1 5]
            [3 2 1 4 5]
            Third:
            [2 3 1 4 5]
            [2 1 3 4 5]
            Fourth:
            [1 2 3 4 5]

        [1, 2, 3, 4, 5]
"""

import random


def bubble_sort_for(my_list):
    for iteration in range(len(my_list) - 1):
        # don't have to check the last "iter" of them
        # they are already sorted
        swapped = False
        for i in range(len(my_list) - 1 - iteration):
            # the extra -1 here prevents an IndexError
            if my_list[i] > my_list[i + 1]:
                temp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = temp
                swapped = True
        if not swapped:
            return


def bubble_sort_while(my_list):
    iteration = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(my_list) - 1 - iteration):
            # the extra -1 here prevents an IndexError
            if my_list[i] > my_list[i + 1]:
                temp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = temp
                swapped = True
        iteration += 1


"""
    Selection Sort - my favorite
    
        scan the list, pick the minimum and swap it back
        
        [5 4 9 2 3 7 1]
        i = 0
        [1 4 9 2 3 7 5]
        i = 1
        [1 2 9 4 3 7 5]
        i = 2
        [1 2 3 4 9 7 5]
        i = 3
        [1 2 3 4 9 7 5]
        i = 4
        [1 2 3 4 5 7 9]
        i = 5
        [1 2 3 4 5 7 9]
        i = 6
        [1 2 3 4 5 7 9]
"""


def selection_sort(my_list):
    for i in range(len(my_list)):
        min_index = i
        # finds the minimum
        for j in range(i + 1, len(my_list)):
            # we were wrong about our current min_index a smaller element is at j
            if my_list[min_index] > my_list[j]:
                min_index = j
        # does the swap
        if min_index != i:
            temp = my_list[min_index]
            my_list[min_index] = my_list[i]
            my_list[i] = temp
    
    return my_list


def test_sort(the_sort, num_tests, test_size):
    for i in range(num_tests):
        random_list = [random.randint(0, 50) for _ in range(test_size)]
        print(random_list)
        copy_of_list = list(random_list)
        
        random_list = the_sort(random_list)
        copy_of_list.sort()
        
        if random_list == copy_of_list:
            print('The List has been sorted')
            print(random_list)
        else:
            print('The List has not been sorted')
            print(random_list)


"""
    Insertion Sort
    
    "pull back sort"
"""


def insertion_sort_better(my_list):
    for i in range(1, len(my_list)):
        j = i
        temp = my_list[i]
        while j > 0 and my_list[j - 1] > my_list[j]:
            my_list[j] = my_list[j - 1]
            j -= 1
        my_list[j] = temp
    
    return my_list


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        j = i
        while j > 0 and my_list[j - 1] > my_list[j]:
            temp = my_list[j]
            my_list[j] = my_list[j - 1]
            my_list[j - 1] = temp
            j -= 1
    
    return my_list


test_sort(insertion_sort, 10, 25)

"""
    You know three sorts:
        BubbleSort, SelectionSort, InsertionSort
        
    How fast do they run?
        number of operations is approximately n^2 for a list of size n
        

Selection Sort:
n comparisons and maybe swap

[5 4 3 2 1] first scan ->                   4 comparisons
[1 4 3 2 5] second scan ->                  3 comparisons
[1 2 3 4 5] third scan -> (starts at 3)     2 comparisons
[1 2 3 4 5] fourth scan -> (starts at 4)    1 comparison
[1 2 3 4 5] fifth scan -> (starts at 5)     0 comparisons

0 + 1 + 2 + 3 + 4 = 10

If you have a list of size n:
n + (n - 1) + (n - 2) + (n - 3) + (n - 4) + .... + 1

This is Gauss Sum (this is a name for it)

add up 1 + 2 + 3 + ... + n = n(n + 1) / 2
    proof is next time

(1/2) n^2 + (1/2) n
"""

import time


def time_test(the_sort, sizes):
    for size in sizes:
        my_list = [random.randint(0, 100) for _ in range(size)]
        start_time = time.process_time()
        print(f'Started the test on size {size}')
        the_sort(my_list)
        end_time = time.process_time()
        print(f'The time it took was {end_time - start_time}')
        

time_test(selection_sort, [10, 100, 1000, 10000, 100000])
