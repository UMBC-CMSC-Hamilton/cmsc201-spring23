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

"""

line numbers match - 300
# find_vowels() counts number of vowels in a string
# Parameters:  sentence;  a string
# Return:      num_vowels; an integer
def find_vowels(sentence):
    num_vowels = 0
    for i in range(len(sentence): # missing paren

        if sentence.upper() in ["A", "E", "I", "O", "U"]: # add sentence[i]
            num_vowels += 1
    return 0  # return num_vowels
if __name__ == '__main__':
    total_vowels = 0
    with open("myfile.txt", "r") as my_file:
       line_list = my_file.readlines()  # alternatively delete this line

       for line in my_file:  # line_list
           # count number of vowels in each list
           total_vowels += find_vowels(line)
    
        print("There are", total_vowels, "vowels") # back one tab level

"""

"""

# recur_max() takes in a list and finds the maximum element
# Parameters:  my_list; a NON-EMPTY list of numbers
# Return:      a numerical value, zero if empty
def recur_max():  # my_list needs to be a parameter
    # BASE CASE: list has only one element
    if not len(my_list):
        return 0
    else:
        # find maximum of the list without the first element
        max_rest = recur_max(my_list[2: ])  # start at [1:]
        if max_rest < my_list[0]:
            return my_list[0]
        else:
            return max_rest[0]  # remove the index [0]
if __name__ == '__main__'  # no colon
    temp_val = int(input("Please enter a num (0 to stop): "))
    the_list = # add [] or list()
    while temp_val == 0: # change == to !=
        the_list.append( temp_val )
        temp_val = int(input("Please enter a num (0 to stop): "))

    list_max = recur_max( the_list )
    print(f"The maximum element in the list is {list_max}")
    print("The maximum element in the list is", list_max)
    print("The maximum element in the list is"+ str(list_max))

"""


def is_power_2(num):
    if num == 0:  # 2^x = 0
        return False
    elif num % 2 == 0:
        return is_power_2(num // 2)
    elif num == 1:
        return True
    else:
        return False


"""
    2 * 2 * 2 * 2 * 2 * 2 * ... * 2
    does it have a factor of two?
    if yes we can divide it
"""


def create_2d_list(height, width, symbol):
    my_grid = []
    for i in range(height):
        new_row = []
        for j in range(width):
            new_row.append(symbol)
        my_grid.append(new_row)
        # print(my_grid)
    return my_grid


"""
    my_grid = [reference to the first sublist, reference to the second sublist, ...]
"""

the_list = create_2d_list(4, 3, "+")

for i in range(len(the_list)):
    print(the_list[i])

the_list[2][2] = 'a'
print('-------------------------')
for i in range(len(the_list)):
    print(the_list[i])

"""
Final Exam:
    This Friday May 19th From 6pm - 8pm AD 101

Total Review of everything:
    variables:
        immutable = bool, float, int, string
        when you pass them in functions get passed by value
            a copy is made
        mutable = lists, dictionaries, classes
        when you pass them into a function they actually pass by reference
            a reference is given
            a reference is a memory location where the original variable is
            local variable name may be different but the actual data is the same
            
        python legal variable names:
            start with a letter or underscore
            contains letters numbers, underscores
            no characters like !@#$%^&*()
        python coding standards PEP8
            lowercase with underscores = snake case
    if statements/elif/else
        order of operations/order of operator precedence
        arithmetic ()*//%+-
            ()
            **
            *, //, /, %
            +, -
        comparisons
            < > <=, >=, ==, !=, in
        logic
            not
            and
            or
            
        (X and Y) or Z
        X and (Y or Z)
        
        How many elifs can we have in a single expression?
            infinity, however many you want, many
        (At most) How many elifs in a single expression will possibly execute?
            1
        Does an if statement need an else?
            no
    for loops:
        when you know how many times you're going to run the loop [most of the time in life]
        for-each
            for x in my_list:
            
                Can't modify x, if x is immutable
                But if x is mutable then you 'can' modify it somewhat
        for-i index loops
            for i in range(len(my_list)):
            
"""
Ω = 5
print(Ω)

my_list = [[1, 2], [3, 4], [5, 6]]

for x in my_list:
    # since x is a reference you can modify these sublists
    x.append(7)
print(my_list)


for x in my_list:
    # more weirdness
    x = [3, 9, 12]
    
print(my_list)

another_list = [1, 2, 3, 4, 5, 6]
for x in another_list:
    x += 1

print(another_list)


"""
    while loops = if statement on repeat
        don't know how many times you're going to run a particular thing
        
        GUI programming (message loops)
        servers (message loops)
        input validation (keep asking the user for proper input before continuing)
        game (chess, checkers, minesweeper, cards, etc)
        (usually there's only a few of them in any piece of code)
    
        Problems:
            infinite loop: while True (and never gets set to false)
        Feature:
            skipped loop: while condition, condition is false before entering, the
                loop is skipped
"""


"""
    functions and recursion
        parameters are input into the function (arguments which become the parameters)
        parameters and other local variables are in the local scope:
            these variables live as long as the function does, and then python forgets
                their names, eventually the python garbage collector will run
                lost or deleted, garbage collected
                
    
    recursion
        base case
            doesn't call additional recursions
        recursive case
            does!
            
        a recursion can cause a "stack overflow" / RecursionError (about 1000 recursion depth)
        
    
"""
# declaration, name (parameters)
# what does the function "need to know"
def happy_function(my_string, my_int, my_float):
    if my_float > 0:
        return my_string * my_int
    else:
        return "sunk"


print(happy_function("asdf", 5, 3.2))