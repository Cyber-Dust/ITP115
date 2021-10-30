# Dasean Volk, dvolk@usc.edu
# Fall 2021, ITP115
# Section: Boba
# Lab 8

#---------------------------------------COIN FLIPPING----------------------------------------#

import random

# function: coin
def coin():
  flip = "heads"
  random_num = random.randrange(0, 2)
  if random_num == 1:
    flip = "tails"
  return flip

# alternative method

# return random.choice(["heads", "tails"])

# function: expirement
def expirement():
  # local variable
  flips = 0
  heads = 0
  while heads < 3: # or !=
    coin_flip = coin()
    flips += 1
    # branching
    if coin_flip == "heads":
      heads += 1
    else:
      heads = 0
    
  
  return flips

def main():
  # average = total / num
  total = 0
  num_runs = 10 
  # run the expirement 10 times
  for count in range(num_runs):
    num_flips = expirement()
    total += num_flips
    
    
  average = total/num_runs
  print("The average for 3 heads in a row is", average)
  
main()
