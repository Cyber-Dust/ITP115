# Dasean Volk, dvolk@usc.edu
# Fall 2021, ITP 115
# Section: Boba
# Assignment 8
# Description:

# -----------------------------------------TIC TAC TOE--------------------------------------------------- #

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

# def is_valid_move(boardList, spot):
board = ["|__|__|__|",
         "|__|__|__|",
         "|__|__|__|"]
# use a for loop to display a list vertically. A comma distinguishes the level.
for i in board: 
    print(i)
