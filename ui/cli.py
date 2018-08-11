"""Hello and welcome to Minesweeper as implemented by @rinslow
We will start a 5X5 Board for you with 6 mines as an example.
The way you communicate with this system is by inserting commands in the
format of 'R/F <X> <Y>' (R=Reveal, F=Flag) and the board will be displayed to you
"""
import os
from env.minesweeper import Board, WIN, LOSE, FLAG as FLAG_SYMBOL, UNKNOWN, INVALID_MOVE, GAME_ON, BOMB

REVEAL = "r"
FLAG = "f"


def print_board(displayed):
    for row in displayed:
        for cell in row:
            to_print = int(cell)
            if cell == float(FLAG_SYMBOL):
                to_print = "F"

            if cell == float(UNKNOWN):
                to_print = "?"

            if cell == float(BOMB):
                to_print = "X"

            print(to_print, end="  ")

        print("\n", end="")


def main():
    board = Board(5, 6)
    displayed = board.displayed
    outcome = GAME_ON

    while outcome not in (WIN, LOSE):
        os.system("clear")

        if outcome == INVALID_MOVE:
            print("You played an invalid move...")

        print_board(displayed)
        move = input("Your Move: ")
        move, x, y = move.split(" ")

        if move.lower() == REVEAL:
            displayed, outcome = board.reveal(int(x), int(y))

        elif move.lower() == FLAG:
            displayed, outcome = board.flag(int(x), int(y))

    if outcome == WIN:
        print("You won!")

    if outcome == LOSE:
        print("You lost :(")
        print_board(board.matrix)


if __name__ == '__main__':
    main()
