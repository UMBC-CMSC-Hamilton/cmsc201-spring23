"""
    How do you open a file?
        there is a special function, print, input write and read to the stdout and stdin
        
        open()
"""

"""
    4 ways to read out of a file
    
    1) read method
        read() reads the entire file and gives you a single string

    2) readlines method
        readlines will read the entire file and then it will give you
        a list of lines
        
    3) readline (no s) method
        reads a single line at a time, returns it to you as a string
            remember it also doesn't get rid of the endlines
    4) use a for loop (also readline but you don't have to call it)
    
"""
my_file = open('test.txt')
print(my_file.read())
print('Reading again')
my_file.seek(35)
print(my_file.read()) #  nothing comes out
my_file.close()

print('using readlines')
my_file = open('test.txt', 'r')
the_lines = my_file.readlines()
for code_lang in the_lines:
    # always think about the endline that gets left on the end of lines
    if code_lang.strip() == 'Python':
        print('We found python')
print(the_lines)

print('here is the next line', my_file.readline())
my_file.close()

my_file = open('test.txt', 'r')

my_string = my_file.readline()
keep_going = 'yes'
while my_string and keep_going in ['y', 'yes']:
    print(my_string)
    my_string = my_file.readline()
    keep_going = input('Keep going? ')

my_file.close()
"""
    readline is good because it only takes one line at a time
    if you're reading in some large data file with line breaks then
    this might be the function for you
"""




"""
Things that evaluate to False:

    strings => empty string
        every other string is true
    int/floats => 0
        every other number evalautes to True
    bools => False is False
        True is True
    
    None evaluates to false
    empty lists and empty dictionaries
    [], {}
"""

if not 0:
    print('zero is not true')

if None:
    print('none is true')
else:
    print('none is false')
    
if []:
    print('The list is true')
else:
    print('The list is false')

if {}:
    print('This dictionary is true')
else:
    print('This dictionary is False')


x = 17
if not(x % 2):  # x % 2 == 0
    print('x is even')

if x % 2:
    print('x is odd')

print('Using a for loop now: ')
my_file = open('test.txt')
for the_line in my_file:
    print(the_line.strip())
    
my_file.close()

"""
HUGE WARNING: open a file in write mode and it will delete the file's
    contents.
"""
if input('Do you want to write using write()?') == 'yes':
    the_write_file = open('write_test2.text', 'w')
    
    in_string = input(">> ")
    while in_string:
        the_write_file.write(in_string + "\n")
        in_string = input(">> ")
    
    the_write_file.close()
    
if input('Do you want to WRITE to the movie file? ') == 'yes':
    with open('movies.txt', 'w') as movie_file:
        the_lines = []
        in_string = input(">> ")
        while in_string:
            the_lines.append(in_string + '\n')
            in_string = input(">> ")
    
        # still no added endlines you have to put them on yourself
        movie_file.writelines(the_lines)
    
        # with will run close for you

if input('Do you want to append to the movie file? ') == 'yes':
    with open('movies.txt', 'a') as movie_file:
        the_lines = []
        in_string = input(">> ")
        while in_string:
            the_lines.append(in_string + '\n')
            in_string = input(">> ")
        
        # still no added endlines you have to put them on yourself
        movie_file.writelines(the_lines)
        
        # with will run close for you
