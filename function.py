'''CS5001 Spring2020
   Xue Wu 
   Project
   Function
'''
import turtle
import math
import random
from game_class import *
from score_class import *

RADIUS = 3
GAP = 0.5
UNIT = 10

def start_msg():
    '''Function: start_msg
       Parameters： none
       Return: column, row and game mode (all int)
       Prompt the user to choose gameboard col, row and game mode
    '''
    
    print('Welcome to Connect Four! Before we start,'
          ' Let us setup the gameboard\n')
    flag = True
    while flag == True:
        gameboard = int(input('The default size is 6x7\n\t...1 - Default'
                              '\n\t...2 - Customize\n'
                              'Please make your selection:\n'))
        if gameboard == 1:
            column = 7
            row = 6
            flag = False
            
        elif gameboard == 2:
            column = int(input('Please input the number of columns:\n'
                               'Reasonable column range: 4-7\n'))
            while column > 8 or column < 4:
                column = int(input('Reasonable column range: 4-7\n'))
                
            row = int(input('Please input the number of rows:\n'
                            'Reasonable row range: 4-7\n'))
            while row > 8 or row < 4:
                row = int(input('Reasonable row range: 4-7\n'))
            flag = False

        else:
            print('Invalid entry')
            
    while flag == False:
        mode = int(input('Please select mode:\n\t...1 - Computer VS User\n'
                         '\t...2 - User1 VS User2\n'))
        if mode == 1 or mode == 2:
            return column, row, mode


def initial_board(column, row):
    '''Function: initial_board
       Parameters: column, row -- int
       Return: board -- list
    '''
    # Initial a gameboard list, begin with 0
    # Use to record player's each step,
    # Use to determine 4-piece streak or not
    board = []
    for i in range(row):
        board.append([])
        for j in range(column):
            board[i].append(0)
    
    return board


'''
below this part are turtle graph functions
'''


def board_bg(width, length):
    '''Function: board_bg
       Parameters: board width & length -- float
       Return: graph -- gameboard
    '''
    # Turtle: Board background color 
    bg = turtle.Turtle()
    bg.shape('square')
    bg.turtlesize(width, length)
    bg.color('teal')
   
def draw_circle(x, y, width, length):
    '''Function: draw_circle 
       Parameters: x, y, board width & length -- float
       Return: graph -- gameboard initail white circle 
    '''
   
    circle = turtle.Turtle()
    # Turtle: draw white circle in the gameboard
    circle.hideturtle()
    for b in range(y, int(width * UNIT),\
                   int((GAP + RADIUS) * UNIT * 2)):
        for a in range(x, int(length * UNIT), \
                       int((GAP + RADIUS) * UNIT * 2)):
            # Draw from left corner
            circle.penup()
            circle.goto(a, b)
            circle.pendown()
            circle.dot(RADIUS * 2 * UNIT, 'white')

def triangle(x, y, width, column):
    '''Function: triangle
       Parameters: x, y, board width & length -- float
       Return: graph -- press bottom on the top of the board
    '''
    
    # Turtle: Draw triangles 
    for i in range(0, column):
        triangle = turtle.Turtle()
        triangle.penup()
        triangle.pencolor('white')
        triangle.shape('triangle')
        triangle.goto(x + i * (GAP + RADIUS) * UNIT * 2, y + UNIT * 2 * width)
        triangle.pendown()
        triangle.setheading(30)

def top_text(width, player):
    '''Function: top_text
       Parameters: board width -- float
                   player -- str
       Return: graph -- toptext 
    '''
    score = Score()
    toptext = turtle.Turtle()
    # Turtle: Display the total number of games won by red and by yellow
    toptext.hideturtle()
    toptext.penup()
    toptext.pencolor('white')
    toptext.goto(-1 * RADIUS * UNIT * 3, width * UNIT + UNIT * 5)
    toptext.pendown()
    toptext.write('RED: '+ score.initialize_score(player),\
                        font=("Arial", 15, "bold"))
    toptext.penup()
    toptext.forward(100)
    toptext.pendown()
    player = 'YELLOW'
    toptext.write('YELLOW: '+ score.initialize_score(player),\
                        font=("Arial", 15, "bold"))
        
def playerturn_display(playerturn, player, x):
    '''Function: playerturn_display
       Parameters: playerturn -- Turtle func
                   player -- str
                   x -- float 
       Return: graph -- player turn
    '''
    # Clear previous text
    playerturn.clear()
    # Turtle: update playerturn on the left of the board 
    playerturn.penup()
    playerturn.goto(x - 150, 30)
    playerturn.pendown()
    playerturn.pencolor('white')
    playerturn.write(player + "'s TURN!",\
                          align="center", font=("Arial", 15, "bold"))
    if player == 'RED':
        playerturn.shape("red.gif")
    else:
        playerturn.shape('yellow.gif')
    playerturn.penup()
    playerturn.goto(x - 150, 0)
    playerturn.stamp()

def pop_button(x, y):
    '''Function: pop_button
       Parameters: x, y -- float
       Return: graph -- pop out button
    '''
    # Turtle: shown on the left of the board
    pop = turtle.Turtle()
    pop.hideturtle()
    pop.penup()
    pop.goto(x - 150, 130)
    pop.pendown()
    pop.pencolor('white')
    pop.write('POP OUT', align="center", font=("Arial", 15, "bold"))
    pop.penup()
    pop.goto(x - 150, 90)
    pop.showturtle()
    pop.pendown
    pop.shape('square')
    pop.turtlesize(3)
    pop.color('lawn green')


def update_movement(update_chess, x, y, count_chess, index, player):
    '''Function: update_movement
       Parameters: update_chess -- Turtle func
                   x, y -- float
                   count_chess -- dic
                   index -- int
                   player -- str
       Return: graph -- text showed on the final page  
    '''
    # Turtle: Update selected circle on the screen board
    update_chess.penup()
    update_chess.goto(x + (GAP + RADIUS) * UNIT * 2 * index, \
                  y + count_chess[index] * (GAP + RADIUS) * UNIT * 2)
    update_chess.pendown()
    if player == 'RED':
        update_chess.shape("red.gif")
        update_chess.stamp()
    elif player == 'YELLOW':
        update_chess.shape('yellow.gif')
        update_chess.stamp()
    else:# pop out 
        update_chess.dot(RADIUS * 2 * UNIT, 'white')
    
def win_text(player, screen, mode):
    '''Function: win_text
       Parameters: player -- str
                   screen -- Turtle func
                   mode -- int
       Return: graph -- text showed on the final page  
    '''
    wintext = turtle.Turtle()
    wintext.hideturtle()
    screen.clearscreen()
    wintext.penup()
    wintext.goto(0,0)
    wintext.pendown()
    if player == 'RED':
        screen.bgcolor('crimson')
        if mode == 1:# Computer vs Human
            wintext.write('Computer win. You lose.', font=("Arial", 40, "bold"))
        else: #Human1
            wintext.write('Player1 win. Congrats!', font=("Arial", 40, "bold"))
            
    elif player == 'YELLOW':
        screen.bgcolor('gold')
        if mode == 1:# Computer vs Human
            wintext.write('You win!! Congrats!', font=("Arial", 40, "bold"))
        else: # Human vs Human
            wintext.write('Player2 win. Congrats!', font=("Arial", 40, "bold"))
            
    else:# nobody win
        screen.bgcolor('light steel blue')
        wintext.write('Game Over',\
                       font=("Arial", 40, "bold"))

