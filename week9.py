# Dasean Volk, dvolk@usc.edu
# Section: Boba
# Week 9 Notes

# import modules needed
import random

# FUNCTIONS
# enables reusable code
# cleaner code
# break up code into managable tasks

# Conventions:
# use snake_case

# Steps:
# 1. define the function
# 2. 

# create functions
def birthday(name):
  print("Happy birthday to you")
  print("Happy birthday to you")
  print("Happy birthday, dear", name)
  print("Happy birthday to you")
  
# function: health_tip
# parameters: None
# prints a random health tip
def health_tip():
  num = random.randrange(0, 5)
  if num == 0:
    print("Eat fruit")
  elif num == 1:
    print("Drink lots of water")
  elif num == 2:
    print("Wear a mask")
  elif num == 3:
    print("Brush your teeth")
  else:
    print("Get exercise")
  
# calling functions
print("Birthday")
birthday()
print("\nHealth Tips")
want_tip = "y"
while want_tip.lower() == "y":
  health_tip()
  want_tip = input("Do you want another tip (y or n)? ")
