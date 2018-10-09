# Tic Tac Toe game written in python.
#
# Created by Jack Ackermann
#


from collections import OrderedDict

board = {'A': ['.', '.', '.'],
        'B': ['.', '.', '.'],
        'C': ['.', '.', '.']}
player_turn = 1
player_one_score = 0
player_two_score = 0
total_turns = 0


def display_board():
    '''
    Draw a TicTacToe board on the console.
    Initial board will be empty, filled with a .

    Once game has started, board with be updated with X's and O's
    '''
    r1, r2, r3 = board['A'][0], board['A'][1], board['A'][2]
    r4, r5, r6 = board['B'][0], board['B'][1], board['B'][2]
    r7, r8, r9 = board['C'][0], board['C'][1], board['C'][2]
    print('\n')
    print(' {0} # {1} # {2} '.format(r1, r2, r3))
    print('###########')
    print(' {0} # {1} # {2} '.format(r4, r5, r6))
    print('###########')
    print(' {0} # {1} # {2} '.format(r7, r8, r9))
    print('\n')


def reset_board():
    '''
    Once a new round starts, reset the board.
    '''
    global board
    board = {'A': ['.', '.', '.'],
        'B': ['.', '.', '.'],
        'C': ['.', '.', '.']}

def check_board(dic):
    '''
    Check the board for any winners
    Once there is a winner, reset the board and the lists
    If its a tie, reset the board
    '''
    column = []
    rows = []
    diagonal = []
    result = []
    # Make list of all data in vertical columns
    for i in range(3):
        tmp = ''
        for i in range(3):
            tmp += str(dic['A'][i])
            tmp += str(dic['B'][i])
            tmp += str(dic['C'][i])
    column = [tmp[i:i+3] for i in range(0, len(tmp), 3)]

    # Make list of all data in the horizontal rows
    for k in ('A', 'B', 'C'):
        tmp = ''.join(board[k])
        rows.append(tmp)

    # Make a list of the two diagonal rows
    res1 = ''.join(rows[0][0] + rows[1][1] + rows[2][2])
    res2 = ''.join(rows[0][2] + rows[1][1] + rows[2][0])
    diagonal = [res1, res2]

    # Merge all the lists and check for winner
    result = rows + column + diagonal
    global player_two_score
    global player_one_score
    for lists in result:
        if lists == 'XXX':
            player_one_score += 1
            print('\nPlayer 1 wins the game!')
            print('Player1 Score: {0}  Player2 Score: {1}\n'.format(player_one_score, player_two_score))
            reset_board()
        if lists == 'OOO':
            player_two_score += 1
            print('\nPlayer 2 wins the game!')
            print('Player1 Score: {0}  Player2 Score: {1}\n'.format(player_one_score, player_two_score))
            reset_board()
    # Check to see if its a draw
    if total_turns == 9:
        print("\nIt's a draw, nobody wins.")
        print('Player1 Score: {0}  Player2 Score: {1}\n'.format(player_one_score, player_two_score))
        reset_board()  
    column.clear()
    rows.clear()
    diagonal.clear()
    result.clear()

def update_board(coord, c):
    '''
    Updated the board with the selected coordinates from players

    Make sure that the player can't select a previously used coordinate
    '''
    x = coord[0]
    y = int(coord[1])
    v = c
    board[x][y] = v
    global total_turns
    total_turns += 1
    display_board()
    
def validate_coord(coord):
    '''
    Check that the player entered a valid coordinate string

    Must be in the format of: A,1
    max value is C2
    '''
    coord = coord.upper().split(',')
    global player_turn
    if coord[0] not in 'ABC' or coord[1] not in '012':
        print("\nInvalid Coordinates entered")
        print("Range must be from A,0 - A,2, B,0 - B,2 and C,0 - C,2")
    elif board[coord[0]][int(coord[1])] in 'XO':
        print('\nCannot use that Coordinate, already been used, please try again')
    else:
        if player_turn == 1:
            player_turn = 2
            update_board(coord, 'X')
        elif player_turn == 2:
            player_turn = 1
            update_board(coord, 'O')

def play_game():
    '''
    Creates an infinite loop to keep the game running.
    Game stops when a player enters 'E'
    '''
    print("Press E to exit")
    while True:
        coord = input("Player {0}, please enter selection, eg b,1: ".format(player_turn))
        if coord.upper() == 'E':
            break
        elif player_turn == 1:
            validate_coord(coord)   
        elif player_turn == 2:
            validate_coord(coord)
        check_board(board)

# Start the game
if __name__ == '__main__':
    play_game()
