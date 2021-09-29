# Dasean Volk, dvolk@usc.edu
# Section: Boba
# Week 6 Notes

#---------------------------------------SLICING--------------------------------------------#
# Slicing allows us to get multiple elements from a sequence
# when we slice a string, we get a substring
# syntax: variable[start_index : stop_index]
# stop_index is up to but not including
# Ex.)
print("\nSlicing")
msg = "Fight on!"
slice = msg[4:7]
print("slice =", slice)

# Using [:] we can slice the parameters in a sequence
# Ex.)
message = "Visit USC"
slice = message[3:7]
print(slice)

# Using strictly slice we only get the one character in the index
# Ex.)
slice = message[2]
print(slice)

#------------------------------------STRING PROCESSING---------------------------------------#
# strings are sequences = they have order

# access an element by using an index
# index is an integer; position number
# stars at 0; ends at len(variable)

print("\nLove me")
msg = "I can do that"
letter = msg[3]
print("letter at index 3 =", letter)
print("length =", len(msg))

# how to establish last and first letter
first_letter = msg[0]                # establish the first letter index =  msg[0]
print("first letter=", first_letter)
last_letter = msg[len(msg)-1]        # establish the last letter index = len(msg) - 1
print("last letter =", last_letter)

# how to create and print out a new message with the first and last letter swapped
print("\nI love the band the Doors")
msg = input("Enter a message: ")
msg = msg.lower()
first_letter = msg[0]
last_letter = msg[len(msg) - 1]
middle = msg[1:len(msg) - 1]
swapped = last_letter + middle + first_letter
print("Swapped =", swapped)


#-----------------------------------STRING METHODS----------------------------------------#
print("\nString Methods")

# string.isalum()
# string.isalpha()
# string.isdigit()
# string.is...
# LOOK THIS UP AND STUDY DIFFERENT METHODS..WHAT EXACTLY DO EACH OF THESE DO

#---------------------------------------LISTS---------------------------------------------#



# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Lab 5

# import random module
import random

# Create 3 lists
nouns =["Chalkboard", "Macbook", "Lamborghini", "Chair"]
verbs =["Walking", "Computing", "Roaring", "Dancing"]
articles = ["a", "an", "the"]

print("Welcome to the Sentence Generator")

# while loop - execute at least once
choice = 0
while choice != 5:
    # print menu
    print("Menu")
    print("1) View Words")
    print("2) Add Noun")
    print("3) Remove Verb")
    print("4) Generate Sentence")
    print("5) Exit")

    # get user input that is an integer
    choice = int(input("> "))

    # use branching
    if choice == 1:
        # view words
        print("articles:", articles)
        print("nouns:", nouns)
        print("verbs:", verbs)
    elif choice == 2:
        # add noun
        new_noun = input("Enter a noun: ")
        nouns.append(new_noun)
    elif choice == 3:
        # remove verb
        bad_verb = input("Enter a verb: ")
        if bad_verb in verbs:
            verbs.remove(bad_verb)
            print("verbs:", verbs)
        else:
            print(bad_verb, "is not in the list of verbs")
    elif choice == 4:
        # generate a sentence
        # ARTICLE NOUN VERB ARTICLE NOUN
        art1 = random.choice(articles)
        art2 = random.choice(articles)
        noun1 = random.choice(nouns)
        noun2 = random.choice(nouns)
        verb_random = random.choice(verbs)
        print(art1, noun1, verb_random, art2, noun2)
    elif choice == 5:
        print("Thank you for using the Sentence Generator")
    else:
        print ("Invalid choice.")
