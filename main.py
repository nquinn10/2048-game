'''
CS5001
Spring 2023
2048 - Main

This program is the main and is where a user would
run and play the actual game itself. It imports the GameBoard
class and allows the user to play the game until it is over, 
the user starts a new one, or the user quits. 

Nicole Quinn
'''
from GameBoard import GameBoard
import turtle


def main():
    try:
        game = GameBoard(4, [])
        # while game is not over
        while game.game_over() == False:
            game.draw_game()
            game.game_moves()
            game.game_over()
            turtle.Turtle._screen.mainloop()
            # if game is over - disable move keys
            if game.game_over() == True:
                game.end_game_moves()
                break
    except ValueError as ex:
        print(f"ValueError was raised")
        print(f"This was the error: {ex}")
    
if __name__ == '__main__':
    main()
