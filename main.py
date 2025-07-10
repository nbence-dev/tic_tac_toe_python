from tictactoe import TicTacToe
import os


# clears console depending on OS
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


# recurring function
def running():
    # Introduction
    print("\33[92m=======================")
    print("\33[93mWelcome to Tic Tac Toe!")
    print("\33[92m=======================\33[0m\n")

    # Creates the game
    game = TicTacToe()

    game.show_board()
    # Asks user if they want to replay
    bContinue = True
    # Determines whether a winner has been found
    winnerChar = ""
    gameOver = False
    # while bContinue:
    print("\nYou are X:")

    # loops until no one can play anymore
    while not gameOver:
        bPlayer_turn = True
        try:

            if bPlayer_turn:
                row = (
                    int(input("Choose the \33[91mROW\33[0m you want to place your x: "))
                    - 1
                )
                # row = (
                #     input("Choose the \33[91mROW\33[0m you want to place your x: ")
                #     .lower()
                #     .strip()
                # )
                column = (
                    int(
                        input(
                            "Choose the \33[91mCOLUMN\33[0m you want to place your x: "
                        )
                    )
                    - 1
                )
                print()
                if row > 2 or row < 0:
                    print("You need to choose between 1-3.")
                # if not row in ["A", "B", "C"]:
                #     print(
                #         "You need to choose between A-C."
                #     )  # 1 2 3 but in list format it is 0 1 2
                elif column > 2 or column < 0:
                    print("You need to choose between 1-3.")
                else:
                    bValidMove = game.player_move(row, column)
                    if bValidMove:
                        bPlayer_turn = False
                        winnerDetermined, winnerChar = game.determine_winner("X")
                        if not winnerDetermined:
                            game.pc_move()
                            winnerDetermined, winnerChar = game.determine_winner("O")
                            if winnerDetermined:
                                gameOver = True
                        else:
                            gameOver = True
        except ValueError:
            print("Only insert numbers, silly!")

    # TODO - Determine winner
    print("\n=================")
    print(f"The winner is: {winnerChar}")
    print("=================\n")

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
