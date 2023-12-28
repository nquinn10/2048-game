'''
CS5001
Spring 2023
2048 - Game Logic Class 

This program creates the 2048 game logic class
that initializes a game board of the standard 
4x4 grid. It contains methods that represent the 
allowable moves in the traditional 2048 game such 
as shifting left, right, up, and down. When the game 
board is shifted, a new tile of value 2 or 4 will show 
up. For the purpose of testing the logic behind the shifts,
there are additional methods for the sole purpose of 
testing the shift logic without the random component. 
Lastly, this class imports and calls the DrawBoard class 
which triggers the game board to be generated and updated 
as moves are made based on keyboard key presses. 

Nicole Quinn
'''
import random
from Draw_Board import DrawBoard
import turtle

class GameBoard:
    '''
    The GameBoard class initializes a 2048 game board of the standard 
    4x4 grid, taking in either an empty list or a pre-established 
    game board containing a list of sublists with integer values. 
    Once created, the class contains methods that shift the game
    board in the established directions (left, right, up, and down),
    leveraging helper methods where necessary. As moves are made,
    new values are added. In addition, there are
    methods to create a new game instance, detect if the game is over,
    and draw the game board leveraging Turtle and by importing the
    DrawBoard class. Lastly, various methods can be called by pressing
    established keys.
    '''

    def __init__(self, board_size, new_game):
        '''
        Constructor: __init__ 
        Creates an new instance of a 4x4 game board.
        Parameters:
           self: the current object
           board_size: size of game board, int
           new_game: an empty list or list of sublists
           containing integers (4x4)
        Returns: 
            Nothing
        Pre-condition:
        board_size: this program assumes a game board of size 4 only. 
        Value error will be raise is board_size is not 4 or if it is
        not an int. 
        new_game: to play the game from the start, this will be an
        empty list. However, to assist with testing various scenarios, 
        a list of sublists representing the values of an in progress 
        game board can be input to start play from that point. These 
        values must be integers. A value error will be raised if 
        new_game is not a list. If a non-empty list is input, 
        a value error will be raised if list of sublists contains
        non-int values
        '''
        # setting the game score to 0 upon initialization
        self.score = 0
        self.board_size = board_size
        self.new_game = new_game
        if not isinstance(board_size, int):
            raise ValueError('board size needs to be int')
        if board_size != 4:
            raise ValueError('board size needs to be 4')
        if not isinstance(new_game, list):
            raise ValueError('new_game need to be list')
        # if playing a new game - 2 random #s to start
        if new_game == []:
            # 4 rows containg 4 0s
            for i in range(board_size):
                self.new_game.append([0] * board_size)
            game_start = [2, 4]
            random_column = random.randint(0, board_size - 1)
            random_row = random.randint(0, board_size - 1)
            i = 0
            # loop until it finds 2 open spots for 2 or 4
            while i < 2:
                if self.new_game[random_row][random_column] != 0:
                    random_column = random.randint(0, board_size - 1)
                    random_row = random.randint(0, board_size - 1)
                else:
                    self.new_game[random_row][random_column] = \
                        random.choice(game_start)
                    i += 1
        # if inputting an established game board
        else:
            self.new_game = new_game
        if len(self.new_game) != 4:
            raise ValueError('board has more than 4 rows') 
        # to check for only int values in game board
        for row in self.new_game:
            if len(row) != 4:
                raise ValueError('row has more than 4 numbers') 
            for i in row:
                if not isinstance(i, int):
                   raise ValueError('integers only in game board') 
        # initialize game board drawing via DrawBoard class 
        self.draw = DrawBoard(board_size)
        self.t = turtle.Turtle()
        # ensure moves respond to key presses
        self.game_moves()

    def start_new_game(self):
        '''
        Method: start_new_game
        When called, takes in a game board instance and
        resets the game to a new game which includes two random
        game board tiles of value 2 or 4.
        Parameters:
           self: the current object
        Returns:
            updates current object to a new game which 
            includes two random game board tiles of value 2 or 4.
        '''
        # reset score to 0
        self.score = 0
        self.board_size
        self.new_game = []
        # 4 rows containg 4 0s
        for i in range(self.board_size):
            self.new_game.append([0] * self.board_size)
        game_start = [2, 4]
        random_column = random.randint(0, self.board_size - 1)
        random_row = random.randint(0, self.board_size - 1)
        i = 0
        # loop until it finds 2 open spots for 2 or 4
        while i < 2:
            if self.new_game[random_row][random_column] != 0:
                random_column = random.randint(0, self.board_size - 1)
                random_row = random.randint(0, self.board_size - 1)
            else:
                self.new_game[random_row][random_column] = \
                    random.choice(game_start)
                i += 1
        # call to start method which draws the board
        self.draw_game()
        return self.new_game
    
    def start_new_game_for_testing(self):
        '''
        Method: start_new_game_for_testing
        Created for the sole purpose of testing to test 
        functionality of original method without the call to 
        draw the board. 
        Parameters:
           self: the current object
        Returns:
            updates the current object to a new game which 
            includes two random game board tiles of value 2 or 4 
            without drawing.
        '''
        self.score = 0
        self.board_size
        self.new_game = []
        for i in range(self.board_size):
            self.new_game.append([0] * self.board_size)
        game_start = [2, 4]
        random_column = random.randint(0, self.board_size - 1)
        random_row = random.randint(0, self.board_size - 1)
        i = 0
        while i < 2:
            if self.new_game[random_row][random_column] != 0:
                random_column = random.randint(0, self.board_size - 1)
                random_row = random.randint(0, self.board_size - 1)
            else:
                self.new_game[random_row][random_column] = \
                    random.choice(game_start)
                i += 1
        return self.new_game
    
    def draw_game(self):
        '''
        Method: draw_game
        When called, takes in a game board instance and
        calls to DrawBoard class to draw the current game
        board. 
        Parameters:
           self: the current object
        Returns:
            nothing
        '''
        # call to draw initialized game board 
        self.draw.board_setup(self.new_game, self.score, self.game_over())
    
    def game_over(self):
        '''
        Method: game_over
        Method to detect when the game is classified as over. 
        This occurs when the number 2048 exists on the board or
        when there are no more valid moves and there is no more
        open space left on the board. A valid move is shifting 
        left, right, up, or down where numbers can be combined. 
        Parameters:
           self: the current object
        Returns:
            A boolean value - True or False 
        Post-condition:
            When False, the user has either not won or there is a
            valid move that exists. If True, the user has won by
            reaching 2048 or the are no more valid moves and the
            game board is full.
        '''
        game_over_check = []
        for row in self.new_game:
            for square in row:
                game_over_check.append(square)
        # check to see if 2048 exists as a tile value
        if 2048 in game_over_check:
            return True
        for row in range(len(self.new_game)):
            for i in range(len(self.new_game[row])):
                # check to see if there are empty spaces left
                if self.new_game[row][i] == 0:
                    return False
                # check if element to the right is equal
                elif i < (len(self.new_game) - 1) and \
                    self.new_game[row][i] == self.new_game[row][i+1]:
                    return False
                # check if element below is equal
                elif row < (len(self.new_game) - 1) and \
                    self.new_game[row][i] == self.new_game[row + 1][i]:
                    return False
        return True

    def new_number(self):
        '''
        Method: new_number
        Method to add a new number (2 or 4) to the game board. Helper
        method that is called within shift methods to add a random
        new number after a successful move is made.
        Parameters:
           self: the current object
        Returns:
            An updated game board with a new random number
            added in. 
        '''
        random_num = [2, 4]
        random_column = random.randint(0, self.board_size - 1)
        random_row = random.randint(0, self.board_size - 1)
        full_board_check = []
        for row in self.new_game:
            for square in row:
                full_board_check.append(square)
        # check to see if there is any space left in the board
        if 0 not in full_board_check:
            self.game_over()
        else: # if space remains, add random num to open spot
            while self.new_game[random_row][random_column] != 0:
                random_column = random.randint(0, self.board_size - 1)
                random_row = random.randint(0, self.board_size - 1)
            self.new_game[random_row][random_column] = \
                random.choice(random_num)
            return self.new_game

    def reverse(self):
        '''
        Method: reverse
        Helper method that is called within shift right and down
        methods to re-order each row in the grid in reverse order.
        Parameters:
           self: the current object
        Returns:
            An updated game board where each row is in reverse order. 
        '''
        # creation of new list containing reverse order for each row
        reverse_grid = []
        for row in self.new_game:
            reverse_row = []
            for i in row[::-1]:
                reverse_row.append(i)
            reverse_grid.append(reverse_row)
        self.new_game = reverse_grid
        return self.new_game
    
    def transpose(self):
        '''
        Method: transpose
        Helper method that is called within shift up and down
        methods to transpose the game board.
        Parameters:
           self: the current object
        Returns:
            An updated game board that is transposed
        '''
        # creation of new list containing transposed game board
        transposed_grid = []
        for i in range(4):
            transposed_grid.append([])
        for row in range(self.board_size):
            for i in transposed_grid:
                i.append(self.new_game[row][0])
                self.new_game[row].pop(0)
        self.new_game = transposed_grid
        return self.new_game
    
    def shift(self):
        '''
        Method: shift
        Helper method that shifts the values of each row
        to the left where there is open space.
        Parameters:
           self: the current object
        Returns:
            An updated game board that has been shifted to
            the left
        Post condition:
            The values are shifted to the left, but not combined. 
        '''
        # default is left shift 
        shifted_grid = []
        for row in self.new_game:
            # append non zero digits 
            shifted_row = []
            for i in row:
                if i != 0:
                    shifted_row.append(i)
            # fill in rest of row with 0s
            while len(shifted_row) < len(row):
                shifted_row.append(0)
            shifted_grid.append(shifted_row)
        self.new_game = shifted_grid
        return self.new_game
    
    def shift_and_combine(self):
        '''
        Method: shift_and_combine
        Helper method that takes the current game board, 
        shifts the game board to the left, adds equal values next to 
        each other together, and then shifts the game board an 
        additional time to adjust for any values that were combined.
        Any combination of numbers updates the overall score. 
        Parameters:
           self: the current object
        Returns:
            An updated game board that has been shifted, combined, 
            and shifted an additional time
        '''
        # default is left shift 
        self.new_game = self.shift()
        for row in self.new_game:
            # stopping at last index on game board
            for i in range(len(row[:3])):
                if row[i] == 0:
                    row[i]
                # add equal numbers
                elif row[i] == row[i + 1]:
                    row[i] = (row[i] + row[i + 1])
                    self.score += row[i] # add combination sum to score
                    row[i + 1] = 0 
                else:
                    row[i] = row[i]
        # shift again once values are combined 
        self.new_game = self.shift()
        #update score
        self.score = self.score
        return self.new_game
    
    def shift_left(self):
        '''
        Method: shift_left
        Method that shifts numbers in the game board to the left.
        Leverages helper functions shift and shift and combine to ensure
        numbers are shifted to the left and combined where possible.
        If numbers can be shifted to the left (as in there is space to move 
        pieces to the left), a new number will be added in a random open
        spot on the game board. 
        Parameters:
           self: the current object
        Returns:
            An updated game board that has been shifted, combined, 
            and shifted an additional time to the left and a new 
            number has been added pending the board could be shifted. 
        '''
        # creation of copy of current game board
        game_board_copy = []
        for row in self.new_game:
            temp = []
            for i in row:
                temp.append(i)
            game_board_copy.append(temp)
        # shift and combine equal values
        self.new_game = self.shift_and_combine()
        # if board is changed with shift/combine, add new num
        if game_board_copy != self.new_game:
            self.new_game = self.new_number()
            self.draw_game()

        self.draw_game()
        return self.new_game
        
    def shift_left_for_testing(self):
        '''
        Method: shift_left_for_testing
        Created for the sole purpose of testing to test 
        functionality of shift_left without adding a new random
        number after shifting or drawing the game board.
        Parameters:
           self: the current object
        Returns:
            An updated game board that has been shifted, combined, 
            and shifted an additional time to the left. 
        '''
        # shift and combine equal values
        self.new_game = self.shift_and_combine()
        return self.new_game

    def shift_right(self):
        '''
        Method: shift_right
        Method that shifts numbers in the game board to the right.
        Leverages helper functions reverse, shift, and shift and combine 
        to ensure numbers are shifted to the right and combined where possible.
        If numbers can be shifted to the right (as in there is space to move 
        pieces to the right), a new number will be added in a random open
        spot on the game board. 
        Parameters:
           self: the current object
        Returns:
            An updated game board that has been shifted, combined, 
            and shifted an additional time to the right and a new 
            number has been added pending the board could be shifted. 
        '''
        # creation of copy of current game board
        game_board_copy = []
        for row in self.new_game:
            temp = []
            for i in row:
                temp.append(i)
            game_board_copy.append(temp)
        # reverse grid 
        self.new_game = self.reverse()
        # shift and combine equal values
        self.new_game = self.shift_and_combine()
        # reverse back
        self.new_game = self.reverse()
        # if board is changed with shift/combine, add new num
        if game_board_copy != self.new_game:
            self.new_game = self.new_number()
            self.draw_game()
        
        self.draw_game()
        return self.new_game
        
    def shift_right_for_testing(self):
        '''
        Method: shift_right_for_testing
        Created for the sole purpose of testing to test 
        functionality of shift_right without adding a new random
        number after shifting or drawing the game board.
        Parameters:
           self: the current object
        Returns:
            An updated game board that has been shifted, combined, 
            and shifted an additional time to the right. 
        '''
        # reverse grid 
        self.new_game = self.reverse()
        # shift and combine equal values
        self.new_game = self.shift_and_combine()
        # reverse back
        self.new_game = self.reverse()
        return self.new_game

    def shift_up(self):
        '''
        Method: shift_up
        Method that shifts numbers in the game board up.
        Leverages helper functions transpose, shift, and shift and combine 
        to ensure numbers are shifted up and combined where possible.
        If numbers can be shifted up (as in there is space to move 
        pieces up), a new number will be added in a random open
        spot on the game board. 
        Parameters:
           self: the current object
        Returns:
            An updated game board that has been shifted, combined, 
            and shifted an additional time up and a new 
            number has been added pending the board could be shifted. 
        '''
        # creation of copy of current game board
        game_board_copy = []
        for row in self.new_game:
            temp = []
            for i in row:
                temp.append(i)
            game_board_copy.append(temp)
        # take grid and transpose
        self.new_game = self.transpose()
        # combine equal values
        self.new_game = self.shift_and_combine()
        # transpose back to normal grid
        self.new_game = self.transpose()
        # if board is changed with shift/combine, add new num
        if game_board_copy != self.new_game:
            self.new_game = self.new_number()
            self.draw_game()
        
        self.draw_game()
        return self.new_game

    def shift_up_for_testing(self):
        '''
        Method: shift_up_for_testing
        Created for the sole purpose of testing to test 
        functionality of shift_up without adding a new random
        number after shifting or drawing the game board.
        Parameters:
           self: the current object
        Returns:
            An updated game board that has been shifted, combined, 
            and shifted an additional time up. 
        '''
        # take grid and transpose
        self.new_game = self.transpose()
        # combine equal values
        self.new_game = self.shift_and_combine()
        # transpose back to normal grid
        self.new_game = self.transpose()
        return self.new_game

    def shift_down(self):
        '''
        Method: shift_down
        Method that shifts numbers in the game board down.
        Leverages helper functions transpose, reverse, shift, and 
        shift and combine to ensure numbers are shifted down and 
        combined where possible. If numbers can be shifted down 
        (as in there is space to move pieces down), a new number 
        will be added in a random open spot on the game board. 
        Parameters:
           self: the current object
        Returns:
            An updated game board that has been shifted, combined, 
            and shifted an additional time down and a new 
            number has been added pending the board could be shifted. 
        '''
        # creation of copy of current game board
        game_board_copy = []
        for row in self.new_game:
            temp = []
            for i in row:
                temp.append(i)
            game_board_copy.append(temp)
        # take grid and transpose
        self.new_game = self.transpose()
        # reverse grid
        self.new_game = self.reverse()
        # shift and combine
        self.new_game = self.shift_and_combine()
        # reverse back 
        self.new_game = self.reverse()
        # transpose back to normal grid
        self.new_game = self.transpose()
        # if board is changed with shift/combine, add new num
        if game_board_copy != self.new_game:
            self.new_game = self.new_number()
            self.draw_game()
            
        self.draw_game()
        return self.new_game
    
    def shift_down_for_testing(self):
        '''
        Method: shift_down_for_testing
        Created for the sole purpose of testing to test 
        functionality of shift_down without adding a new random
        number after shifting or drawing the game board.
        Parameters:
           self: the current object
        Returns:
            An updated game board that has been shifted, combined, 
            and shifted an additional time down. 
        '''
        # take grid and transpose
        self.new_game = self.transpose()
        # reverse grid
        self.new_game = self.reverse()
        # shift and combine
        self.new_game = self.shift_and_combine()
        # reverse back 
        self.new_game = self.reverse()
        # transpose back to normal grid
        self.new_game = self.transpose()
        return self.new_game

    def exit_game(self):
        '''
        Method: exit_game
        Method to exit the game by quitting Turtle.
        Parameters:
           self: the current object
        Returns:
            Quits Turtle and returns user to terminal 
        '''
        return turtle.bye()

    def game_moves(self):
            '''
        Method: game_moves
        Method that leverages Turtle onkeypress() method to connect
        key presses to a previously created method. Enables user
        to shift left, right, up, or down. In addition, allows
        user to quit the game or start a new one. 
        Parameters:
           self: the current object
        Returns:
            Nothing
            '''
            # set value of keys to methods
            self.t.screen.onkeypress(lambda: self.shift_left(), 'Left')
            self.t.screen.onkeypress(lambda: self.shift_right(), 'Right')
            self.t.screen.onkeypress(lambda: self.shift_up(), 'Up')
            self.t.screen.onkeypress(lambda: self.shift_down(), 'Down')
            self.t.screen.onkeypress(lambda: self.start_new_game(), 'n')
            self.t.screen.onkeypress(lambda: self.exit_game(), 'q')

            self.t.screen.listen()
    
    def end_game_moves(self):
            '''
        Method: game_moves
        Method that leverages Turtle onkeypress() method to connect
        key presses to a previously created method. Disables shift
        keys and only allows user to quit the game or start a new one. 
        Parameters:
           self: the current object
        Returns:
            Nothing
            '''
            # set value of keys to methods
            self.t.screen.onkeypress(None, 'Left')
            self.t.screen.onkeypress(None, 'Right')
            self.t.screen.onkeypress(None, 'Up')
            self.t.screen.onkeypress(None, 'Down')
            self.t.screen.onkeypress(lambda: self.start_new_game(), 'n')
            self.t.screen.onkeypress(lambda: self.exit_game(), 'q')

            self.t.screen.listen()

    def __str__(self):
        '''
        Method: __str__
        Takes in a game board instance and returns a string
        representation of the current game board instance.
        Parameters:
           self: the current object
        Returns:
            A string representation of the current game board 
            instance. In a list of sublists format. 
        '''
        output = (f"{self.new_game}")
        return output
    

