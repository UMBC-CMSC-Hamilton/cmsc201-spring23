a_map = {"squirrel": 15, "bear": 31, "turnip": 71, "broccoli": 45}
a_map['chocolate'] = 5
for x in a_map:
    print(x)

"""
    20. Write a boolean expression that returns True when
    the dictionary names contains the keys "Eric" but does
    not contain "George"
"""
names = {}  # don't need this
# this is the answer here:
'Eric' in names and 'George' not in names

"""
21. Write a boolean expression that returns True when
row is a legal index for my_2d_list and col is a legal
 index for my_2d_list[row].

legal = it must be a non-IndexError
"""
my_2d_list = [[1, 2, 3, 4, 5, 5, 6], [3, 4, 5]]
row = 0
col = 0
# the answer is below:
0 <= row < len(my_2d_list) and 0 <= col < len(my_2d_list[row])

"""
    starting at top left and going clockwise:
    name / signature
    parameters
    the function itself
    function call
    body of the function
"""

a_list = [[2, 4, 6], [1, 2, 8], [3, 11, 17]]
for x in range(5, 7):
    print(a_list[x % 3][(2 * x + 2) % 3])

"""
x = 5
    a_list[5 % 3][(2 * 5 + 2) % 3]
    a_list[2][0] = 3
x = 6
    a_list[6 % 3][(2 * 6 + 2) % 3]
    a_list[0][2] = 6
___end work__
    3
    6
"""

test_string = "abracadabra"
print("z".join(test_string.split("a")))
# practice a little bit with join and split
print('z'.join(['', 'br', 'c', 'd', 'br', '']))

"""
# findVowels() counts number of vowels in a string
# Parameters:  sentence;  a string
# Return:      numVowels; an integer
def findVowels(sentence):
    numVowels == 0 <-- comparison not assignment
    for i in range(len(sentence): missing paren
        if sentence[i](fix).upper() in ["A", "E", "I", "O", "U"]:
            numVowels += 1
    return 0 -> numVowels

def main():
    totalVowels = 0
    myFile = open("myFile.txt")
    lineList = myFile.readlines()

    for i in range(len(myFile -> lineList)):
        #count number of vowels in each list
        totalVowels += findVowels(lineList[i])
    (reverse-indent)print("There are", totalVowels, "vowels in this file")
    close(myFile) ->myFile.close()

main()

"""


def fileMin(filename):
    with open(filename) as the_file:
        my_lines = the_file.readlines()
        # strip off the new line and maybe other whitespace
        # set the current minimum to one of the lines
        if not my_lines:
            return 0
        # can't run this line if the file is empty
        current_min = int(my_lines[0].strip())
        for x in my_lines:
            value = int(x.strip())
            if value < current_min:
                current_min = value
        
        return current_min
    # the_file.close() if you didn't use with keyword


def the_sum(number):
    """
        the_sum returns the sum from 0 up to number
        the_sum(number - 1)
    """
    if number == 0:
        return 0
    
    return number + the_sum(number - 1)
