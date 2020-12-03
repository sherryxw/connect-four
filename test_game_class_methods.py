'''
    CS5001 Spring2020
    Xue Wu
    Project
    Test code -- game_class methods
    This file contains testable game_class methods.
    Other non-testable methods will use other ways to test.
    Please refer to design.txt

    Please ignore the pop-out window, it's made by Turtle functions.
'''
from game_class import *

def test_count_lst():
    '''Function: test_count_lst
       Parameters: none
       Return: number of test that failed
    '''
    # Test case 
    game1 = Gameboard(0, 0, [], 1)
    game2 = Gameboard(0, 1, [[]], 1)
    game3 = Gameboard(1, 1, [[0]], 1)
    game4 = Gameboard(2, 3, [[0,0],[0,0], [0,0]], 1)
    game5 = Gameboard(5, 4, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]], 1)
    game6 = Gameboard(3, 3, [[0,0,0],[0,0,0],[0,0,0]], 1)

    fail = 0
    game1.count_list()
    game2.count_list()
    game3.count_list()
    game4.count_list()
    game5.count_list()
    game6.count_list()
    
    if game1.count_chess != {}:
        fail += 1
    if game2.count_chess != {}:
        fail += 1
    if game3.count_chess != {0:0}:
        fail += 1
    if game4.count_chess != {0:0, 1:0}:
        fail += 1
    if game5.count_chess != {0:0, 1:0, 2:0, 3:0, 4:0}:
        fail += 1
    if game6.count_chess != {0:0, 1:0, 2:0}:
        fail += 1

    return fail
    
def test_update_on_lst():
    '''Function: test_update_on_lst
       Parameters: none
       Return: number of test that failed
    '''
    fail = 0
    # Test case
    game1 = Gameboard(4, 4, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], 1)
    game2 = Gameboard(5, 4, [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0],\
                             [0,0,0,0,0]], 1)
    game3 = Gameboard(3, 3, [[0,0,0], [0,0,0], [0,0,0]], 1)

    game1.count_chess = {0:0, 1:1, 2:1, 3:3}
    game2.count_chess = {0:2, 1:2, 2:0, 3:0, 4:0}
    game3.count_chess = {0:2, 1:2, 2:2}
    
    game1.update_on_lst(0)
    game2.update_on_lst(1)
    game3.update_on_lst(2)
    if game1.board != [['RED', 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], \
                       [0, 0, 0, 0]]:
        fail += 1
    if game2.board != [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 'RED', 0, 0, 0],\
                       [0, 0, 0, 0, 0]]:
        fail += 1
    if game3.board != [[0, 0, 0], [0, 0, 0], [0, 0, 'RED']]:
        fail += 1

    return fail

def test_player_turns():
    '''Function: test_player_turns
       Parameters: none
       Return: number of test that failed
    '''
    # Test case 
    game1 = Gameboard(0, 0, [], 2)
    game2 = Gameboard(0, 1, [[]], 2)
    game3 = Gameboard(1, 1, [[0]], 2)
    game4 = Gameboard(2, 3, [[0,0],[0,0], [0,0]], 2)
    game5 = Gameboard(5, 4, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]], 2)
    game6 = Gameboard(3, 3, [[0,0,0],[0,0,0],[0,0,0]], 2)
    
    fail = 0
    # Default player = 'RED'
    game1.player_turns()
    game2.player_turns()
    game3.player_turns()
    game4.player_turns()
    game5.player_turns()
    game6.player_turns()
    
    if game1.player != 'YELLOW':
        fail += 1
    if game2.player != 'YELLOW':
        fail += 1
    if game3.player != 'YELLOW':
        fail += 1
    if game4.player != 'YELLOW':
        fail += 1
    if game5.player != 'YELLOW':
        fail += 1
    if game6.player != 'YELLOW':
        fail += 1

    return fail

def test_is_full():
    '''Function: test_is_full
       Parameters: none
       Return: boolean results
    '''
    fail = 0
    # Test case  
    game1 = Gameboard(0, 0, [], 1)
    game2 = Gameboard(0, 1, [[]], 1)
    game3 = Gameboard(1, 1, [[0]], 1)
    game4 = Gameboard(2, 3, [[0,0],[0,0], [0,0]], 1)
    game5 = Gameboard(5, 4, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],\
                             [0,0,0,0,0]], 1)
    game6 = Gameboard(3, 3, [[0,0,0],[0,0,0],[0,0,0]], 1)
    
    game1.count_chess = {}
    game2.count_chess = {}
    game3.count_chess = {0:1}
    game4.count_chess = {0:3, 1:3, 2:3}
    game5.count_chess = {0:4, 1:4, 2:4, 3:4, 4:4}
    game6.count_chess = {0:3, 1:3, 2:3}

    if game1.is_full() != True:
        fail += 1
    if game2.is_full() != True:
        fail += 1
    if game3.is_full() != True:
        fail += 1
    if game4.is_full() != True:
        fail += 1
    if game5.is_full() != True:
        fail += 1
    if game6.is_full() != True:
        fail += 1
    
    return fail
    
def test_is_streak():
    '''Function: test_is_streak
       Parameters: none
       Return: boolean results
    '''
    fail = 0
    # Test case 
    game1 = Gameboard(0, 0, [], 2)
    game2 = Gameboard(1, 1, [['RED']], 2)
    game3 = Gameboard(4, 4, [['RED','RED','RED','RED'],\
                             [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 2)
    game4 = Gameboard(5, 4, [['RED', 0, 0, 0, 0], ['RED', 0, 0, 0, 0],\
                             ['RED', 0, 0, 0, 0], ['RED', 0, 0, 0, 0]], 2)
    game5 = Gameboard(4, 5, [['RED', 0, 0, 0], [0, 'RED', 0, 0],\
                             [0, 0, 'RED', 0], [0, 0, 0, 'RED'],\
                             [0, 0, 0, 0]], 2)
    game6 = Gameboard(6, 6, [[0, 0, 0, 0, 0, 'RED'], [0, 0, 0, 0, 'RED', 0],\
                             [0, 0, 0, 'RED', 0, 0], [0, 0, 'RED', 0, 0, 0, ],\
                             [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], 2)
    
    if game1.is_streak() == True:
        fail += 1
    if game2.is_streak() == True:
        fail += 1
    # 4-streak in row 
    if game3.is_streak() != True:
        fail += 1
    # 4-streak in col
    if game4.is_streak() != True:
        fail += 1
    # 4-streak positive diagonal
    if game5.is_streak() != True:
        fail += 1
    # 4-streak negative diagonal
    if game6.is_streak() != True:
        fail += 1

    return fail

    
def main():

    # Test count_list
    fail = test_count_lst()
    if fail != 0:
        print('count_list test fail')
    else:
        print('count_list test pass.')

    # Test update_on_lst
    fail = test_update_on_lst()
    if fail != 0:
        print('update_on_lst test fail')
    else:
        print('update_on_lst test pass.')
    
    # Test player_turns
    fail = test_player_turns()
    if fail != 0:
        print('player_turns test fail')
    else:
        print('plaer_turns test pass.')

    # Test is_full
    fail = test_is_full()
    if fail != 0:
        print('is_full test fail')
    else:
        print('is_full test pass.')

    # Test is_streak 
    fail = test_is_streak()
    if fail != 0:
        print('is_streak test fail')
    else:
        print('is_streak test pass.')
        
    

        
main()
