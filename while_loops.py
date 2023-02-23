"""
a while loop is the 'other type of loop'

    a for loop iterates over a list, or a range, or some object that has
        next lines (files) etc, strings (give character by character)
    
    a while loop is an if statement on repeat
"""
if False:
    i = 0
    while i <= 10:
        print(i)  # becomes 20 lines of code...
        # forget about this i += 1, accidentally change code and delete it
        # immediately you have infinite loop
        #
        i += 1  # what happens if we don't include this?
    
    # if you loop around in a while loop forever we call that an infinite loop
    
    for i in range(11):
        print(i)
    
    """
        either you have some process that you want to keep it going:
            graphical windows, internet servers, a game
            
            loop until you get the windows quit message
                WM_DESTROY
            
            while True - web services
            
            while not checkmate:
            
        user input validation
            get the user to input new data until they do what you want
    """
    
    value = int(input('Enter a number between 1 and 10: '))
    while not (1 <= value <= 10):
        value = int(input('Sorry, that was not between 1 and 10, try again: '))
    
    print(f'Yay you entered a correct value of {value}')
    
    """
        Food list
        want to create the list until someone enters quit
    """
    
    # the code that you don't want to repeat, but you need to do before
    # you get into the loop
    food_list = []
    
    # priming the input
    food = input('Tell me a food: ')
    while food != 'quit':
        food_list.append(food)
        food = input('Tell me a food: ')
    # input -> check -> add
    
    print(food_list)
    
    """
        Weird little example
    """
    p = 0
    current = 1
    # discrete logarithm of a number
    the_number = int(input('Tell me a number: '))
    while current < the_number:
        current *= 2  # current = current * 2
        print('current is', current)
        p += 1
    
    print(the_number, current, p)
    # rounds up the log
    
    # if you know how many times you need to repeat, use for
    #       it's ok if you "know the answer" by taking len(a_list)
    # if you don't know, then probably while loops
    #
    my_list = [1, 2, 3, 4, 3, 2, 5, 7, 3, 5]
    
    for x in my_list:
        if x % 2 == 1:
            print(x)
    
    index = 0
    while index < len(my_list):
        if my_list[index] % 2 == 1:
            print(my_list[index])
        index += 1
    
    username = 'eric8'
    password = 'secretpw1'
    
    entered_user = input('What is your username: ')
    entered_pw = input('What is your password: ')
    
    """
        Aside:
        
        X and Y (want this to be true)
        
        while not(X and Y):
        while not(username == entered_user and password == entered_pw):
        
        DeMorgan's Law
        not (X and Y) == not X or not Y
        not (X or Y) == not X and not Y
    """
    attempts = 1
    while (username != entered_user or password != entered_pw) and attempts < 5:
        print('Sorry one of your identifiers was not correct. ')
        entered_user = input('What is your username: ')
        entered_pw = input('What is your password: ')
        attempts += 1


"""
    list remove - say you want to remove an element out of a list
        
        by index
            use delete keyword called del
            
        by the element's value
            .remove()
"""
sample_list = ['a', 'b', 'c', 'd', 'e', 'f']
del sample_list[3]
print(sample_list)

del sample_list[0]
# del sample_list[17] index errors will happen if you go out of bounds
print(sample_list)


"""
    list.remove(element) not index
"""

another_sample = [1, 2, 7, 9, 2, 5, 7, 2]
another_sample.remove(2)
print(another_sample)

remove_element = int(input('Give me an element to remove: '))
if remove_element in another_sample:
    another_sample.remove(remove_element)

print(another_sample)

while 2 in another_sample:
    another_sample.remove(2)
    
print(another_sample)
