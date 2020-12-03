'''CS5001 Spring2020
   Project -- driver
   Xue Wu
'''
from game_class import Gameboard
from function import *

def main():
    # Prompt user: gameboard column and row
    column, row, mode = start_msg()

    # Set up gameboad before play 
    setup = Gameboard(column, row, initial_board(column, row), mode)
    setup.game_prepare()

    # Play game
    if setup.mode == 1:
        setup.game_start_mode_1()
    else:
        setup.game_start_mode_2()

            
main()

