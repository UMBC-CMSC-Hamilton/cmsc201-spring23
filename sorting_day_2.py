"""
    Log-Linear Sorts
    
        Merge Sort
        
        Quick Sort

"""
import random
"""

    Idea of Merge Sort:
    
        take first half of the list
        second half of the list
        sort them individually
        merge them back together
        
        [2 8 1 4 9 6 5 3]
        [2 8 1 4] [9 6 5 3]
        somehow magically merge sort does this:
        [1 2 4 8] [3 5 6 9]
            (it calls merge sort on the halves)
            it's a recursive sort
        "merge process"
        [1 2 3 4 5 6 8 9]
        
    Idea of merge:
        maintain two indices
        L1[i1] < L2[i2]
            take L1[i1]
            add 1 to i1
        else
            take L2[i2]
            add 1 to i2
        take the rest of the stuff in the remaining list
        
        i1 = i2 = 0
        [4 7 9 10] [1 2 3 5]
        
        i2 = 1
        [1]
        [4 7 9 10] [2 3 5]
        i2 = 2
        [1 2]
        [4 7 9 10] [3 5]
        i2 = 3
        [1 2 3]
        [4 7 9 10] [5]
        i1 = 1, i2 = 3
        [1 2 3 4]
        [7 9 10] [5]
        i1 = 1, i2 = 4
        [1 2 3 4 5]
        [7 9 10] []
        ==>
        [1 2 3 4 5 7 9 10]
"""

def merge(list_a, list_b):
    index_a = 0
    index_b = 0
    
    result = []
    
    # go until one of the lists is 'used up'
    while index_a < len(list_a) and index_b < len(list_b):
        if list_a[index_a] < list_b[index_b]:
            result.append(list_a[index_a])
            index_a += 1
        else:
            result.append(list_b[index_b])
            index_b += 1
    # one of the lists is used up but we don't know which
    for i in range(index_a, len(list_a)):
        result.append(list_a[i])
    for j in range(index_b, len(list_b)):
        result.append(list_b[j])
    
    return result


def merge_sort(the_list):
    n = len(the_list)
    if n < 2:
        return the_list
    
    first_half = the_list[0: n // 2]
    second_half = the_list[n//2: len(the_list)]
    
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    
    return merge(first_half, second_half)


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
1   [size 16]
2   [size 8] [size 8]
4   [size 4] [size 4] [size 4] [size 4]
8   [size 2] [size 2] [size 2] [size 2] [size 2] [size 2] [size 2] [size 2]
16  x [size 1]

1   [size 81]
2   [size 40] [size 41]
4   [size 20] [size 20] [size 20] [size 21]
8   7 x [size 10] + 1 [size 11]
16  15 x [size 5] + 1 [size 6]
32  17 x [size 3] + 15 x [size 2]
64  17 x [size 2] + 47 * [size 1]
81  81 x [size 1]

Total cost is n * lg(n)

lg = log base 2 rather than base 10 or base e or whatever

"""
test_sort(merge_sort, 10, 50)



def quick_sort(the_list):
    if len(the_list) < 2:
        return the_list
    
    pivot = the_list[0]
    less_list = []
    greater_or_equal_list = []
    
    for i in range(1, len(the_list)):
        if the_list[i] < pivot:
            less_list.append(the_list[i])
        else:
            greater_or_equal_list.append(the_list[i])
    
    less_list = quick_sort(less_list)
    greater_or_equal_list = quick_sort(greater_or_equal_list)
    """
        [4 1 6 8 9 3 2 5 2 3 4]
        [1 3 2 2 3] 4 [6 8 9 5 4]
        [1 2 2 3 3] 4 [4 5 6 8 9]
    """
    return less_list + [pivot] + greater_or_equal_list

test_sort(quick_sort, 10, 50)

import time
def time_test(the_sort, sizes):
    for size in sizes:
        my_list = [random.randint(0, 100) for _ in range(size)]
        start_time = time.process_time()
        print(f'Started the test on size {size}')
        the_sort(my_list)
        end_time = time.process_time()
        print(f'The time it took was {end_time - start_time}')
        
time_test(quick_sort, [10, 100, 1000, 10000, 100000])
