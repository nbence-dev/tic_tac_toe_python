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
    print("\n\33[34mYou are X:\33[0m")

    # loops until no one can play anymore
    while not gameOver:
        bPlayer_turn = True
        try:

            if bPlayer_turn:
                # row = (
                #     int(input("Choose the \33[91mROW\33[0m you want to place your x: "))
                #     - 1
                # )
                row = (
                    input("\nChoose the \33[91mROW\33[0m you want to place your x: ")
                    .upper()
                    .strip()
                )
                column = (
                    int(
                        input(
                            "Choose the \33[91mCOLUMN\33[0m you want to place your x: "
                        )
                    )
                    - 1
                )
                print()

                # TODO - Convert A to number
                alpha = ["A", "B", "C"]
                numbers = [0, 1, 2]

                # if row > 2 or row < 0:
                #     print("You need to choose between 1-3.")
                if not row in alpha:
                    print(
                        "You need to choose between A-C."
                    )  # 1 2 3 but in list format it is 0 1 2
                elif column > 2 or column < 0:
                    print("You need to choose between 1-3.")
                else:
                    index = alpha.index(row)
                    row_num = numbers[index]

                    bValidMove = game.player_move(row_num, column)
                    if bValidMove:
                        bPlayer_turn = False
                        winnerDetermined, winnerChar = game.determine_winner(
                            "\33[34mX\33[0m"  # CHECK for x with blue
                        )
                        if not winnerDetermined:
                            game.pc_move()
                            winnerDetermined, winnerChar = game.determine_winner(
                                "\33[31mO\33[0m"  # check for o with red
                            )
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
