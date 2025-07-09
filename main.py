from tictactoe import TicTacToe
import os


# clears console depending on OS
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


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
        bPlayer_turn = True
        try:

            if bPlayer_turn:
                row = int(input("Choose the row you want to place your x: ")) - 1
                column = int(input("Choose the column you want to place your x: ")) - 1
                if row > 2 or row < 0:
                    print(
                        "You need to choose between 1-3."
                    )  # 1 2 3 but in list format it is 0 1 2
                elif column > 2 or column < 0:
                    print("You need to choose between 1-3.")
                else:
                    game.player_move(row, column)
                    bPlayer_turn = False
                    game.pc_move()
        except ValueError:
            print("Only insert numbers, silly!")

    # TODO - Determine winner

    # TODO - Ask player if they want to continue
    qContinue = input("Do you want to play again? Type 'y' or 'n': ")
    # if yes, recursion, if no, quit program
    if qContinue == "y":
        clear_console()
        return running()
    elif qContinue == "n":
        print("\nHave a good day.\n")
        # bContinue = False


running()
