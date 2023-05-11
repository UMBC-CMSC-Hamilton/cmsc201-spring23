"""
May 19th 6-8 pm

    NOT IN YOUR REGULAR CLASSROOM
    either ENGR 027 or AD 101

"""

"""

[12, 5, 78, 34, 23, 8, 88, 41]
10. Bubble Sort = swaps adjacent elements
Pass 1:
[ 5 , 12 , 34 , 23 , 8 , 78 , 41 , 88 ]

Pass 2:
[ 5 , 12 , 23 , 8 , 34 , 41 , 78 , 88 ]

Pass3:
[ 5 , 12 , 8 , 23 , 34 , 41 , 78 , 88 ]

Pass4:
[ 5 , 8,  12 , 23 , 34 , 41 , 78 , 88 ]

11. Selection Sort

[12, 5, 78, 34, 23, 8, 88, 41]

Pass 1:
[ 5 , 12 , 78 , 34 , 23 , 8 , 88 , 41 ]

Pass 2:
[ 5 , 8 , 78 , 34 , 23 , 12 , 88 , 41 ]

Pass3:
[ 5 , 8 , 12 , 34 , 23 , 78 , 88 , 41 ]

Pass4:
[ 5 , 8 , 12 , 23 , 34 , 78 , 88 , 41 ]

Pass5:
[ 5 , 8 , 12 , 23 , 34 , 78 , 88 , 41 ]

Pass6:
[ 5 , 8 , 12 , 23 , 34 , 41 , 88 , 78 ]

Pass6:
[ 5 , 8 , 12 , 23 , 34 , 41 , 78 , 88 ]

"""

"""
Quick Sort this list:
[12, 5, 78, 34, 23, 8, 88, 41]
pivot = 12
[5, 8] + 12 +  [78, 34, 23, 88, 41]
pivot = 5
less = [], greater = [8]
[] + [5] + [8] = [5, 8] done

[78, 34, 23, 88, 41]
pivot = 78
[34, 23, 41] + 78 + [88]

pivot = 34
less = [23], [41]
[23, 34, 41] done

[23, 34, 41, 78, 88] done
[5, 8, 12, 23, 34, 41, 78, 88]

quick-sort you can do good things and get Omega(n lg(n)) running time in best case
    list is somewhat randomized

quick-sort does the worst with a sorted list.

1 + 2 + 3 + 4 + .. + (n - 1) = n(n -1)/2 which is O(n^2) worst case
[1, 2, 3, 4, 5]
pivot = 1, greater = [2, 3, 4, 5]
pivot = 2, greater = [3, 4, 5]
pivot = 3, greater = [4, 5]
pivot = 4, greater = [5]
base case

super easiest way is to pick the pivot randomly from the list

[9 7 8 1 5 3 4]
what if randomly we pick 1 as the pivot?
greater = [9 7 8 5 3 4], less = []

select the median (or something close to the median) but that costs extra time.
"""

"""
13. Create an expression that evaluates to True only if the string name which contains only letters, is composed of only uppercase letters.
"""
name = 'ERIC'
# don't overcomplicate things:
name.upper() == name


#
def is_upper():
    for i in range(len(name)):
        if not ('A' <= name[i] <= 'Z'):
            return False
    return True


# forbidden things to do it
all(name[i] == name[i].upper() for i in range(len(name)))
# any()

"""
14. Create an expression that evaluates to True only if the string
time contains “:” as its third character, and ends with either “AM” or “PM”
"""
time = "05:42:39 PM"
# kinda hard...
print(time[2] == ":" and (time[len(time) - 2:] == "AM" or time[-2:] == "PM"))
print(time[2] == ":" and (time[len(time) - 2:] in ['AM', "PM"]))

"""

fruits = {"apples": 5, "oranges": 9, "grapes": 2}

15. print( fruits["grapes"], fruits["oranges"], fruits["apples"] )

2 9 5

16. print( fruits.get("oranges", "buy groceries!") )

9

17. print( fruits.get("pears", "buy groceries!") )

if there's no parameter in the .get function it returns None

buy groceries!

18. print( fruits["rhubarb"] )

KeyError (only have say error)

19. fruits['papaya'] = 17
print( fruits )

{"apples": 5, "oranges": 9, "grapes": 2, "papaya": 17}

"""

"""

20. What is the Big Ω run time for linear search?  (2 points)

    finds it the first try:
    Ω(1)

21. In what scenario would the best case occur for a selection sort?  (4 points)

    Trick Question
    Any list produces the best and worst cases because they are the same.
    Ω(n^2) = best,  O(n^2) = worst

22. What is the Big Ω run time for binary search?  (2 points)
    finds it the first try:
        Ω(1)
    Big-O time:
        O(lg(n))
23. In summary, what scenario would the best case occur for search algorithms?  (4 points)

    If you find the element on the first try, you get Ω(1).

24. When would you need to use linear search over binary search? (4 points)

    List is unsorted.

"""

"""
Memorize or be able to derive the chart:
0       0       0000
1       1       0001
2       2       0010
3       3       0011
4       4       0100
5       5       0101
6       6       0110
7       7       0111
8       8       1000
9       9       1001
10      A       1010
11      B       1011
12      C       1100
13      D       1101
14      E       1110
15      F       1111

5. Convert the decimal number 19
 	to binary: 		_________________
 	    0001 0011
 	    10011
 	    19//2 => 9 (odd) // 2 => 4 (even) //2=> 2 (even) //2 => 1 (odd)
 	to hexadecimal:	_________
        0x13 = 13h
        16 + 3 = 19
26. Convert the decimal number 241
 	to binary: 		_________________
 	to hexadecimal:	_________
    241 -> 120 -> 60 -> 30 -> 15 -> 7 -> 3 -> 1
    1111 0001
    0xF1

27. Convert the binary number 1011 1001
 	to decimal: 		_________
 	to hexadecimal:	_________
        128 + 32 + 16 + 8 + 1 = 185
        0xB9 = 11 * 16 + 9 = 176 + 9 = 185 so good

28. Convert the hexadecimal number 8B12AA12
 	to binary: 	_____________________________________________________
    8B12AA12 = 1000 1011 0001 0010 1010 1010 0001 0010
"""

"""
string, int float, bool pass by value / immutable (python specific)
    a copy is made so the local variable cannot overwrite the global variable

29) summer

"""


def hello(count):
    if count < 0:
        return
    print("hello")
    if count % 3 == 0:
        hello(count - 8)
    else:
        hello(count + 1)


if __name__ == '__main__':
    hello(15)
"""
hello(15)           hello
hello(7)            hello
hello(8)            hello
hello(9)            hello
hello(1)            hello
hello(2)            hello
hello(3)            hello
hello(-5)
"""


def square_area(side_length):
    return side_length ** 2


if __name__ == '__main__':
    print(square_area(square_area(2)))

threeD = [[
    [201],
    [202, 203]],
    [
        [331, 341],
        [304, 313]
    ]]
print(threeD[0][0][0] == 201)
print(threeD[0][1][0] == 202)
print(threeD[1][0][1] == 341)


def func(first, second):
    if first <= 0:
        return -1
    if first == 1:
        return second
    return second + func(first - 1, second)


if __name__ == '__main__':
    ans = func(3, 9)
    print(ans)

"""
func(3, 9) = 9 + func(2, 9)
func(2, 9) = 9 + func(1, 9)
func(1, 9) = 9

27
"""
