"""
    What is control flow?
        sequential - execute one line of code and then go to the next line
            examples are Print, input, math calculations, string calculations
        conditional - execute a statement that determines whether to jump
            to a different line or continue onto the next line
        iterative - loops (for and while) (do while, do unless)
            any code that repeats itself based on some index, counter, condition
        functional - you can jump to and execute a block of code from anywhere
            in your program.  when you're finished it will return you to the
            place that called the function
            
            you can pass your function "messages" we call them arguments
            your function can pass messages back, we call that returning
        
    What is a function?
        a function is a block of code, syntax in python is similar
    Gives some examples!
    
    Anything else about functions? Arguments vs Parameters
    Scope - in programming

"""


def my_first_function():
    print('hi i am a function')


def square_me(x):
    print(x ** 2)
    return x ** 2


my_first_function()
my_first_function()
my_first_function()

square_me(5)
square_me(7)
square_me(12)


def create_list_of_size(the_size):
    new_list = []
    for i in range(the_size):
        new_list.append(input('Enter something for the list: '))
    print(new_list)
    
"""
    we generally call this scope
        because all variables inside a function have a finite lifetime
        you can't just create a variable inside a function and then
            use it later... because the variable name is forgotten
            
"""


def count_as(a_string):
    count = 0  # local version
    # this version of count only exists while the function is running
    # every time you call the function it resets to 0
    for the_char in a_string:
        if the_char.lower() == 'a':
            count += 1
    # this is the way to pass a message back to the main program
    return count


# create_list_of_size(3)
# create_list_of_size(8)
# create_list_of_size(4)
# create_list_of_size(0)


count = 0  # global version
print(count_as('aardvark'))
if count_as('aardvark') > 0:
    count += 1
print(count_as('apple amber'))
if count_as('apple amber') > 0:
    count += 1
    
print(count)

my_var = square_me(17)
print(my_var)
square_me(18)
