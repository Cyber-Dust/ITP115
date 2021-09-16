# Week 4, ITP 115
# Dasean Volk, dvolk@usc.edu

# num = int(input("Enter a number: "))
# while num != 16:
#     print("Wrong! Please try again!")
#     num = int(input("Enter another number: "))
# print("You did it!")

# Lab 3

# while loop
answer = ""

# What condition causes us to stop looping?
while answer != "q" or answer != "Q":
    # PRINT MENU
    print("\nWhat would you like to know?")
    print("a) Favorite Animal")
    print("c) Favorite Color")
    print("f) Favorite Food")
    print("q) Quit")
    answer = input("> ")

    if answer == "a" or answer == "A":
        print("My favorite animal is a Penguin.")
    elif answer == "c" or answer == "C":
        print("My favorite color is Blue.")
    elif answer == "f" or answer == "F":
        print("My favorite food is Chinese Food.")
    elif answer == "q" or answer == "Q":
        print("Goodbye")
    else:
        print("Please enter a valid letter.")
