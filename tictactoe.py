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
            return False
        elif self.board[row][column] == "-":
            self.board[row][column] = "\33[34mX\33[0m"
            self.show_board()
        return True

    # TODO - Make PC smarter
    def pc_move(self):
        print("\nPC is placing his circle...")
        time.sleep(2)
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if self.board[x][y] == "-":
                self.board[x][y] = "\33[31mO\33[0m"
                print(f"PC placed \33[31mO\33[0m at {chr(65 + x)}{y + 1}\n")
                self.show_board()

                break
        # Smarter PC logic (in comments):
        # 1. Check if PC can win in the next move. If yes, make that move.
        # 2. Check if player can win in the next move. If yes, block that move.
        # 3. Otherwise, pick a random empty spot.

        # Example implementation steps:
        # for each empty cell:
        #     - Temporarily place 'O' in the cell
        #     - Check if this leads to a win for PC
        #     - If yes, make this move and return
        #     - Else, revert the cell
        # for each empty cell:
        #     - Temporarily place 'X' in the cell
        #     - Check if this leads to a win for player
        #     - If yes, place 'O' there to block and return
        #     - Else, revert the cell
        # If no immediate win or block, pick a random empty cell as before.

        # --- CODED SMARTER PC LOGIC BELOW (IN COMMENTS) ---
        # # 1. Try to win
        # for i in range(3):
        #     for j in range(3):
        #         if self.board[i][j] == "-":
        #             self.board[i][j] = "O"
        #             if self.check_win("O"):
        #                 print(f"PC placed O at {chr(65 + i)}{j + 1}")
        #                 self.show_board()
        #                 return
        #             self.board[i][j] = "-"
        #
        # # 2. Block player win
        # for i in range(3):
        #     for j in range(3):
        #         if self.board[i][j] == "-":
        #             self.board[i][j] = "X"
        #             if self.check_win("X"):
        #                 self.board[i][j] = "O"
        #                 print(f"PC placed O at {chr(65 + i)}{j + 1}")
        #                 self.show_board()
        #                 return
        #             self.board[i][j] = "-"
        #
        # # 3. Otherwise, random move
        # while True:
        #     x = random.randint(0, 2)
        #     y = random.randint(0, 2)
        #     if self.board[x][y] == "-":
        #         self.board[x][y] = "O"
        #         print(f"PC placed O at {chr(65 + x)}{y + 1}")
        #         self.show_board()
        #         break
        #
        # # Helper function needed:
        # # def check_win(self, symbol):
        # #     # Check rows, columns, and diagonals for a win for 'symbol'
        # #     ...

    # To determine the winner in a Tic Tac Toe match, you need to check if either player has succeeded in placing three of their marks in a row. This can happen in three ways:
    # 1. Horizontally: All three cells in any row contain the same player's symbol.
    # 2. Vertically: All three cells in any column contain the same player's symbol.
    # 3. Diagonally: All three cells in either of the two diagonals contain the same player's symbol.
    # If any of these conditions are met for a player, that player is declared the winner.

    def determine_winner(self, char):

        # TODO - Determine winner horizontally
        for row in self.board:
            counter = 0
            for column in row:
                if column == char:
                    counter += 1
                    if counter == 3:
                        return True, char

        # TODO - Determine winner vertically

        for _ in range(0, 3):  # self.board[0][1] self.board[1][1] self.board[2][1]
            counter = 0
            for value in range(0, 3):
                if self.board[value][_] == char:
                    counter += 1
                    if counter == 3:
                        return True, char

        # TODO - Determine winner diagonally.
        l_diagonal = 0
        for _ in range(0, 3):
            if self.board[_][_] == char:
                l_diagonal += 1
                if l_diagonal == 3:
                    return True, char

        r_diagonal = 0  # 0,2    1,1    2,0
        length_of_board = 2
        for _ in range(0, 3):  # 0,2  1,1    2,0
            if self.board[_][length_of_board] == char:
                r_diagonal += 1
                length_of_board -= 1
                if r_diagonal == 3:
                    return True, char
        # TODO - Determine draw
        if all(cell != "-" for row in self.board for cell in row):
            return True, "draw"

        return False, None

        # TODO - Determine winner vertically
        # TODO - Determine winner diagonally

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
