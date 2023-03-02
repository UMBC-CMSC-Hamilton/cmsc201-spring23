"""
    strip
        removes whitespace from a string, from the front and back
            not from inside of strings, doesn't look inside non-whitespace
            leading and trailing whitespace
            lstrip and rstrip
            
            "orange" vs "orange "
    split
        takes a string, splits it on whitespace
            result is that it makes a list of strings
    join
        inverse of split
        takes a list of strings and makes one string out of them
        
        separator.join(a_list_of_strings)
        ' '.join(['a', 'b', 'c'])
"""

my_string = input('Tell me a string: ')

while my_string != 'quit':
    print(my_string)
    print(my_string.strip())
    my_string = input('Tell me a string: ')

another_string = '\n\n\nhello there\t\t\t'
print(another_string, another_string.strip(), sep=";", end="")

"""
    whitespace characters are:
        \t, \n, \r, [space]
        \r = brings you back to the start of the line
"""


my_string = input('Tell me a string to split: ')

while my_string != 'quit':
    print(my_string)
    print(my_string.split())
    my_string = input('Tell me a string to split: ')
    
print("a\nb\nc\nd".split())


my_string = input('Tell me a string to join: ')

while my_string != 'quit':
    print(my_string.join(['a', 'b', 'c','d', 'e', 'f']))
    my_string = input('Tell me a string to join: ')
    
"""
    you can't just plug a list of integers into join
"""
list_of_integers = [1, 2, 6, 5, 9, 3, 5, 4]
list_of_strings = []
for x in list_of_integers:
    list_of_strings.append(str(x))
print(list_of_strings)

print(' + '.join(list_of_strings))
# be careful that the list contains actual strings rather than anything else
# print(' + '.join(list_of_integers))
