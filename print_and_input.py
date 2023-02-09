"""

    python is an interpreted language
            CPython is the main interpreter for python
                Java, javascript, ruby, C#, lisp
                there is an intermediate step between your code and the machine

            compiled languages = in the end when we run a compiler it will translate our code
                    into machine code.
                assembly language
                C/C++
                rust
"""

"""
print command
 = built in function
 
 print can output a bunch of different data types
"""

print('this is a string')
print(57)
print(3.14159265)
print(True, False)

"""
4 basic data types are 
    string, integer (int) float, bool
"""

print(3, 4, 5, 6, 7)
print('hello', 17, 2.7182818459, False)

"""
We call things like 3, 'hello', False literals

    string literals = its a hard coded string, not inputted not a variable etc
    otherwise just a literal
"""

print(3 + 6, "hello" + "world")
"""
    string concatenation - putting two strings together.
"""
print('windows' + "update" + "is bad")
# no distinction between single ' and "

# empty print will insert a newline
print()

print("x\ny" "z") # weird but allowed

"""
Escape sequences \n  = new line
    \t = tab
    \'
    \"
    \a = not used anymore
    \r = carriage return
    
    all newlines in windows are still actually \r\n
"""

print('Eric\'s car')
print("Eric's car.  Also he said \"come to class\"")

"""
    if we want to talk about input we need to put the result into some place in memory
    
    variables allow us to store data in memory
    
    in python, not strictly typed you dont have to declare the type of variable that youre using
        you are permitted to simply assign the variable the first time
"""

my_string = "hello this is a string"
my_integer = 343
the_float = 1.6
the_bool = True
print(my_string, my_integer, the_float, the_bool)

# not strictly typed
the_bool = 52
print(the_bool)

"""
    Variable naming rules
    
        must start with an underscore or a letter, not a number, no symbols !@#$%^&*(
        after that it can be letters numbers and underscores


    7_is_a_number = 7 Syntax
    !this_variable! also illegl
    $varname = perl but definitely not python
        
"""
hello_world = "this is our first program"
__double_underscores_are_cool = 5
__THIS_VARIABLE = 4.2
h324324324 = 7

my_input = input("Tell me a word: ")
print("the word was", my_input)

# casting string into an int using the int "constructor" or function
the_number = int(input('Tell me a number: '))
print(the_number + 5)
# try except but we'll have to wait
# for now you can assume that all data types will be entered correctly

the_float = float(input('tell me a number with a decimal: '))
print(the_float + the_number)

print(3.81 - 2.81)

print(f"the number is {the_number} and the_float is {the_float} and the cow says {my_input}")
print("%d %s" % (the_number, my_input))

"""
    all of my variables are in something called snake case
    
        lowercase words and numbers separated by underscores
        
    the variable describes what it is you're doing with the variable
    
    the_radius, approximate_result, window_button, response
    
    camelCaseIsLikeThis -> java, javascript, similar la
    CapitalCaseIsLikeThis
    
"""