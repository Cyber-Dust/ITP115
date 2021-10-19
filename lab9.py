# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Lab 7

#--------------------------------------WELCOME TO THE SHAPE PRINTER--------------------------------------#

# define functions

# function: print_rect
# parameter 1: length is an int for the height of the rectangle
# parameter 2: width is an int for the width of the rectangles
def print_rect(length, width):
  # use - & |
  print(" " + "-" * width)
  for line in range(length):
    print("|" + " " * width + "|")
  
  print(" " + "-" * width)
  
# function: print_square
def print_square(size):
  print_rect(size, size)
  
# define main
def main():
# testing
#   print_rect(5, 3)
#   print_square(4)
  print("Welcome to the Shape Printer!")
  print("R) Rectangle")
  print("S) Square")
  shape = input("Enter the shape you want to print: ")
  if shape.lower() == "r":
    user_length = int(input("Enter the length: "))
    user_width = int(input("Enter the width: "))
    print_rect(user_length, user_width)
  elif shape.lower() == "s":
    user_size = int(input("Enter the size: "))
    print_square(user_size)
  else:
    print("That shape is not supported.")
    
# call main 
main()
