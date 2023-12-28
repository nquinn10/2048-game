## High Level Design:
This program contains 4 elements:
- GameBoard - This is a class specifically set up to house all of the
game board/move logic. This initializes a game board in the form of a 
list of sublists. The board is initialized to a new game which means
only two tiles with values (either 2 or 4) and the rest are filled with 
0s to represent blank tiles in the actual game. In addition, the score is
set to 0. In the event the user wants to input a 4x4 game board of their choosing
without starting from a new game, this class can also accommodate that. 
The DrawBoard class is also imported into this class and initialized in the 
constructor as well as a Turtle instance. This allows for the game board to be 
drawn and updated as moves are made. 

    This class contains various methods and helper methods to start and and draw
    a new game, detect if a game is over, shift the board left, right, up, and 
    down, add a new number, and exit the game. There are also methods to allow for
    game moves to be made based on key presses on the keyboard. 

    Lastly, to ensure the core functionality of the shift methods were tested, 
    test shift methods were created to remove the randomness component and call
    to draw method. Instead the randomness was tested in various other methods.

- DrawBoard - This class is specifically set up to house all of the Turtle
moves and methods to draw the game board as called upon, always containing
the game board outline, title, and instructions. This class initializes Turtle 
and establishes the game board sizing parameters which assumes a 4x4 grid. 

    This class contains various methods, most notably, the board_setup method
    which acts as the main method for drawing the actual board while calling on 
    various helper methods to display the correct messages, values, colors, etc.

    The board_setup method is called in the GameBoard class to ensure the board is 
    updated when moves are made. In addition to updating values, the board tiles will
    update in color based on the number value in the board. If the game is over, either 
    by reaching 2048 or by having no more valid moves, a game over message will be printed. 

- TestGameBoard - This class tests the GameBoard class by importing
the class and Python unittest and generating tests for various scenarios/game 
moves and exceptions for each of the core methods. In addition to testing the core functionality of the 
game board shift methods, it also tests for randomness to ensure that when a new number is added
or a new game board is created, the number of non-zero values is as expected as well as the
integer value of the number being added to the board (2 or 4). The core shift functions contain
many helper functions (shift, shift and combine, transpose, and reverse) and as such those were
not individually tested. Any method that was connected to drawing/turtle was not tested as specified in the project instructions. Lastly, the game over method was tested based on various scenarios where a game board would be considered finished/not finished. 

- Main - This is the main of the program where it can be run as a new game. It uses a while loop 
so that while the game is not deemed as over, you can continue to play and uses the keys. If the game
is deemed to be over based on established criteria, the key board shift functions will no longer work and 
you must either quit or start a new game. The quit - 'q' keyboard press works as expected and closes out
the program, but there is an error message in the terminal. This can be ignored as it has no impact on
the functionality of the program while playing or after playing. 


## Instructions - How to Run the Program
To run the program follow these steps: 
- Open each of the files contained in the zip
- Go to main.py and run the program. The default is set up to 
run as a new game. If you would like to input your own 4x4 list of sublists
you may do so and run the game from there
- Once the game has opened, use the left, right, up, and down arrows to move
the tiles in those directions. If a successful shift is made, as in a piece is 
moved or combined or both, a new tile will appear on the board. If for example, you 
shift left and there are nowhere for the tiles to shift, the game will not add a new tile. 
As shifts are made and tiles are combined, your score will update.
- Continue to play until you either win by reaching 2048 or until the game board is full
and there are no more valid moves. An appropriate message will appear on the screen. If you reach 
2048 and there are still additional moves that can be made, the game will let you keep playing until
there are no more valid moves. 
- If you would like to start a new game, select the 'n' key and a new game will be started and the score
will reset. If you would like to exit the game, select the 'q' key and the turtle window will close

## Program Features: 
- This program will initialize a new 4x4 2048 game board upon running it from main.
- This program will also initialize a 2048 4x4 game board grid of your choosing if that
is input into the GameBoard creation in main.
- The game board is only intended to be a 4x4 grid - no larger or smaller
- The game board window opens and displays the initialized game board. The window contains
the game title, instructions on how to move, start a new game, and quit. 
- The game board also actively tracks the game score above the board as moves are made. If a new
game is started, it is reset to 0.
- [Extra Credit] The game board leverages similar colors to the game board tiles on the real 2048 game and when tiles of equal values are merged, the colors are updated. 
- The game board logic is tested in the TestGameBoard.py file and passes all established tests
- The game board should be run as specified in the instructions above, but if non integer values are entered for the game board grid or if the game board is any size other than 4, value errors will be raised. These are also tested in the test file.

