'''
CS5001
Spring 2023
2048 - Draw Board Class

This program creates the 2048 draw board class
that imports and initializes turtle to draw the game
board based on the 4x4 grid. It contains a board_setup
method which contains many helper methods to draw the
initial board outline and the tile values and colors 
as they change. In addition, it draws the game instructions,
title, score as it changes, and a game over message. 

Nicole Quinn
'''

import turtle

class DrawBoard:
    '''
    The DrawBoard class initializes a 2048 game board of the standard 
    4x4 grid, taking in a board of size 4 and initializes turtle to 
    draw the game. Once created, the class contains a board_setup
    method to draw the board containing the game board values and 
    score. This method draws on many helper functions to ensure the 
    game displays the game board, title, instructions, score, and a
    game over message if needed. __str__ method is not included as it
    is a drawing only class and there is nothing to print.
    '''
    
    def __init__(self, board_size):
        '''
        Constructor: __init__ 
        Initializes turtle and parameters for which the game board
        and game play screen will be drawn
        Parameters:
           self: the current object
           board_size: size of game board, int
        Returns: 
            Nothing
        Pre-condition:
        board_size: this program assumes a game board of size 4 only. 
        Value error will be raise is board_size is not 4 or if it is
        not an int. 
        '''
        self.board_size = board_size
        if not isinstance(board_size, int):
            raise ValueError('board size needs to be int')
        if board_size != 4:
            raise ValueError('board size needs to be 4')
        # set square side length
        self.square_length = 80
        # set border length
        self.border_length = 20
        # initiate turtle
        self.pen = turtle.Turtle()
        self.screen = turtle.Screen()
        self.tile_color = ''
        self.num_color = ''
        # set game board to empty list
        self.grid = []

    def board_setup(self, grid, score, end_game):
        '''
        Method: board_setup
        When called, it initializes turtle and game board to be drawn. 
        It takes in game board as a list of sublists, a score, and a boolean
        value to determine if the game is over and leverages turtle to draw
        a game board with the appropriate values in place.  
        Parameters:
           self: the current object
           grid: current game board, lists of sublists
           score: starting score for game board, int
           end_game: True - game is over, False - game is still
           active, boolean value
        Returns:
            Nothing
        '''
        # set up of turtle screen
        self.screen.bgcolor('#FAF8F0')
        turtle.screensize(2000, 2000)
        turtle.setup(1500, 1500)
        turtle.colormode(255)
        self.pen.screen.tracer(0, 0)
        self.pen.hideturtle()
        # call to write and update score
        self.draw_score(score)
        # call to draw_title method
        self.draw_title()
        # call to add instructions
        self.draw_instructions()
        y_point = 200
        # draw outer square border
        self.pen.penup()
        self.pen.goto(0, y_point)
        self.pen.pendown()
        self.pen.pencolor('#B4A397')
        self.pen.fillcolor('#B4A397')
        self.pen.begin_fill()
        for i in range(4):
            self.pen.forward(self.square_length * self.board_size + 
                             self.border_length * (self.board_size + 1))
            self.pen.right(90)
        self.pen.end_fill() 
        self.grid = grid
        board_values = []
        # loop to draw individual square tiles and add values
        for col in range(self.board_size):
            for row in range(self.board_size):
                x = self.border_length * (row + 1) + self.square_length * row
                y = y_point - (self.square_length * col) - \
                    (self.border_length * (col + 1))
                # identify tile value in grid
                tile_value = self.grid[col][row]
                board_values.append(tile_value)
                # assign 0s to blank tiles
                if tile_value == 0:
                    tile_value = ""
                else:
                    tile_value = self.grid[col][row]
                # use tile values to select color
                tile_color = self.fill_tile_color(tile_value)
                # draw the tile with the correct color
                self.draw_square(x, y, tile_color)
                self.pen.penup()
                self.pen.goto(x + self.square_length / 2, 
                              y - self.square_length / 2)
                self.pen.pendown()
                self.pen.pencolor('#776E65')
                # write tile value in tile
                self.pen.write(tile_value, align='center', 
                               font=('Clear Sans', 20, 'bold'))
        # call to end game methods to display correct message        
        if end_game == True and 2048 in board_values:
            self.game_won()
        elif end_game == True:
            self.end_game()
        turtle.update()
        turtle.done()
    

    def draw_square(self,x, y, color):
        '''
        Method: draw_square
        When called, it draws a square in provided color, 
        starting at x and y coordinates. 
        Parameters:
           self: the current object
           x: top left corner x coordinate, int
           y: top left corner y coordinate, int
           color: color hex code, string
        Returns:
            Nothing
        '''
        self.pen.penup()
        # set turtle to x,y coordinate
        self.pen.goto(x, y)
        self.pen.pendown()
        self.pen.pencolor('#CDC1B4')
        # set fill color based on number in tile
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        for i in range(4):
            self.pen.forward(self.square_length) 
            self.pen.right(90)
        self.pen.end_fill()

    def fill_tile_color(self, number):
        '''
        Method: fill_tile_color
        When called, returns tile's color hex code
        for the number provided
        Parameters:
           self: the current object
           number: tile value, int
        Returns:
            hex code of given number as a string
        '''
        if number == "":
            self.tile_color = '#C8B8AC'
        elif number == 2:
            self.tile_color = '#EDE0D5'
        elif number == 4:
            self.tile_color = '#EDDDC3'
        elif number == 8:
            self.tile_color = '#F7A974'
        elif number == 16:
            self.tile_color = '#FD8B5F'
        elif number == 32:
            self.tile_color = '#FE7159'
        elif number == 64:
            self.tile_color = '#FF543B'
        elif number == 128:
            self.tile_color = '#EEC96F'
        elif number == 256:
            self.tile_color = '#EEC560'
        elif number == 512:
            self.tile_color = '#EFC152' 
        elif number == 1024:
            self.tile_color = '#EFBD45'
        elif number == 2048:
            self.tile_color = '#EFBA3A'
        return self.tile_color
    
    
    def draw_title(self):
        '''
        Method: draw_title
        When called, writes the game board title
        in established location
        Parameters:
           self: the current object
        Returns:
            nothing
        '''
        self.pen.penup()
        self.pen.goto(120, 210)
        self.pen.pendown()
        self.pen.pencolor('#6D635B')
        self.pen.write('2048', align='right', 
                       font=('Clear Sans', 45, 'bold'))
    
    def draw_score(self, score):
        '''
        Method: draw_score
        When called, writes the game score in
        established location 
        Parameters:
           self: the current object
           score: current game score, int
        Returns:
            nothing
        '''
        self.pen.clear()
        self.pen.penup()
        self.pen.goto(310, 210)
        self.pen.pendown()
        self.pen.pencolor('#6D635B')
        self.pen.write(f'Score: {score}', align='left', 
                       font=('Clear Sans', 20, 'bold'))

    def draw_instructions(self):
        '''
        Method: draw_instructions
        When called, writes the game instructions
        in established location
        Parameters:
           self: the current object
        Returns:
            nothing
        '''
        self.pen.penup()
        self.pen.goto(-600, 50)
        self.pen.pendown()
        self.pen.pencolor('#6D635B')
        self.pen.write(f'Welcome to 2048 \n' '\n'
                       'HOW TO PLAY: Use your arrow keys to move the tiles. \n' 
                       'Tiles with the same number merge into one when they touch.\n'
                        'Add them up to reach 2048!\n' '\n'
                        'To start a new game, press the key "n"\n'
                        'To exit the game, press the key "q"', align='left', 
                        font=('Clear Sans', 20, 'bold'))
        
    def end_game(self):
        '''
        Method: end_game
        When called, writes game over message
        in established location
        Parameters:
           self: the current object
        Returns:
            nothing
        '''
        self.pen.penup()
        self.pen.goto(-300, -50)
        self.pen.pendown()
        self.pen.pencolor('#6D635B')
        self.pen.write('Game Over!', align='Center', 
                       font=('Clear Sans', 60, 'bold'))

    def game_won(self):
        '''
        Method: game_won
        When called, writes winning message
        in established location
        Parameters:
           self: the current object
        Returns:
            nothing
        '''
        self.pen.penup()
        self.pen.goto(-300, -100)
        self.pen.pendown()
        self.pen.pencolor('#6D635B')
        self.pen.write('Game Over,\n'
                        'You Won!', align='Center', 
                        font=('Clear Sans', 60, 'bold'))
