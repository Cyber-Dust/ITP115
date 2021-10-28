# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 7 
# Description:
# -----------------------------------------------NAME: TITLE--------------------------------------------------------- #

import random


# define displayMenu() function
# Parameters (input): None
# o Return value (output): None
# o Displays the game rules to the user:

def displayMenu():
    print("Let's play Rock Paper Scissors.\nThe rules of the game are:\n  Rock smashes Scissors\n  Scissors cut Paper"
          "\n  Paper covers Rock\n  If both the choices are the same, it's a tie")


# define getComputerChoice() function
# Parameters (input): None
# o Return value (output): an integer that is a random number between 0 and 2.
# o Use the random module to get a random integer between 0 and 2.

def getComputerChoice():
    random_num = random.randrange(0, 2)
    return random_num


# Define the getPlayerChoice() function.
# o Parameters (input): None
# o Return value (output): an integer that represents the user’s choice
# o Display the following message to the user:

def getPlayerChoice():
    user = int(input("Enter 0 for Rock, 1 for Paper, or 2 for Scissors\n > "))


# ------------------------------------CALL FUNCTIONS---------------------------------------------- #

displayMenu()
getComputerChoice()
getPlayerChoice()

