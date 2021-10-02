# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 5


#-----------------------------WELCOME TO THE ALPHABET ITERATOR---------------------------------#
# In this assignment, we will be building a random sentence iterator using the alphabet. After
# the sentence is entered, the program outputs the number of special characters used and prints
# out an alphabetical list displaying each letter used in a row. NONE represents no letter or
# special characters present. * is the indication of how many times a letter or special character
# is present.

# This program uses:
# range-based for loop.
# inputs
# loop using a string variable
# STEPS

# a range based loop that takes in how many times it wants to run the characters input
print("Character Distribution")
userruns = int(input("Enter the number of times to run: "))

for num in range(userruns):
# create variable that contains all letters of the alphabet
# this is a string not an integer, so we use ""
    abc = "abcdefghijklmnopqrstuvwxyz"
# variable used later to increment the number of characters not in the alphabet, set to 0
    special = 0
# get input from user
# the .lower() at the end of the input allows us to not include the method in our if statements!
    user = input("\nEnter a sentence: ").lower()


    # count the # of special characters that are not in the alphabet and not spaces
    for letter in user:
        if letter not in abc and letter != ' ':
            # increments the number of characters not in the alphabet
            special = special + 1
    if special is 0:
        print("Special Characters: NONE")
    else:
        # multiply the number of special characters variable using asterisks
        print("Special Characters: " + "*" * special)

    # this for-loop will print out a range of a-z vertically
    for letter in abc:
        # variable for number of times a letter occurs set at 0
        abcVariable = 0
        for character in user:
            # if the letter variable is in the abc variable
            if letter == character:
                # increment the number of times a letter is used
                abcVariable = abcVariable + 1
        if abcVariable is 0:
            print(letter + ": NONE")
        else:
            # multiply the number of letter uses times the updated abcVariable
            print(letter + ": " + "*" * abcVariable)



