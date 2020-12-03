'''CS5001 Spring2020
   Xue Wu 
   Project
   Class -- Gameboard
'''
import turtle
import math
import random
from function import *
from score_class import *

RADIUS = 3
GAP = 0.5
UNIT = 10

class Gameboard:

    def __init__(self, column, row, board, mode):

        # Gameboard column & row & length & width
        self.column = column
        self.row = row
        self.board = board
        self.length = RADIUS * self.column + (self.column + 1) * GAP
        self.width = RADIUS * self.row + (self.row + 1) * GAP
        
        # Bottom left corner circle: (x, y)
        # Draw the board start from bottom left corner 
        self.x = int(-1 * self.length * UNIT + (RADIUS + 2 * GAP) * 10)
        self.y = int(-1 * self.width * UNIT + (RADIUS + 2 * GAP) * 10)

        # Default computer(red) go first 
        self.player = 'RED'
        
        # Remember the number of chess for each column
        # Use to determine valid action 
        self.count_chess = {}

        # Player scorefile (initial/update)
        self.score = Score()

        # Pop_out
        self.popout = 0

        # game mode
        # mode1: Computer VS Human
        # mode2: Human VS Human
        self.mode = mode
        
        # Turtle 1: playerturn
        # Change every time when play the chess 
        self.playerturn = turtle.Turtle()
        self.playerturn.hideturtle()
        
        # Turtle 2: screen
        # Add 2 shapes instead of built-in circles (extra point part)
        # Set up background pic
        self.screen = turtle.Screen()
        self.screen.addshape("red.gif")
        self.screen.addshape('yellow.gif')
        self.screen.bgpic('bg.gif')
        
        # Turtle 3: update_chess 
        # Update chess position on the screen 
        self.update_chess = turtle.Turtle()
        self.update_chess.hideturtle()
        
    def count_list(self):
        '''Name: count_list (dictionary)
           To remember the number of chesses played in each column
           Use to determine valid action or not
           Initial = 0 
        '''
        for char in range(self.column):
            self.count_chess[char] = 0
        
    def game_prepare(self):
        '''Name: game_prepare
           Processing method: contain several functions
           Appear initial info on the screen before the game
        '''
        # Turtle: Draw gameboard
        board_bg(self.width, self.length)
        # Turtle: Draw white circle
        draw_circle(self.x, self.y, self.width, self.length)
        # Turtle: Draw n (=column) triangles
        triangle(self.x, self.y, self.width, self.column)
        # Turtle: Show current total score for each player 
        top_text(self.width, self.player)
        # Turtle: Display current player turn
        playerturn_display(self.playerturn, self.player, self.x)
        # Turtle: Display pop_out button option 
        pop_button(self.x, self.y)
        # Initial count_list 
        self.count_list()

    def update_on_lst(self, index):
        '''Name: update_on_lst
           Index -- the column being chosen by player
           Update chosen chess on the board list in order to
           see if 4-streaks happen or not 
        '''
        curr_row = self.count_chess[index]
        self.board[curr_row][index] = self.player

    def player_turns(self):
        '''Name: player_turns
           Change player method
        '''
        if self.player == 'YELLOW':
            self.player = 'RED'
        else:
            self.player = 'YELLOW'
            

    def one_round(self, index):
        '''Name: one_round
           Index -- the column being chosen by player
           Include one_round play essential steps
           Sound: play sound each time the piece change (extra points part)
                   need to install 2 packages by pip3 before running.
                    1. pip3 install playsound
                    2. pip3 install -U PyObjC
        '''
        # Update chess on the board list
        self.update_on_lst(index)
        # Show chess movement on the screen, play sound
        self.sound()
        update_movement(self.update_chess, self.x, self.y, \
                                self.count_chess, index, self.player)
        # Update count_chess dictionary 
        self.count_chess[index] += 1
        
        # If game is over, show final page
        # If not, change player and continue 
        if not self.is_game_over():
            self.player_turns()
            playerturn_display(self.playerturn, self.player, self.x)
            if self.mode == 1:
                self.game_start_mode_1()
            else:
                self.game_start_mode_2()

    def click(self, x, y):
        '''Name: click
           User method
           -- To determin user purpose through coordinate (x,y)
           -- User have an option to choose pop_out variation, which means
               they can use their turn to remove one of their opponent's
               pieces from the top of that column instead of adding a piece of
               their own. (extra point part)
           -- If they fail to choose a valid column, game will automatically
               change player turn, and computer will move forward.
           -- If user wishes to use pop_out option, simply first click the pop
               bottom, then click the triangle (to show which column they wish
               to remove).
        '''
        # Pop out area
        # User choose to remove one instead of adding one
        if x > self.x - 150 - RADIUS * UNIT and x < self.x - 150 + RADIUS * UNIT\
           and y > 58 and y < 118:
            # Do pop_out
            self.popout = 1
            # Click a triangle(column)
            self.screen.onclick(self.click)

        # Triangle area
        # Find out the index(chosen column)
        elif y < self.y + UNIT * 2 * self.width + UNIT * 2 and \
             y > self.y + UNIT * 2 * self.width - UNIT * 2:
            
            index = math.ceil((x - self.x - RADIUS * UNIT)/\
                              ((RADIUS + GAP) * 2 * UNIT))
            # Not pop_out: if the selected column is not full, do one_round
            # If selected column is full, program does nothing. 
            if self.popout == 0:
                if self.count_chess[index] < self.row:
                    self.one_round(index)
            # Pop_out, do pop_out 
            else:
                self.pop_out(index)
    
    def game_start_mode_1(self):
        '''Name: game_start_mode_1
           Computer VS Human
           Computer: random choose a column and do one_rond
           User: using turtle click function to make a choice
        '''
        # Computer VS User
        # Computer = 'RED'
        if self.player == 'RED':
            self.screen.onclick(None)
            while True:
                # Selected a column randomly
                # If it's valid choice, do one_round; else, choose again
                index = random.randint(0, self.column-1)
                if self.count_chess[index] < self.row:
                    self.one_round(index)
                    break
            
        # User = 'YELLOW'
        else: 
            self.screen.onclick(self.click)

    def game_start_mode_2(self):
        '''Name: game_start_mode_2
           User1 VS User2 (two human players)
        '''
        # Two human players
        # Red for user1, Yellow for user2
        self.screen.onclick(self.click)


    def is_full(self):
        '''Name: is_full
           Determin whether gameboard is full or not
           Sum up the values of count_chess dictionary 
        '''
        sum = 0
        for i in range(0, self.column):
            sum += self.count_chess[i]
        return sum == self.row * self.column

    def is_streak(self):
        '''Name: is_streak
           4 ways to achieve 4-piece streak
        '''
        # 4-piece streak in a row
        for i in range(len(self.board)):
            for j in range(self.column-3): # range(4)
                if self.board[i][j] == self.player and \
                   self.board[i][j+1] == self.player and\
                   self.board[i][j+2] == self.player and\
                   self.board[i][j+3] == self.player:
                    return True    

        # 4-piece streak in a column
        for i in range(3, self.row): # range(3,6)
            for j in range(self.column):
                if self.board[i][j] == self.player and\
                   self.board[i-1][j] == self.player and\
                   self.board[i-2][j] == self.player and\
                   self.board[i-3][j] == self.player:
                    return True

        # 4-piece streak in a positive diagonal
        for i in range(3, self.row): # range(3,6)
            for j in range(self.column-3): #range(0,4)
                if self.board[i][j] == self.player and\
                   self.board[i-1][j+1] == self.player and\
                   self.board[i-2][j+2] == self.player and\
                   self.board[i-3][j+3] == self.player:
                    return True
                   
        # 4-piece streak in a negative diagonal
        for i in range(self.row - 3): # range(0,3)
            for j in range(self.column - 3): #range(0,3)
                if self.board[i][j] == self.player and\
                   self.board[i+1][j+1] == self.player and\
                   self.board[i+2][j+2] == self.player and\
                   self.board[i+3][j+3] == self.player:
                    return True

    def is_game_over(self):
        '''Name: is_game_over
           Game over in two ways:
               1. 4-piece streak (always in first place consideration)
               2. Gameboard is full, nobody win 
        '''
        # 4-piece streak
        if self.is_streak():
            # Update player's scorefile
            self.score.updated_score(self.player)
            # Show win msg on the screen 
            win_text(self.player, self.screen, self.mode)
            return True
           
        # Gameboard full or Not game over
        else:
            # Gameboard full
            if self.is_full():
                # Show game over on the screen
                win_text('no body', self.screen, self.mode)
                return True
        
    def pop_out(self, index):
        '''Name: pop_out (extra points part)
           Index -- the column being chosen by player
           Purpose -- remove a red chess from the index column
                      Remove -- if the top chess is red
                      Not remove -- if the top chess is not red,
                                    change player to next round           
        '''
        # Find out pop_out row from dictionary 
        row = self.count_chess[index] - 1
        
        # Do remove if top chess is red, valid choice
        if self.board[row][index] != self.player and row >= 0:
            # Update Board lst: back to 0
            self.board[row][index] == 0
            # Update cout_chess dictionary: count - 1
            self.count_chess[index] -= 1
            # Update on screen 
            player = 'none'
            update_movement(self.update_chess, self.x, self.y, \
                             self.count_chess, index, player)

        # If not valid choice, move to reset part
        # Reset popout flag, change player turn, do next round 
        self.popout = 0
        self.player_turns()
        playerturn_display(self.playerturn, self.player, self.x)
        if self.mode == 1:
            self.game_start_mode_1()
        else:
            self.game_start_mode_2()
            

    def sound(self):
        '''Name: sound (extra point part)
           Add sound to the game when playing chess
        '''
        # Install 2 package by pip3 before running this method
        # pip3 install playsound
        # pip3 install -U PyObjC
        try:
            from playsound import playsound
            playsound('sound.mp3')
        except:
            # Pass this method if not install
            pass
        
