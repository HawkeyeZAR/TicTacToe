# Tic Tac Toe game written in python.
# This version I have tried to do by using OOP.
# Created by Jack Ackermann


class TicTacToe(object):
    '''Main Class'''
    def __init__(self):
        '''Initiate our variables'''
        self.player_turn = 1
        self.player_one_score = 0
        self.player_two_score = 0
        self.game_state = 0
        self.choices_made = []
        # Initialize the board with default values
        self.a1, self.a2, self.a3 = '.', '.', '.'
        self.b1, self.b2, self.b3 = '.', '.', '.'
        self.c1, self.c2, self.c3 = '.', '.', '.'

    def create_board(self):
        '''Print our score on screen and draw the tictactoe board'''
        p1 = self.player_one_score
        p2 = self.player_two_score
        print("Player_1 Score: {0} -- Player_2 Score: {1}\n".format(p1, p2))
        print(' {0} | {1} | {2} '.format(self.a1, self.a2, self.a3))
        print('-----|-----')
        print(' {0} | {1} | {2} '.format(self.b1, self.b2, self.b3))
        print('-----|-----')
        print(' {0} | {1} | {2} '.format(self.c1, self.c2, self.c3))
        print('\n')

    def update_board(self, coord):
        '''Updates the boards with the entered values'''
        def update_value(c):
            '''Helper function used to modify the values'''
            if coord == 'A1':
                self.a1 = c
            elif coord == 'A2':
                self.a2 = c
            elif coord == 'A3':
                self.a3 = c
            elif coord == 'B1':
                self.b1 = c
            elif coord == 'B2':
                self.b2 = c
            elif coord == 'B3':
                self.b3 = c
            elif coord == 'C1':
                self.c1 = c
            elif coord == 'C2':
                self.c2 = c
            elif coord == 'C3':
                self.c3 = c
        # update self.choices_made list with all entered data
        self.choices_made.append(coord)
        if self.player_turn == 1:
            update_value('X')
        elif self.player_turn == 2:
            update_value('O')
        # Display the updated board to the console
        self.create_board()

    def reset_board(self):
        '''Resets the board back to initial state after win or tie'''
        # Reset list containing choices made
        self.choices_made.clear()
        # Initialize the board with default values
        self.a1, self.a2, self.a3 = '.', '.', '.'
        self.b1, self.b2, self.b3 = '.', '.', '.'
        self.c1, self.c2, self.c3 = '.', '.', '.'

    def update_score(self, player):
        '''
        Update the winners score.
        '''
        if player == 1:
            self.player_one_score += 1
            self.reset_board()
        elif player == 2:
            self.player_two_score += 1
            self.reset_board()

    def check_win(self):
        '''Check to see if a player has won or if it is a draw'''
        # create strings containing all winning combonations
        combo = {'combo1': self.a1 + self.a2 + self.a3,
                 'combo2': self.b1 + self.b2 + self.b3,
                 'combo3': self.c1 + self.c2 + self.c3,
                 'combo4': self.a1 + self.b1 + self.c1,
                 'combo5': self.a2 + self.b2 + self.c2,
                 'combo6': self.a3 + self.b3 + self.c3,
                 'combo7': self.a1 + self.b2 + self.c3,
                 'combo8': self.a3 + self.b2 + self.c1}
        for keys in combo:
            if combo[keys] == 'XXX':
                print('Player 1 wins this round!')
                self.update_score(1)
            elif combo[keys] == 'OOO':
                print('Player 2 wins this round!')
                self.update_score(2)
        # Check to see if it is a draw
        if len(self.choices_made) >= 9:
            print("It's a draw! Nobody wins this round. \n")
            self.reset_board()

    def get_player_selection(self):
        '''
        Check whos turn it's to play, update variable for next players turn
        Get player input, update choices_made list with player_selection data

        if user entered E, set self.game_state = 0, to end the game
        '''
        msg = "Player_{0}, make your choice. (Ex:b1) ".format(self.player_turn)
        self.player_selection = input(msg)
        coord = self.player_selection.upper()
        # If user entered E, break the loop to exit program
        if self.player_selection.upper() == 'E':
            self.game_state = 0
            return
        if coord[0] not in 'ABC' or coord[1] not in '123' or len(coord) > 2:
            print("Invalid data entered, A1 to C3, are valid ranges")
        elif coord in self.choices_made:
            print("Already made that choice, please try a different choice.")
        else:
            if self.player_turn == 1:
                self.update_board(coord)
                self.check_win()
                self.player_turn = 2
            elif self.player_turn == 2:
                self.update_board(coord)
                self.check_win()
                self.player_turn = 1


def start_game():
    '''main function to start the game'''
    print("##-------------------------------------------##")
    print("## Welcome, the round is about to begine     ##")
    print("## Please press E, if you would like to quit ##")
    print("##-------------------------------------------##\n")
    tic = TicTacToe()
    tic.create_board()
    tic.game_state = 1
    while True:
        tic.get_player_selection()
        if tic.game_state == 0:
            print("\nUser exited the game, thanks for playing\n")
            break


if __name__ == '__main__':
    start_game()
