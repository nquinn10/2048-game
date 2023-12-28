'''
CS5001
Spring 2023
2048 - GameBoard Test

This program tests the GameBoard class by importing
the class and Python unittest and generating tests
for various scenarios/game moves for each of the core 
methods.

Nicole Quinn
'''

from GameBoard import GameBoard
import unittest

class GameBoardTest(unittest.TestCase):
    '''
    The GameBoardTest class leverages Python unittest to 
    test the GameBoard class and the various methods
    that accompany it. Each method tests a method from the 
    GameBoard class by verifiying their attribute or return
    values are as expected. This includes verifying if 
    ValueErrors are raised appropriately. 
    '''

    def test_init(self):
        '''
        Constructor Test: test_init
        Test method to verify the game board instance 
        attributes are as expected and the game board 
        initialization occurs as expected. This includes raising
        errors when attribute board size is not 4 and is not an 
        int, and also when new_game is not a list and does not
        contain integer values only. This also includes testing
        the random elements to ensure the correct amount and value
        of random integers are added. 
        Parameters:
           self: the current object
        Returns: 
            Nothing
        '''
        # test to confirm input grid is the same as the one that is created 
        self.assertEqual(GameBoard(4, [[2, 2, 2, 2],
                                       [2, 4, 4, 2],
                                       [16, 16, 16, 8],
                                       [2, 2, 0, 0]]).new_game, 
                                       [[2, 2, 2, 2], 
                                        [2, 4, 4, 2],
                                        [16, 16, 16, 8],
                                        [2, 2, 0, 0]])
        # test to confirm board size is as specified 
        self.assertEqual(GameBoard(4, [[2, 2, 2, 2], 
                                       [2, 4, 4, 2], 
                                       [16, 16, 16, 8], 
                                       [2, 2, 0, 0]]).board_size, 4)
        # test to confirm len of new game is the len of board size of 4
        self.assertEqual(len(GameBoard(4, []).new_game), 4)
        # test to confirm board size of empty new game is as specified
        self.assertEqual(GameBoard(4, []).board_size, 4)
        # set up to test for randomness 
        random_num_test = GameBoard(4, []).new_game
        non_zero_count = 0
        random_num_value = []
        for row in random_num_test:
            for i in row:
                if i != 0:
                    non_zero_count += 1
                    random_num_value.append(i)
        # test to confirm that there are two non-zero elements in new game board
        self.assertEqual(non_zero_count, 2)
        # test to confirm that two random numbers generated are only 2 or 4
        self.assertTrue(random_num_value, 
                        ([2, 2] or [4, 2] or [4, 4]) in random_num_value)

        self.assertEqual(GameBoard(4, []).score, 0)
        # assuming score of this game board starts at 0
        game_board = GameBoard(4, [[4, 0, 0, 4],
                                   [0, 0, 2, 2],
                                   [0, 0, 0, 8],
                                   [0, 0, 2, 2]])
        # shift left to adjust score
        game_board.shift_left_for_testing()
        # test to make sure shift and combine equals correct score
        self.assertEqual(game_board.score, 16)
        # raise error when board size is not 4
        with self.assertRaises(ValueError):
            GameBoard(5, [[4, 0, 0, 4],
                          [0, 0, 2, 2],
                          [0, 0, 0, 8],
                          [0, 0, 2, 2]])
        # raise error when board size is not  an int
        with self.assertRaises(ValueError):
            GameBoard('t', [[4, 0, 0, 4], 
                            [0, 0, 2, 2],
                            [0, 0, 0, 8],
                            [0, 0, 2, 2]])
        # raise error when new_game is not a list
        with self.assertRaises(ValueError):
            GameBoard('t', 25)
        # raise error when new_game values are not integers
        with self.assertRaises(ValueError):
            GameBoard('t', [[4, 'l', 0, 4],
                            [0, 0, 2, 2],
                            [0, 0, 0, 8],
                            [0, 0, 2, 2]])
        # raise error when there are not 4 rows
        with self.assertRaises(ValueError):
            GameBoard(4, [[4, 0, 0, 4],
                          [0, 0, 2, 2],
                          [0, 0, 0, 8],
                          [0, 0, 2, 2],
                          [0, 0, 2, 2]])
        # raise error when rows are not 4 in length
        with self.assertRaises(ValueError):
            GameBoard(4, [[4, 0, 0, 4],
                          [0, 0, 2, 2, 0],
                          [0, 0, 0, 8],
                          [0, 0, 2, 2]])   
        

    def test_start_new_game(self):
        '''
        Method Test: test_start_new_game
        Test method to verify the start_new_game method
        functions as expected. This also includes testing
        the random elements to ensure the correct amount and value
        of random integers are added. 
        Parameters:
           self: the current object
        Returns: 
            Nothing
        '''
        # test to confirm len of new game is the len of board size of 4
        self.assertEqual(len(GameBoard(4, []).start_new_game_for_testing()), 4)
        # set up to test for randomness 
        random_num_test = GameBoard(4, []).start_new_game_for_testing()
        non_zero_count = 0
        random_num_value = []
        for row in random_num_test:
            for i in row:
                if i != 0:
                    non_zero_count += 1
                    random_num_value.append(i)
        # test to confirm that there are two non-zero elements in new game board
        self.assertEqual(non_zero_count, 2)
        # test to cofnirm that two random numbers generated are only 2 or 4
        self.assertTrue(random_num_value, 
                        ([2, 2] or [4, 2] or [4, 4]) in random_num_value)
    

    def test_game_over(self):
        '''
        Method Test: test_game_over
        Test method to verify the game_over method
        functions as expected. True means the game is over
        and False means there are valid moves left.
        Parameters:
           self: the current object
        Returns: 
            Nothing
        '''
        # 2048 in game board - game over 
        self.assertTrue(GameBoard(4, [[2, 4, 2, 4],
                                      [4, 2, 4, 2],
                                      [32, 16, 128, 8],
                                      [8, 2048, 4, 0]]).game_over())
        # no more valid combos - game over
        self.assertTrue(GameBoard(4, [[2, 4, 2, 4],
                                      [4, 2, 4, 2],
                                      [32, 16, 128, 8],
                                      [4, 1024, 2, 4]]).game_over())
        # last row, last 2 digits are equal - can be combined
        self.assertFalse(GameBoard(4, [[2, 4, 2, 4],
                                       [4, 2, 4, 2],
                                       [32, 16, 128, 8],
                                       [8, 1024, 2, 2]]).game_over())
        # first 2 rows, second digits are equal - can be combined 
        self.assertFalse(GameBoard(4, [[16, 4, 2, 4],
                                       [4, 4, 4, 2],
                                       [32, 16, 128, 8],
                                       [8, 1024, 2, 4]]).game_over())
        # last 2 rows, last digits are equal - can be combined 
        self.assertFalse(GameBoard(4, [[2, 4, 2, 4],
                                       [4, 2, 4, 2],
                                       [32, 16, 128, 2],
                                       [8, 1024, 4, 2]]).game_over())
        # no more valid combos - game over
        self.assertTrue(GameBoard(4, [[2, 4, 2, 4],
                                      [4, 2, 4, 2],
                                      [32, 16, 128, 8],
                                      [8, 1024, 4, 2]]).game_over())
        # first row, first 2 digits are equal - can be combined 
        self.assertFalse(GameBoard(4, [[4, 4, 2, 4],
                                       [16, 2, 4, 2],
                                       [32, 64, 128, 8],
                                       [8, 1024, 2, 4]]).game_over())

    def test_new_number(self):
        '''
        Method Test: test_new_num
        Test method to verify the new_number method
        functions as expected. This also includes testing
        the random elements to ensure the correct amount and value
        of random integers are added. 
        Parameters:
           self: the current object
        Returns: 
            Nothing
        '''
        # starting board to test
        game_board = GameBoard(4, [[4, 0, 0, 4],
                                   [0, 0, 0, 2],
                                   [0, 0, 128, 8],
                                   [0, 0, 2, 4]])
        # number of 0s in board
        game_board_zero_count = 9
        # add new number to game board
        new_num_test = game_board.new_number()
        zero_count = 0
        new_num_value = []
        for row in new_num_test:
            for i in row:
                if i == 0:
                    zero_count += 1
                elif i != 0:
                    new_num_value.append(i)
        # test to confirm that there is 1 less 0 in game board when 0 is added 
        self.assertEqual(zero_count, game_board_zero_count - 1)
        # test to cofnirm that new random number generated are only 2 or 4
        self.assertTrue(new_num_value, (2 or 4) in new_num_value)


    def test_shift_left_for_testing(self):
        '''
        Method Test: test_shift_left_for_testing
        Test method to verify the shift_left_for_testing
        method functions as expected. The shift_left_for_testing
        method performs the core functionality of shifting. The 
        test of the randomness in the shift_left method is captured
        in the test_new_number method above. 
        Parameters:
           self: the current object
        Returns: 
            Nothing
        '''
        # test of normal shift and combine
        self.assertEqual(GameBoard(4, [[2, 2, 2, 2],
                                       [2, 4, 4, 2],
                                       [16, 16, 16, 8],
                                       [2, 2, 0, 0]]).shift_left_for_testing(), 
                                       [[4, 4, 0, 0],
                                        [2, 8, 2, 0],
                                        [32, 16, 8, 0],
                                        [4, 0, 0, 0]])
        # test of normal shift and combine
        self.assertEqual(GameBoard(4, [[0, 0, 0, 2],
                                       [0, 0, 0, 0],
                                       [0, 0, 0, 0], 
                                       [0, 0, 0, 0]]).shift_left_for_testing(), 
                                       [[2, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                         [0, 0, 0, 0]])
        # test of normal shift and combine
        self.assertEqual(GameBoard(4, [[2, 4, 2, 4], 
                                       [4, 2, 4, 2], 
                                       [32, 16, 128, 8],
                                       [2, 2, 1024, 0]]).shift_left_for_testing(), 
                                       [[2, 4, 2, 4], 
                                        [4, 2, 4, 2],
                                        [32, 16, 128, 8],
                                        [4, 1024, 0, 0]])
        # test of shift with nothing to shift
        self.assertEqual(GameBoard(4, [[2, 4, 2, 4], 
                                       [4, 2, 4, 2],
                                       [32, 16, 128, 8],
                                       [4, 1024, 0, 0]]).shift_left_for_testing(), 
                                       [[2, 4, 2, 4],
                                        [4, 2, 4, 2],
                                        [32, 16, 128, 8],
                                        [4, 1024, 0, 0]])
    
    def test_shift_right_for_testing(self):
        '''
        Method Test: test_shift_right_for_testing
        Test method to verify the shift_right_for_testing
        method functions as expected. The shift_right_for_testing
        method performs the core functionality of shifting. The 
        test of the randomness in the shift_right method is captured
        in the test_new_number method above. 
        Parameters:
           self: the current object
        Returns: 
            Nothing
        '''
        # test of normal shift and combine
        self.assertEqual(GameBoard(4, [[2, 4, 2, 4],
                                       [4, 2, 4, 2],
                                       [32, 16, 128, 8],
                                       [8, 1024, 2, 2]]).shift_right_for_testing(),
                                       [[2, 4, 2, 4], 
                                        [4, 2, 4, 2], 
                                        [32, 16, 128, 8],
                                        [0, 8, 1024, 4]])
        # test of normal shift and combine
        self.assertEqual(GameBoard(4, [[2, 2, 2, 2],
                                       [2, 4, 4, 2],
                                       [16, 16, 16, 8],
                                       [2, 2, 0, 0]]).shift_right_for_testing(), 
                                       [[0, 0, 4, 4],
                                        [0, 2, 8, 2],
                                        [0, 16, 32, 8],
                                        [0, 0, 0, 4]])
        # test of normal shift and combine
        self.assertEqual(GameBoard(4, [[4, 0, 0, 0],
                                       [0, 0, 0, 0],
                                       [0, 0, 0, 0],
                                       [0, 0, 0, 0]]).shift_right_for_testing(), 
                                       [[0, 0, 0, 4],
                                        [0, 0, 0, 0], 
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0]])
        # test of shift with nothing to shift
        self.assertEqual(GameBoard(4, [[2, 4, 2, 4],
                                       [4, 2, 4, 2],
                                       [32, 16, 128, 8],
                                       [0, 0, 1024, 4]]).shift_right_for_testing(), 
                                       [[2, 4, 2, 4],
                                        [4, 2, 4, 2],
                                        [32, 16, 128, 8],
                                        [0, 0, 1024, 4]])

    def test_shift_up_for_testing(self):
        '''
        Method Test: test_shift_up_for_testing
        Test method to verify the shift_up_for_testing
        method functions as expected. The shift_up_for_testing
        method performs the core functionality of shifting. The 
        test of the randomness in the shift_up method is captured
        in the test_new_number method above. 
        Parameters:
           self: the current object
        Returns: 
            Nothing
        '''
        # test of normal shift and combine
        self.assertEqual(GameBoard(4, [[2, 4, 2, 4],
                                       [2, 4, 0, 0], 
                                       [0, 0, 4, 2],
                                       [2, 2, 2, 0]]).shift_up_for_testing(),
                                       [[4, 8, 2, 4],
                                        [2, 2, 4, 2],
                                        [0, 0, 2, 0],
                                        [0, 0, 0, 0]])
        # test of normal shift and combine
        self.assertEqual(GameBoard(4, [[0, 0, 0, 0], 
                                       [0, 0, 2, 0],
                                       [0, 4, 0, 0],
                                       [0, 0, 0, 8]]).shift_up_for_testing(),
                                       [[0, 4, 2, 8],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0]])
        # test of normal shift and combine
        self.assertEqual(GameBoard(4, [[0, 2, 4, 0],
                                       [0, 32, 32, 4],
                                       [8, 32, 0, 4],
                                       [4, 32, 2, 0]]).shift_up_for_testing(),
                                       [[8, 2, 4, 8],
                                        [4, 64, 32, 0],
                                        [0, 32, 2, 0],
                                        [0, 0, 0, 0]])
        # test of shift with nothing to shift
        self.assertEqual(GameBoard(4, [[2, 4, 2, 4],
                                       [4, 2, 0, 0], 
                                       [0, 0, 0, 0],
                                       [0, 0, 0, 0]]).shift_up_for_testing(), 
                                       [[2, 4, 2, 4],
                                        [4, 2, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0]])
    
    def test_shift_down_for_testing(self):
        '''
        Method Test: test_shift_down_for_testing
        Test method to verify the shift_down_for_testing
        method functions as expected. The shift_down_for_testing
        method performs the core functionality of shifting. The 
        test of the randomness in the shift_down method is captured
        in the test_new_number method above. 
        Parameters:
           self: the current object
        Returns: 
            Nothing
        '''
        # test of normal shift and combine
        self.assertEqual(GameBoard(4, [[4, 8, 2, 4],
                                       [2, 2, 4, 2],
                                       [0, 0, 2, 0],
                                       [0, 0, 0, 0]]).shift_down_for_testing(),
                                       [[0, 0, 0, 0],
                                        [0, 0, 2, 0],
                                        [4, 8, 4, 4],
                                        [2, 2, 2, 2]])
        # test of normal shift and combine
        self.assertEqual(GameBoard(4, [[2, 4, 2, 32],
                                       [0, 4, 0, 32], 
                                       [2, 0, 4, 32], 
                                       [2, 0, 0, 32]]).shift_down_for_testing(), 
                                       [[0, 0, 0, 0],
                                        [0, 0, 0, 0], 
                                        [2, 0, 2, 64], 
                                        [4, 8, 4, 64]])
        # test of normal shift and combine
        self.assertEqual(GameBoard(4, [[128, 8, 512, 16],
                                       [128, 8, 0, 8], 
                                       [512, 0, 2, 2], 
                                       [512, 1024, 2, 4]]).shift_down_for_testing(),
                                       [[0, 0, 0, 16],
                                        [0, 0, 0, 8], 
                                        [256, 16, 512, 2], 
                                        [1024, 1024, 4, 4]])
        # test of shift with nothing to shift
        self.assertEqual(GameBoard(4, [[0, 2, 4, 0], 
                                       [0, 4, 2, 0], 
                                       [8, 8, 8, 16], 
                                       [1024, 128, 64, 32]]).shift_down_for_testing(), 
                                       [[0, 2, 4, 0], 
                                        [0, 4, 2, 0],
                                        [8, 8, 8, 16],
                                        [1024, 128, 64, 32]])
        
    def test_str(self):
        '''
        Method Test: test_str
        Test method to verify if the string representation 
        of the current game board instance is as expected
        Parameters:
           self: the current object
        Returns: 
            Nothing
        '''
        self.assertEqual(str(GameBoard(4, [[0, 2, 4, 0], 
                                       [0, 4, 2, 0], 
                                       [8, 8, 8, 16], 
                                       [1024, 128, 64, 32]])), '[[0, 2, 4, 0], ' 
                                       '[0, 4, 2, 0], ' 
                                       '[8, 8, 8, 16], ' 
                                       '[1024, 128, 64, 32]]')
        self.assertEqual(str(GameBoard(4,[[128, 8, 512, 16],
                                       [128, 8, 0, 8], 
                                       [512, 0, 2, 2], 
                                       [512, 1024, 2, 4]])), '[[128, 8, 512, 16], '
                                       '[128, 8, 0, 8], '
                                       '[512, 0, 2, 2], '
                                       '[512, 1024, 2, 4]]')
        self.assertEqual(str(GameBoard(4, [[4, 8, 2, 4],
                                       [2, 2, 4, 2],
                                       [0, 0, 2, 0],
                                       [0, 0, 0, 0]])), '[[4, 8, 2, 4], '
                                       '[2, 2, 4, 2], '
                                       '[0, 0, 2, 0], '
                                       '[0, 0, 0, 0]]')

def main():
    unittest.main()
if __name__ == '__main__':
    main()

