# Dasean Volk, dvolk@usc.edu
# Assignment 4
# Description: a program that allows the user to enter an unknown amount of numbers. The
# user will signal that they are done entering numbers by entering -1. The program will
# determine the smallest number entered and largest number entered by using variables
# and branching.

# variables that will hold the smallest number, largest number, count,
# sum, and the number the user will enter
user = " "
count = 0
sum = 0

# create do while loop first,set variables
while 
# displays instruction to user
print("\nInput an integer greater than or equal to 0 (-1 to quit):")

# while loop that ends when the user enters a -1, getting input with a >
while user != -1:
    user = int(input("> "))
    if count == 0:
        smallNum = user
        largeNum = user
    else:
        if user > largeNum:
            largeNum = user
        elif user < smallNum:
            smallNum = user
    sum = sum + user
    count = count + 1


print(sum)
print(count)


again = input("Would you like to enter another set of numbers (y/n)?")
if again == "y" or again == "Y":

else:
    print("Goodbye!")
#NEED TO FIND AVERAGE AND PRINT, CREATE DO WHILE LOOP
