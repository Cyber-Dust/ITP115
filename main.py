# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 2

# This program creates a Mad Libs story.
# It gets input from the user and prints output.

# list of variables for mad  lib story, line 15 adds a 1 to whatever number is entered.
noun = input("Enter a movie title: ")
noun2 = input("Enter another movie title: ")
verb = input("Enter a verb ending in 'ing': ")
color = input("Enter a color: ")
automobile = input("Enter the make of a car (plural): ")
number1 = int(input("Enter a number: ") + str(1))
number2 = int(input("Enter a second number: "))
number3 = int(input("Enter a third number: "))
decimal = float(input("Enter a temperature with a decimal: "))

# Multiplies inputs number2 and 3 on line 23
# Whatever decimal is entered on line 25, it adds 10 to it
print("This weekend, me and my friend went to see " + "\"" + noun + "\"" + ".")
print("On the way to the theater, we saw " + "\"" + str(number1) + "\"" + " " + "\"" + color + "\"" + " " + "\"" + automobile + "\"" + ".")
print("At the movie, we bought " + "\"" + str(number2 * number3) + "\"" + " packages of candy and " + "\"" + str(number3) + "\"" + " large sodas.")
print("Although the temperature in the theater was " + "\"" + str(decimal + 10) + "\"" + " Fahrenheit, we were " + "\"" + verb + "\"" + " the whole way through.")
print("The movie was not too bad, but I think " + "\"" + noun2 + "\"" + " looked better.")
