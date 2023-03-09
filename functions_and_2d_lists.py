"""
    2d lists
        list of lists
    Each of the sublists has it own size
    
    

"""
def dont_run_me():
    my_list = [
        [1, 2, 5, 7],
        [2, 4],
        [6, 7, 8],
        [1, 2, 3, 4, 5, 6, 7]
    ]
    
    # length of the outer list is 4
    print(len(my_list))
    
    for i in range(len(my_list)):
        # j will only take the indices that exist in the ith inner list
        for j in range(len(my_list[i])):
            print(my_list[i][j], end=', ')
            
            # first index [i] gives us the inner list at position i
            # second index gets us the element at position j inside that list
        print()
    
    
    """
        How do I create a list of lists?
    """
    
    new_list_size = int(input('What is the size of the new list? '))
    my_new_list = []
    
    for i in range(new_list_size):
        new_sublist = []
        # populate the list
        for j in range(new_list_size):
            new_sublist.append(i ** j)
        # add it to the main list
        my_new_list.append(new_sublist)
        
    print(my_new_list)


EMPTY_SPACE = " "
CROSS = 'X'
NOUGHT = 'O'
BOARD_SIZE = 3


def display_board(the_board):
    for i in range(len(the_board) - 1):
        current_line = ' | '.join(the_board[i])
        print(current_line)
        print("-" * len(current_line))

    print(' | '.join(the_board[len(the_board) - 1]))


def board_filled(the_board):
    for i in range(len(the_board)):
        for j in range(len(the_board)):
            if the_board[i][j] == EMPTY_SPACE:
                return False
            
    return True

def game_loop():
    the_board = make_board()
    current_player = [CROSS, NOUGHT]
    turn = 0
    
    while detect_victory(the_board) == EMPTY_SPACE and not board_filled(the_board):
        display_board(the_board)
        the_move = get_move(the_board)
        x = the_move[0]
        y = the_move[1]
        the_board[x][y] = current_player[turn % 2]
        turn += 1
    
    display_board(the_board)
    print('The winner was', detect_victory(the_board))


def get_move(the_board):
    the_move = input('Enter the coordinate of your move: ')
    # format is going to be something like 1 2 or 2 3 or 3 1
    while True:
        split_move = the_move.split()
        if len(split_move) == 2:
            x = int(split_move[0])
            y = int(split_move[1])
            
            if 1 <= x <= 3 and 1 <= y <= 3:
                if the_board[x - 1][y - 1] == EMPTY_SPACE:
                    return [x - 1, y - 1]
                else:
                    print('That space is filled. ')
            else:
                print('You entered coordinates that were out of bounds. Both must be between 1 and 3.')
        else:
            print('You should enter two numbers between 1 and 3.')

        the_move = input('Enter the coordinate of your move: ')


def make_board():
    tic_tac_toe = []
    for i in range(BOARD_SIZE):
        new_row = []
        for j in range(BOARD_SIZE):
            new_row.append(EMPTY_SPACE)
        tic_tac_toe.append(new_row)
        
    return tic_tac_toe


def detect_victory(the_board):
    """
    Detects row victories
    """
    for i in range(len(the_board)):  # for each row
        winner = the_board[i][0]  # first index of the row
        for j in range(1, len(the_board[i])):  # each column
            if winner != the_board[i][j]:
                winner = EMPTY_SPACE
        if winner != EMPTY_SPACE:
            return winner

    """
    Detects column victories
    """
    for i in range(len(the_board)):  # for each row
        winner = the_board[0][i]  # first index of the row
        for j in range(1, len(the_board[i])):  # each column
            if winner != the_board[j][i]:
                winner = EMPTY_SPACE
        if winner != EMPTY_SPACE:
            return winner
        
    diag_winner = the_board[0][0]
    anti_diag_winner = the_board[0][2]
    # BOARD_SIZE - 1 - i construction
    for i in range(len(the_board)):  # assume we're on a square
        if the_board[i][i] != diag_winner:
            diag_winner = EMPTY_SPACE
        if the_board[i][BOARD_SIZE - 1 - i] != anti_diag_winner:
            anti_diag_winner = EMPTY_SPACE
        
    if diag_winner != EMPTY_SPACE:
        return diag_winner
    if anti_diag_winner != EMPTY_SPACE:
        return anti_diag_winner
    
    return EMPTY_SPACE


if __name__ == '__main__':
    game_loop()
