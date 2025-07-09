from tictactoe import TicTacToe
import os

# clears console depending on OS
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# recurring function
def running():
    # Introduction
    print("=======================")
    print("Welcome to Tic Tac Toe!")
    print("=======================\n")

    # Creates the game
    game = TicTacToe()

    # Asks user if they want to replay
    bContinue = True
    # Determines whether a winner has been found
    gameOver = False
    # while bContinue:
    print("You are X:")

# loops until no one can play anymore
    while not gameOver:
        try:
            row = int(input("Choose the row you want to place your x: "))
            column = int(input("Choose the column you want to place your x: "))
            if row-1 > 2 or row-1 < 0:
                print("You need to choose between 1-3.") # 1 2 3 but in list format it is 0 1 2
            elif column-1 > 2 or column-1 < 0:
                print("You need to choose between 1-3.")
            else:
                game.player_move(row,column)
        except ValueError:
            print("Only insert numbers, silly!")
    
    # TODO - Determine winner

    # TODO - Ask player if they want to continue
    qContinue = input("Do you want to play again? Type 'y' or 'n': ")
    # if yes, recursion, if no, quit program
    if (qContinue == 'y'):
        clear_console()
        return running()
    elif (qContinue == 'n'):
        print("\nHave a good day.\n")
        # bContinue = False

    

running()
       

