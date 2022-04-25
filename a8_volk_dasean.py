# Dasean Volk, dvolk@usc.edu
# Assignment 8

# -----------------------------------------TIC TAC TOE--------------------------------------------------- #
# Description:
# This is a game of tic tac toe. Enter a number between 0-8 that correlates to the spot on the board you wish to
# select. The game will alternate players and determine the winner after all spots on the board are chosen.

import TicTacToeHelper


# Define the isValidMove(boardList, spot) function.
# o Parameter 1: a list representing the board
# o Parameter 2: an integer corresponding to the index position that a user would
# like to place their letter on
# o Return value: a boolean value (True or False)
# o This function should look at the specified spot on the board. Return True if the
# spot is open. Return False if the spot is taken or if the spot parameter is not a
# valid index. A spot is taken if it equals "x" or "o". A valid index is between 0 and
# 8 (inclusive).

def is_valid_move(board_list, spot):
    if spot < 0 or spot > 8:
        return False # returns false if you enter an invalid integer
    elif board_list[spot] == "x" or board_list[spot] =="o":
        return False
    else:
        return True


def update_board(board_list, spot, player_letter):
    # index spot
    board_list[spot] = player_letter

def play_game():
    board_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    move_counter = 0
    winner = "n"
    while winner == "n":
        TicTacToeHelper.printUglyBoard(board_list)
        if move_counter % 2 == 0:
            x_move = int(input("Player x pick a spot: "))
            # check if the move is valid
            move_counter += 1
            while is_valid_move(board_list, x_move) == False:
                x_move = int(input("Player x, pick a spot: "))
            # return a T or F
            update_board(board_list, x_move, "x")
        elif move_counter % 2 == 1:
            o_move = int(input("Player o, pick a spot: "))
            move_counter += 1
            while is_valid_move(board_list, o_move) == False:
                o_move = int(input("Player o, pick a spot: "))
            update_board(board_list, o_move, "o")
        winner = TicTacToeHelper.checkForWinner(board_list, move_counter)
    print("\nGame Over!")
    if winner == "x":
        print("Player x is the winner!")
    elif winner == "o":
        print("Player o is the winner!")
    elif winner == "s":
        print("Stalemate reached!")
    # Check for winner will output n,s,x, or o
    # s = stalemate

def continue_game():
    play_again = input("Do you want to continue playing (y or n)? ")
    if play_again.lower() == "y":
        return True
    elif play_again.lower() == "n":
        return False

def main():
    new_game = True
    # do while loop that plays game until user wishes to exit
    while new_game:
        print("Welcome to Tic Tac Toe!")
        play_game()
        new_game = continue_game()
    print("\nThank you for playing. Goodbye!")
main()
