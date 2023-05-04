"""

    Computational Complexity
    Asymptotic Analysis
    Time Complexity

        Given an algorithm and a size of data, how many operations does it take
            to run that algorithm?
        Can we make sense of that as a function of the size of data (n)?
        
        How does that perform as we go to infinity (large data sets)?
        
        Time Scale 1: ~ 1 ms, faster than humans notice what's happening
                   2: ~ 5 minutes human time (you can run these, but be careful)
                   3: ~ 13.6 billion years (don't run these)

    A mathematical tool that we use to describe how algorithms perform.
    
        Big-O <-- focus on Big-O, Omega
        
        f(n) is O(g(n)) when there are constants C > 0 and N >= 0 such that
            f(n) <= C g(n) [for all n >= N][eventually]
            
        "f is either in the class of g, or asymptotically less"
        
        lim_{n \to \infty} f(n)/g(n) < infinity
        
        
    3n^2 + 5n is O(n^2)
    
        3n^2 + 5n <= 8 n^2
        
    3n^2 + 5n is basically in the same class as n^2 (or it's smaller)
    
    13n is O(n^2)
    13n or n^2
    lim 13n / n^2 = 0 < infinity
    C = 13
    
"""

"""
    Recall bubble sort:
        i = 0
        while we have swapped
            swapped = False
            for j in range(0, len(the list) - i)
                if the element j and j + 1 are in the wrong order, flip them
                    set swapped to true
            i += 1
            
    inner loop takes 5(n - i) operations for each i
    
    many possibilities about the outer loop
    
    best case:
        i = 0 (if the list is sorted, swapped is never set, we only go through the outer loop once)
        5(n - 0) operations = 5n operations, O(n) <-- Omega (technically)
    
        Omega(n) = need to know this too
    worst case:
        always going to swap
        reverse sorted lists are really bad for this
        [5, 4, 3, 2, 1]
        [4, 3, 2, 1, 5] (4 operations)
        [3, 2, 1, 4, 5] (3 operations)
        [2, 1, 3, 4, 5] (2 operations)
        [1, 2, 3, 4, 5] (1 operation)
        
        sum from i = 1 to n of 5(n - i)
        Omega(n) = best case
        O(n^2) = worst case
"""

"""
    Remember selection sort:
    
    for i in range(n): this is a for loop so always does the maximum number of operations
        for j in range(i, n) going to do n - i steps just like the bubble sort
        find the ith minimum and swap it into position i
    
    sum of i = 1 to n of (n - i) = n^2 / 2 - n/2 which is O(n^2) also Omega(n^2)
    
        O = overestimate
    O(n^2) = worst case [very not true, big O is the mathematical definition, think of it as the worst case]
    Omega(n^2) = best case [same thing, very wrong but memorize it for now]
        Ω (not a great font) = line means it's a lower bound, the best case
"""

"""
Linear search and binary search

    search gives us a list, and says: find an element x in that list
    scans through the list element by element
    
    Worst Case is O(n) - need
    Average Case is O(n) = approximately O(n/2) - interesting
    Best Case is Omega(1) - need
"""


def linear_search(my_list, element):
    for i in range(len(my_list)):
        if my_list[i] == element:
            return True
    
    return False


import random

a_list = [random.randint(0, 10) for _ in range(20)]
print(a_list)

"""
    Omega(1)
    O(1)
    Generally mean constant time.
    operation doesn't depend on the list size/data structure size
    Best case of linear search is constant time because it doesn't matter how many elements are
        in the list if you find it at the first position, second, third, fourth.  n/2th position would
        not work.
    
"""

"""
Hypothetically what if maybe theoretically the list was sorted?
"""

def binary_search(my_list, start, end, the_element):
    midpoint = (start + end) // 2
    print(midpoint, my_list[midpoint])
    if start == end:
        return my_list[midpoint] == the_element
    elif my_list[midpoint] == the_element:
        return True
    
    if the_element < my_list[midpoint]:
        return binary_search(my_list, start, midpoint - 1, the_element)
    else:  # leveraging trichotomy
        return binary_search(my_list, midpoint + 1, end, the_element)


sorted_list = [1, 5, 17, 21, 34, 91, 128, 333, 721, 2842, 7700]
print(sorted_list[len(sorted_list) // 2])

print(binary_search(sorted_list, 0, len(sorted_list), 17))
print(binary_search(sorted_list, 0, len(sorted_list), 5))
print(binary_search(sorted_list, 0, len(sorted_list), 250))

"""
    Think about how it works when you divide a list in half over and over
        Hint: think about logs
"""
Ω = 4
print(Ω)
