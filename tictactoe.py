import random
import time


class TicTacToe:
    def __init__(self):
        self.board = [
            ["-" for _ in range(3)] for _ in range(3)
        ]  # Empty board used for Tic Tac Toe
        self.gameOver = False

    # Hardcoded version:
    # board = [
    #     ['-', '-', '-'],
    #     ['-', '-', '-'],
    #     ['-', '-', '-']
    # ]
    def player_move(self, row, column):

        if self.board[row][column] == "X" or self.board[row][column] == "O":
            print("You cannot place your X there.")
        elif self.board[row][column] == "-":
            self.board[row][column] = "X"
            self.show_board()

    def pc_move(self):
        print("PC is placing his circle...\n")
        time.sleep(2)
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if self.board[x][y] == "-":
                self.board[x][y] = "O"
                print(f"PC placed O at {chr(65 + x)}{y + 1}")
                self.show_board()

                break

    def determine_winner(self):
        pass

        #    1   2   3
        # A  X | O |
        #   ---+---+---
        # B    | X |
        #   ---+---+---
        # C    |   | O

    def show_board(self):
        # print("    1   2   3")
        # alpha = ["A", "B", "C"]
        # counter = 0
        # for row in self.board:
        #     printRow = f" {alpha[counter]} "
        #     counter += 1
        #     for column in row:
        #         printRow += f" {column} |"
        #     print(printRow)
        #     print("   ---+---+---")

        print("    1   2   3")
        alpha = ["A", "B", "C"]
        for i, row in enumerate(self.board):
            row_str = " | ".join(row)
            print(f" {alpha[i]}  {row_str}")
            if i < len(self.board) - 1:
                print("   ---+---+---")


if __name__ == "__main__":
    game = TicTacToe()
    game.show_board()
