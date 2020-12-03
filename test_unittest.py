'''CS5001 Spring2020
   Xue Wu 
   Project Test Code --
   Gameboard class init & Score class & initial_board func

   Please ignore pop_out window, It's made by Turtle function. 
'''

import unittest
import os
from game_class import *
from score_class import *
from function import *

class TestGameboard(unittest.TestCase):
    
    def test_init(self):

        # Plase ignore the pop-out window when running the test code
        # It's made by Turtle functions
        game1 = Gameboard(4, 5, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],\
                                 [0,0,0,0,0]], 1)
        self.assertEqual(game1.column, 4)
        self.assertEqual(game1.row, 5)
        self.assertEqual(game1.board, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],\
                                       [0,0,0,0,0]])
        self.assertEqual(game1.length, 14.5)
        self.assertEqual(game1.width, 18)
        self.assertEqual(game1.x, -105)
        self.assertEqual(game1.y, -140)
        self.assertEqual(game1.player, 'RED')
        self.assertEqual(game1.count_chess, {})
        self.assertEqual(game1.popout, 0)
        self.assertEqual(game1.mode, 1)

        game2 = Gameboard(2, 3, [[0,0],[0,0]], 2)
        self.assertNotEqual(game2.column, 5)
        self.assertNotEqual(game2.row, 4)
        self.assertNotEqual(game2.board, [[0,0,0],[0,0]])
        self.assertNotEqual(game2.length, 10)
        self.assertNotEqual(game2.width, 15)
        self.assertNotEqual(game2.x, 0)
        self.assertNotEqual(game2.y, 0)
        self.assertNotEqual(game2.player, 'green')
        self.assertNotEqual(game2.count_chess, [])
        self.assertNotEqual(game2.popout, 2)
        self.assertNotEqual(game2.mode, 1)
        
class ScoreTest(unittest.TestCase):
    
    def test_init(self):
        s = Score()
        self.assertEqual(s.score, 0)

    def test_initialize_score(self):
        s = Score()
        # Initialize score from file with a non-
        # existent file; score goes back to zero
        if os.path.exists('test.txt'):
            os.remove('test.txt')
        s.initialize_score('test')
        self.assertEqual(s.score, 0)

    def test_updated_score(self):
        s = Score()
        # Update score from file: += 1
        with open('test.txt', 'w') as outfile:
            outfile.write('0')
        s.updated_score('test')
        self.assertEqual(s.score, 1)
        os.remove('test.txt')

        with open('test.txt', 'w') as outfile:
            outfile.write('5')
        s.updated_score('test')
        self.assertEqual(s.score, 6)
        os.remove('test.txt')

        with open('test.txt', 'w') as outfile:
            outfile.write('-1')
        s.updated_score('test')
        self.assertEqual(s.score, 0)
        os.remove('test.txt')

class TestInitialboard(unittest.TestCase):
    def test_initial_board(self):
        self.assertEqual(initial_board(0, 1), [[]])
        self.assertEqual(initial_board(0, 0), [])
        self.assertEqual(initial_board(1, 0), [])
        self.assertEqual(initial_board(1, 1), [[0]])
        self.assertEqual(initial_board(2, 2), [[0,0],[0,0]])
        self.assertEqual(initial_board(3, 1), [[0,0,0]])
        self.assertEqual(initial_board(1, 3), [[0],[0],[0]])
        self.assertEqual(initial_board(3, 3), [[0,0,0],[0,0,0],[0,0,0]])     

    
def main():
 
    unittest.main(verbosity = 3)
    
    
main()
