# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 7
# Description: User vs. computer game of rock, paper, and scissors utilizing functions.
# cmd + shift + r (mac) = replace all instances

# ---------------------------------------WELCOME TO ROCK, PAPER, SCISSORS-------------------------------------------- #

import random


# define display_menu() function
# Parameters (input): None
# o Return value (output): None
# o Displays the game rules to the user:

def display_menu():
    print("Let's play Rock Paper Scissors.\nThe rules of the game are:\n  Rock smashes Scissors\n  Scissors cut Paper"
          "\n  Paper covers Rock\n  If both the choices are the same, it's a tie")


# define get_computer_choice() function
# Parameters (input): None
# o Return value (output): an integer that is a random number between 0 and 2.
# o Use the random module to get a random integer between 0 and 2.

def get_computer_choice():
    computer_choice = random.randrange(0, 2)
    return computer_choice


# Define the get_player_choice() function.
# o Parameters (input): None
# o Return value (output): an integer that represents the user’s choice
# o Display the following message to the user:

def get_player_choice():
    print("\nEnter 0 for Rock, 1 for Paper, or 2 for Scissors")
    player_choice = int(input("> "))
    while player_choice > 2 or player_choice < 0:
        player_choice = int(input("> "))
    return player_choice


# Define the play_round(computerChoice, playerChoice) function.
# o Parameter 1: an integer representing the computer’s choice
# o Parameter 2: an integer representing the player’s choice
# o Return value: an integer the represents if there was a tie or the winner:
# • Return -1 if the computer won the round
# • Return 1 if the player won the round
# • Return 0 if there is a tie
# player = get_player_choice()
# computer = get_computer_choice()

def play_round(player, computer):
    if player == 0 and computer == 2:
        print("You Win!")
        return 1
    elif player == 2 and computer == 0:
        print("Computer Wins!")
        return -1
    elif player == 2 and computer == 1:
        print("You Win!")
        return 1
    elif player == 1 and computer == 2:
        print("Computer Wins!")
        return -1
    elif player == 0 and computer == 1:
        print("Computer Wins!")
        return -1
    elif player == 1 and computer == 0:
        print("You Win!")
        return 1
    elif player == computer:
        print("Its a tie!")
        return 0


# Define the continue_game() function.
# o Parameters: None
# o Return value: a bool (Boolean), which is True or False (not a string)
# o Ask the user if they want to continue. Allow them to enter upper or lower case
# letters.

def continue_game():
    play_again = input("Do you want to continue playing (y or n)?")
    if play_again.lower() == "y":
        return True
    elif play_again.lower() == "n":
        return False


def main():
    display_menu()
    player_wins = 0
    cpu_wins = 0
    tie = 0
    new_game = True
    while new_game:
        player = get_player_choice()
        cpu = get_computer_choice()
        game = play_round(player, cpu)
        if game == 1:
            player_wins += 1
        elif game == -1:
            cpu_wins += 1
        elif game == 0:
            tie += 1
        new_game = continue_game()
    print("\nYou won", player_wins, "game(s)")
    print("The computer won", cpu_wins, "game(s)")
    print("You tied with the computer", tie, "times(s).")
    print("\nThank you for playing. Rock on!")


# ------------------------------------------------CALL FUNCTIONS----------------------------------------------------- #

main()
