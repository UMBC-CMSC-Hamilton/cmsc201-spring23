def binary_to_decimal(my_binary):
    """
        1001101
    """
    result = 0
    place = 1
    for i in range(len(my_binary) - 1, -1, -1):
        if my_binary[i] == '1':
            result += place
        place *= 2
    
    return result


def decimal_to_binary(number):
    """
        ask even or odd?
        int divide by 2
    
        100010011001
        we're going to have to store this as a string
    """
    result = ''
    if number == 0:
        return '0b0'
    while number != 0:
        # if it's even you put a zero on the front, else a 1, divide by 2
        if number % 2 == 0:
            result = '0' + result
        else:
            result = '1' + result
        number //= 2
    
    result = '0b' + result
    return result


num = int(input('Enter a number to convert into binary'))
while num != -1:
    print(decimal_to_binary(num), bin(num))
    num = int(input('Enter a number to convert into binary'))

"""
what is hex?  hexadecimal = base 16
    extremely related to binary, binary is base 2, hex is base 2^4 = 16

    what are hexadecimal digits?
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A=10, B=11, C=12, D=13, E=14, F=15
        
        dec bin hex     dec bin  hex    dec bin hex     dec bin hex
        0 0000  0       4   0100 4      8   1000 8      12 1100 C
        1 0001  1       5   0101 5      9   1001 9      13 1101 D
        2 0010  2       6   0110 6      10  1010 A      14 1110 E
        3 0011  3       7   0111 7      11  1011 B      15 1111 F
       11
        11
        01
       100
       
       0110 0111 1001 1100 1111 -> hex 679CF (obviously hex because dec doesn't have C F)
       00011001 -> 1100 1 <- not this instead do 1 1001 <- this one4
       0001 1001 -> 0x19
       1 + 8 + 16 = 25dec
        A23 this is pretty easy to see that it's hex because it has an A
        1234 (hex)
       
        Add zeros up front then split into blocks of 4
        
       
       50 -> 050
       other way 50 -> 500
       
       How to distinguish:
            (hex) (dec) (bin)
            101 (hex)
        0x(the hex number)
        0x1234                  0x101       101h
        1234                    101
        0b110110101010010       0b101       101b
        
    56A2 -> 0101 0110 1010 0010

        dec bin hex     dec bin  hex    dec bin hex     dec bin hex
        0 0000  0       4   0100 4      8   1000 8      12 1100 C
        1 0001  1       5   0101 5      9   1001 9      13 1101 D
        2 0010  2       6   0110 6      10  1010 A      14 1110 E
        3 0011  3       7   0111 7      11  1011 B      15 1111 F

    F35421E
    1111 0011 0101 0100 0010 0001 1110
    
   hex <-> bin <-> dec
   
   hex <-> dec
"""

num = (input('Enter a number to convert into decimal'))
while num != 'quit':
    print(binary_to_decimal(num))
    num = (input('Enter a number to convert into decimal'))

"""
    hex to decimal
    
    0x43A -> dec
    10 * 16^0 + 3 * 16^1 + 4 * 16^2
    
"""


def hex_to_decimal(my_hex):
    """
        32AF
    """
    result = 0
    place = 1
    for i in range(len(my_hex) - 1, -1, -1):
        if '0' <= my_hex[i] <= '9':
            result += int(my_hex[i]) * place
        elif my_hex[i].lower() == 'a':
            result += 10 * place
        elif my_hex[i].lower() == 'b':
            result += 11 * place
        elif my_hex[i].lower() == 'c':
            result += 12 * place
        elif my_hex[i].lower() == 'd':
            result += 13 * place
        elif my_hex[i].lower() == 'e':
            result += 14 * place
        elif my_hex[i].lower() == 'f':
            result += 15 * place
        place *= 16  # changed from 2 to 16 for hex
    
    return result


num = (input('Enter a number to convert into decimal'))
while num != 'quit':
    print(hex_to_decimal(num))
    num = (input('Enter a number to convert into decimal'))

"""
    hex -> dec
    
    32A = 3 * 16^2 + 2 * 16 + 10 * 16^0
        = 3 * 256 + 2 * 16 + 10
        = 768 + 32 + 10 = 810 dec
        
    F3C = 15 * 256 + 3 * 16 + 12
        = (10 + 5)(256) + 48 + 12
        = 2560 + 1280 + 48 + 12
        = 3840 + 60 = 3900
    
    A4, FF -> dec you see that mental math is hard
    3 hex digits is probably the max that we'd give you
        FF = 15 * 16 + 15 = 255
    dec -> hex
        same as dec into binary
        while num != 0
            ask what is num % 2 ? 0 or 1 that'll be our digit
            divide the number by 2 (int divide)

        while num != 0
            ask what is num % 16 ? 0 or 1 that'll be our digit
            divide the number by 16 (int divide)
            
    FF = 15 * 16 + 15 = 255
"""

def decimal_to_hex(the_number):
    result = ''
    
    if the_number == 0:
        return '0x0'
    
    while the_number:
        if 0 <= the_number % 16 <= 9:
            result = str(the_number % 16) + result
        elif the_number % 16 == 10:
            result = 'A' + result
        elif the_number % 16 == 11:
            result = 'B' + result
        elif the_number % 16 == 12:
            result = 'C' + result
        elif the_number % 16 == 13:
            result = 'D' + result
        elif the_number % 16 == 14:
            result = 'E' + result
        elif the_number % 16 == 15:
            result = 'F' + result

        the_number //= 16
    
    return '0x' + result


my_number = int(input('Tell me a number to convert to hex: '))
while my_number != -1:
    print(decimal_to_hex(my_number))
    my_number = int(input('Tell me a number to convert to hex: '))


def decimal_to_hex_dict(the_number):
    result = ''
    
    if the_number == 0:
        return '0x0'
    
    my_hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                   6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                   12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    while the_number:
        result = my_hex_dict[the_number % 16] + result
        the_number //= 16
    
    return '0x' + result
