square_me = lambda x: x ** 2
all_true = lambda x, y, z: x and y and z

print(square_me(5))
print(square_me(7))
print(all_true(True, False, True))
print(all_true(True, True, True))

print((lambda x: x + 2)(5))


def distance(x, y):
    d = 0
    for i in range(len(x)):
        d += (x[i] - y[i]) ** 2
    return d ** (1 / 2)


"""
    What if you are calling a function that will call the distance function but only
    give one point, the other point is assumed to be zero (0, 0, 0)
    
    
"""

# if you do this, it will immediately evaluate
# distance((0,0,0), y)
# y won't exist and it'll give you an error
# a function of y that when you put in a y, this thing will evaluate

zero_dist = lambda y: distance((0, 0, 0), y)
print(zero_dist((2, 3, 4)))

"""
errors in python
"""

file_name = input('Enter file name: ')

try:
    with open(file_name) as the_file:
        print(the_file.read())
        print(5 // 0)

except FileNotFoundError as fnfe:
    print(fnfe)
except ZeroDivisionError:
    print('Why did you try to divide by zero?')

print("hello there")

the_input = input('Enter an integer: ')
the_number = 0
set_number = False
while not set_number:
    try:
        the_number = int(the_input)
        print('That was an integer')
        set_number = True
    except ValueError:
        print('That was not an integer')
        the_input = input('Enter an integer: ')

"""
    break should be used sparingly
    
    IT SHOULD NEVER TAKE THE PLACE OF A WHILE CONDITION
    
    similar about continue
        continue is even more rare
"""
print(the_number)


def my_function(**keywords):
    print(keywords)


my_function(a=17, c="happy", b=31, robot='chicken')


def my_print(the_string, end="\n", sep=" "):
    print(the_string, end=end, sep=sep)


my_print("hello", sep='happy', end="::")
