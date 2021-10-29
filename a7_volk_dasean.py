# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 7
# Description: User vs. computer game of rock, paper, and scissors utilizing functions.

# ---------------------------------------WELCOME TO ROCK, PAPER, SCISSORS-------------------------------------------- #

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
    print("Enter 0 for Rock, 1 for Paper, or 2 for Scissors")
    for i in range(0, 3):
      user = int(input("> "))
      # if user > 3 or < 0: # Make sure that user 0,1, or 2.

# Define the playRound(computerChoice, playerChoice) function.
# o Parameter 1: an integer representing the computer’s choice
# o Parameter 2: an integer representing the player’s choice
# o Return value: an integer the represents if there was a tie or the winner:
# • Return -1 if the computer won the round
# • Return 1 if the player won the round
# • Return 0 if there is a tie

# def playRound():

# Define the continueGame() function.
# o Parameters: None
# o Return value: a bool (Boolean), which is True or False (not a string)
# o Ask the user if they want to continue. Allow them to enter upper or lower case
# letters.

# def continueGame():
#       playAgain = input("Do you want to continue playing (y or n)?")
#       if playAgain == "y".lower():





# ------------------------------------------------CALL FUNCTIONS----------------------------------------------------- #

displayMenu()
getComputerChoice()
getPlayerChoice()
# call the rest of the functions




