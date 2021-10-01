# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 5


#-----------------------------WELCOME TO THE SENTENCE GENERATOR---------------------------------#
# In this assignment, we will be building a random sentence generator using the alphabet. After
# the sentence is entered, the program outputs the number of special characters used and prints
# out an alphabetical list displaying each letter in a row. NONE is used if there is no asterisks
# present.
# This program uses:
# range-based for loop.
# inputs
# loop using a string variable
# STEPS



import random

# create variable that contains all letters of the alphabet
# letter = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

# get input from user
user = input("Enter a sentence: ")

# count the # of special characters that are not in the alphabet and not spaces\
# for special in user:
#     if "a" or "A" in special:
#         print("a: ")
#     elif "b" or "B" in special:
#         print("b ")

# create a variable and use a for loop to loop through user input !USE BRANCHING!
counter = 0
for i in user:
    letter = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    if i.lower() not in letter:
        counter += 1
    elif user == "B" or "b":
        counter += 1
    elif user == "C" or "c":
        counter += 1
    elif user == "D" or "d":
        counter += 1
    elif user == "E" or "e":
        counter += 1
    elif user == "F" or "f":
        counter += 1

# Print out the number of special characters using asterisks
print("Special Character: " + (counter * "*"))
# Use multiplication operator with a string and number to repeat the string

# if no special characters print out none

