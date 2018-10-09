'''
Tic Tac Toe game written in python.

Using tkinter GUI and OOP

Created by Jack Ackermann
'''

from tkinter import Tk, ttk, Frame, FALSE, Canvas, Label, messagebox, StringVar


class TicTacToe(Frame):
    ''' Main Class '''
    def centre_window(self):
        ''' Create Window and centre to screen '''
        w = 345
        h = 365
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def __init__(self, parent, *args, **kwargs):
        ''' Initialize widgets and variables '''
        Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.title('TicTacToe  - Created in Python')
        self.centre_window()
        self.grid(column=0, row=0, sticky='nsew',  padx=0,  pady=0)
        self.current_player = 1
        self.play_count = 0
        self.score_player1 = 0
        self.score_player2 = 0
        # Save selected coordinates chosen by players
        self.a1, self.a2, self.a3 = [], [], []
        self.b1, self.b2, self.b3 = [], [], []
        self.c1, self.c2, self.c3 = [], [], []
        # Load the screen widgets onto canvas
        self.load_widgets()

    def load_widgets(self):
        ''' All widgets go under here '''
        self.canvas = Canvas(self, width=340, height=340, background='cyan2')
        self.canvas.grid(column=0, row=0)
        # Create grid
        self.create_grid()
        # Create player turn status bar at bottom of screen
        self.player_turn = Label(self, text='Player_1 is ready', font='bold')
        self.player_turn.grid(row=1, column=0, sticky="Sw")
        # Add player score to screen
        self.p1 = StringVar()
        self.p1.set('Player1: {0}'.format(self.score_player1))
        self.score1 = Label(self, textvariable=self.p1, background='cyan2')
        self.score1.grid(row=0, column=0, sticky="sw")
        self.p2 = StringVar()
        self.p2.set('Player2: {0}'.format(self.score_player2))
        self.score2 = Label(self, textvariable=self.p2, background='cyan2')
        self.score2.grid(row=0, column=0, sticky="se")
        # Create and bind onclick events to tags of each square
        self.on_click()

    def create_grid(self):
        '''
        Setup TicTacToe grid
        x=10, y=109, x_left=327, y_bottom=109
        '''
        self.canvas.create_line(10, 109, 327, 109, fill="black", width='4')
        self.canvas.create_line(10, 220, 327, 220, fill="black", width='4')
        self.canvas.create_line(115, 10, 115, 327, fill="black", width='4')
        self.canvas.create_line(225, 10, 225, 327, fill="black", width='4')

    def player_one_turn(self, tag):
        '''
        When its players one turn, draw a big X in chosen block
        '''
        coords1 = {'A1': [30, 30, 100, 100], 'A2': [140, 30, 210, 100],
                   'A3': [250, 30, 320, 100], 'B1': [30, 130, 105, 205],
                   'B2': [140, 130, 215, 205], 'B3': [250, 130, 325, 205],
                   'C1': [30, 235, 105, 310], 'C2': [140, 235, 215, 310],
                   'C3': [250, 235, 325, 310]}
        coords2 = {'A1': [100, 30, 30, 100], 'A2': [210, 30, 140, 100],
                   'A3': [320, 30, 250, 100], 'B1': [105, 130, 30, 205],
                   'B2': [215, 130, 140, 205], 'B3': [325, 130, 250, 205],
                   'C1': [105, 235, 30, 310], 'C2': [215, 235, 140, 310],
                   'C3': [325, 235, 250, 310]}
        self.canvas.create_line(coords1[tag], fill="black", width='10')
        self.canvas.create_line(coords2[tag], fill="black", width='10')
        if (len(eval("self.{0}".format(tag.lower())))) >= 1:
            messagebox.showinfo("Invalid Choice", "That box is being used.")
        else:
            tmp = "self.{0}.append('X')".format(tag.lower())
            eval(tmp)

    def player_two_turn(self, tag):
        '''
        When its player two's turn, draw a red circle in chosen block
        '''
        coords = {'A1': [25, 25, 100, 100], 'A2': [135, 25, 210, 100],
                  'A3': [245, 25, 320, 100], 'B1': [25, 200, 100, 125],
                  'B2': [135, 200, 210, 125], 'B3': [245, 200, 320, 125],
                  'C1': [25, 235, 100, 315], 'C2': [135, 235, 210, 315],
                  'C3': [245, 235, 320, 315]}
        self.canvas.create_oval(coords[tag], fill="Red", outline="red")
        if (len(eval("self.{0}".format(tag.lower())))) >= 1:
            messagebox.showinfo("Invalid Choice", "That box is being used.")
        else:
            tmp = "self.{0}.append('O')".format(tag.lower())
            eval(tmp)

    def on_click(self):
        '''
        Create a grid of invisible square blocks to bind onclick() events too
        '''
        def clicked(event, tag):
            '''
            Player has chosen a block, check to see if it resulted in a win
            Call the function to draw a X or an O
            Change the player status to the next player
            '''
            if self.current_player == 1:
                self.player_one_turn(tag)
                self.play_count += 1
                self.check_win()
                self.current_player = 2
                self.player_turn.config(text="Player_2 is ready", font='bold')
            elif self.current_player == 2:
                self.player_two_turn(tag)
                self.play_count += 1
                self.check_win()
                self.current_player = 1
                self.player_turn.config(text="Player_1 is ready", font='bold')
            if self.play_count == 9:
                messagebox.showinfo("Game Over", "Nobody wins, it is a draw")
                self.reset_board()

        sqaure = {'a1': [10, 10, 110, 105], 'a2': [118, 10, 220, 105],
                  'a3': [230, 10, 325, 105], 'b1': [10, 115, 110, 215],
                  'b2': [118, 115, 220, 215], 'b3': [230, 115, 325, 215],
                  'c1': [10, 225, 110, 325], 'c2': [118, 225, 220, 325],
                  'c3': [230, 225, 325, 325]}

        for v in sqaure.keys():
            tag = v.upper()
            self.canvas.create_rectangle(sqaure[v], fill="cyan2", width='0',
                                         tags=tag)
            self.canvas.tag_bind(tag, "<Button-1>", lambda event,
                                 tag=tag: clicked(event, tag))

    def check_win(self):
        '''
        Check to see if a player has won.
        If a player has won, adjust the score and reset the board.
        '''
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
            tmp_str = ''.join(combo[keys])
            if tmp_str == 'XXX':
                self.score_player1 += 1
                self.p1.set('Player1: {0}'.format(self.score_player1))
                self.reset_board()
                messagebox.showinfo("Winner", "Player 1 wins this round!")
            elif tmp_str == 'OOO':
                self.score_player2 += 1
                self.p2.set('Player2: {0}'.format(self.score_player2))
                self.reset_board()
                messagebox.showinfo("Winner", "Player 2 wins this round!")

    # reset the game board
    def reset_board(self):
        '''
        Clears the board after a win or a draw
        '''
        self.canvas.delete("all")
        self.play_count = 0
        self.a1.clear()
        self.a2.clear()
        self.a3.clear()
        self.b1.clear()
        self.b2.clear()
        self.b3.clear()
        self.c1.clear()
        self.c2.clear()
        self.c3.clear()
        self.create_grid()
        self.on_click()

    # Exit the program. Linked to the Exit Button
    def onExit(self):
        '''
        Exits the program. Button not implemented
        '''
        self.root.destroy()


def main():
    ''' Main Function '''
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    # root.configure(background="black")
    TicTacToe(root)
    root.mainloop()

if __name__ == '__main__':
    main()
