"""
a file, a number
instructions, size of your ram

mov instruction
    mov [slot] value
    mov [slot] [another slot]
add instruction
    sub, mul, div, mod all of these are basically the same
    add [5] 3 [7] slot(7) + 3 => slot(5)
cmp instruction
    cmp [x] [y]
    cmp val val
    cmp [x] val
    
    cmp 5 7
jmp (all its flavors)
    je, jne, jl, jle, jg, jge, jmp (unconditional)

random.ret 10

0   mov [0] 5
1   add [0] [0] 3  # slot 0 will have value 12
2   cmp [0] 10
3   jge 6 # how does jump know if something is greater than or equal to?
4   int print "slot 0 was less than 10"
5   jmp 7
6   int print "slot 0 was not less than 10"
7   hlt
8   jmp 200
9   add [200] [100] [5]

the compare instruction asks two questions:
    1) is it equal?
    2) cmp x y is x < y?
    equal_flag = False
    less_flag = True

Check for index errors because you can accidentally plug in numbers that
    are either outside of the program or outside of the ram
    
    add [5] [0] 3
    ['add', '[5]', '[0]', '3']
    never: add [   5 ] [ 0 ] 3 (all the memory addresses will not have spaces)
    ['add', '[', not good...
        you can use split
"""

