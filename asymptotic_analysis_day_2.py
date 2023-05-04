"""
Idea:
    Way to measure performance of algorithms based on the running time
        depending on the size of the data set
    Big-O = upper bound, it can be used to describe the worst case of an algorithm
        f(n) is O(g(n)) when there are constants C and N so that
            f(n) <= C * g(n) for n >= N
            g(n) is a bigger or equal class of function than f
        
        n^2 is O(n^3) why?
        n^2 <= 1 * n^3
        50 * n^2 <= C * n^3
        if you pick C = 1, then you have to solve:
        
        50 n^2 <= n^3
        Divide out by n^2
        50 <= n
        Pick N = 50
        
        Big-O just requires that there are SOME constants C, N to do this.
            doesn't mean that it works for ALL C, N
        
        O(n^2)
            Bubble Sort, Selection Sort, Insertion Sort
            Omega(n)        Omega(n^2)      Omega(n)
        O(n)
    Omega = lower bound, we can use this to describe the "best case"
        f(n) is Omega(g(n)) when there are constants C, N
            so that f(n) >= C g(n) for n >= N

    Log base change formula:
        log_a(x) = log_b(x) / log_b(a)
        "All logs are the same in O, Omega, Theta"

    Log-Linear Sorts: Average time is n * lg(n), lg(n) = log_2(n)
        Merge Sort:
        
        Quick Sort:
"""

def merge(a_list, b_list):
    # a_list -> n
    # b_list -> m
    # total runtime here is n + m, O(n + m), Omega(n + m) -> Theta(n + m)
    a_index = 0
    b_index = 0
    sorted_list = []
    while a_index < len(a_list) and b_index < len(b_list):
        if a_list[a_index] < b_list[b_index]:
            sorted_list.append(a_list[a_index])
            a_index += 1
        else:
            sorted_list.append(b_list[b_index])
            b_index += 1
            
    for i in range(a_index, len(a_list)):
        sorted_list.append(a_list[i])
    for j in range(b_index, len(b_list)):
        sorted_list.append(b_list[j])

    return sorted_list


def merge_sort(the_list):
    # divides our list in half, sorts the bottom half, top half and then it runs
    # the merge operation
    if len(the_list) <= 1:
        return the_list
    midpoint = len(the_list) // 2
    lower = merge_sort(the_list[0: midpoint])
    upper = merge_sort(the_list[midpoint:])
    return merge(lower, upper)

"""
100
50 50 -> 100 merge points
25 25 25 25-> 50 + 50 = 100 merge points
12 13 12 13 12 13 12 13 = 25 + 25 + 25 + 25 = 100 merge points
6 6 6 7 6 6 6 7 6 6 6 7 6 6 6 7 = 100
3 3 3 3 3 3 3 4 3 3 3 3 3 3 3 4 3 3 3 3 3 3 3 4 3 3 3 3 3 3 3 4 3 3 3 3 3 3 3 4 = 100
[a bunch of 1's and 2's] if it's all 1's then it's going to be 100 x 1's = 100

Cost is always the same at each level, it's always the size of the list.
*
Log base 2 of the size of the list number of times.

O(n lg(n))
Omega(n lg(n)) time, always
Therefore it's Theta(n lg(n))
"""



"""
    [4, 2, 7, 1, 3, 9, 5]
    pivot = 4
    [2, 1, 3], [7, 9, 5]
    2 [1] [3]    7, [5], [9]
    [1, 2, 3] + [4] +  [5, 7, 9]
    [1, 2, 3, 4, 5, 7, 9]
"""

def quick_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    
    # you can be smarter than this, but this is the traditional textbook version
    pivot = the_list[0]
    less_list = []
    bigger_list = []  # equal list too
    for i in range(1, len(the_list)):
        if pivot >= the_list[i]:
            bigger_list.append(the_list[i])
        else:
            less_list.append(the_list[i])
    less_list = quick_sort(less_list)
    bigger_list = quick_sort(bigger_list)
    # + means list concatenation, so it will just add the lists together
    return less_list + [pivot] + bigger_list

"""
    Here's the argument:
        If quick sort goes well, then it'll split the list into about half each time.
        less and greater lists will be approximately the equal size
        this is a lot like merge sort, so it will give us n * lg(n) time [ true ]
        
    Worst case for quick-sort-textbook:
    
        what if we have a sorted list?
            
            
            [1, 2, 3, 4, 5, 6, 7, 8]
            less = [] pivot = 1 greater = [2, 3, 4, 5, 6, 7, 8]
            less = [] pivot = 2 greater = [3, 4, 5, 6, 7, 8]
            less = [] pivot = 3 greater = [4, 5, 6, 7, 8]
            less = [] pivot = 4 greater = [5, 6, 7, 8]
            less = [] pivot = 5 greater = [6, 7, 8]
            less = [] pivot = 6 greater = [7, 8]
            less = [] pivot = 7 greater = [8] (base case)
            basically 7 steps on a list of size 8
            this would be n - 1 steps on a list of size n
            
            we have to run the thing that costs 2n, n times
            2n^2 which is O(n^2) = worst case of quick_sort
            
            quick_sort can kind of "malfunction" = it will sort the list so it will
                work, but it's just going to take way way way longer than you expect
"""

import time
import random
import sys


size = 3500
for i in range(10):
    random_list = [random.randint(0, 100) for _ in range(size)]
    start_time = time.process_time()
    quick_sort(random_list)
    print(f'It took {time.process_time() - start_time}')


sys.setrecursionlimit(10000)
"""
start_time = time.process_time()
sorted_list = [i for i in range(size)]
quick_sort(sorted_list)
print(f'It took {time.process_time() - start_time}')
"""

"""
Overview (what you need to know for the final):
                Worst           Best
Bubble*         O(n^2)          Omega(n) = if sorted
Selection*      O(n^2)          Omega(n^2) = does the same thing every time
Insertion       O(n^2)          Omega(n) = if sorted
Quick*          O(n^2)          Omega(n lg(n)) : average case is n lg(n)
Merge           O(n lg(n))      Omega(n lg(n))

Linear Search*  O(n)            Omega(1)
Binary Search*  O(lg(n))        Omega(1)
"""

"""
Talk about the runtime:
    Like merge sort only it doesn't have to merge
    Binary search = only if you have a sorted list
    [2, 6, 9, 10, 11, 15, 21]
    middle = 10
    looking for 21
    i know that the thing i'm looking for has to be in the upper half of the list
    [11, 15, 21]
    middle = 15 looking for 21, ah same thing go up
    [21] -> cool
    
    n
    n/2
    n/4
    n/8
    n/16
    n/32
    ...
    n/2^k = approximately 1
    solve for k
    n = 2^k (approx)
    lg(n) ~=~ k
    what is k? = number of times we have to run the recursion
    O(lg(n))
"""


def time_test(the_sort, sizes):
    for size in sizes:
        my_list = [random.randint(0, 100) for _ in range(size)]
        start_time = time.process_time()
        print(f'Started the test on size {size}')
        the_sort(my_list)
        end_time = time.process_time()
        print(f'The time it took was {end_time - start_time}')


time_test(merge_sort, [10, 100, 1000, 10000, 100000, 1000000])
