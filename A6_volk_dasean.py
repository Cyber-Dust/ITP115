# Dasean Volk, dvolk@usc.edu
# Assignment 6
# Description: xx
#-----------------------------------------WELCOME TO THE JUMBLED WORD GUESSING GAME------------------------------------#
# This program asks the user to interpret a jumbled word from a list of strings. If the user cannot faithfully guess,
# the program will ask the user for a corresponding hint. Once the user guesses the correct word, the program will
# congratulate the user and display how many times it took them to guess the word.
#444
#begin python advanced starting monday
# import the random module
import random

# create 2 lists that 1. contains words and 2. contains the hints for those words
user = "" # do while empty variable
words = ['love', 'movie', 'car', 'video game']
hints = ['a warm and fuzzy feeling', 'motion pictures', 'an engine and four wheels', 'people play these digitally']

# get random word with the corresponding hint and put them into a variable

random_word = random.choice(words)

position = words.index(random_word)

word_list = list(random_word)

jumbled_word = "" # create empty string to hold the jumbled word

# loop through the list while it has elements
# create a jumbled word
while len(word_list) > 0:
    element = random.choice(word_list)
    jumbled_word = jumbled_word + element
    word_list.remove(element)
print("The jumbled word is:", jumbled_word)

count = 0
# have the user guess the word until they get it correct, using a loop
while user != random_word:
    user = input("Enter your guess: ")
    if user != random_word:
        print("That is not correct.")
        hint = input("\n Would you like a hint (y or n)?").lower() # if the guess is incorrect, ask if they want a hint
        if hint == "y":
            print("The hint is", hints[position]) # give them the hint
        else:
            print("The jumbled word is", jumbled_word)
    count += 1 # count the number of guesses
# if correct, print the number of guesses
print("Congratulations!! You got it! \n It took you", count, "attempts")
