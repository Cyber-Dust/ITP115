# Dasean Volk, dvolk@usc.edu
# Week X Notes

#-------------------------------------------FUNCTIONS PT2-------------------------------------------------#

# Functions

# Immutable Variables = not affeced by changes in the function

# a list is mutable when you use methods like append() or sort()


# import modules

# global constants ///
# constant means dont change the value
# global means acessible to the whole file, even inside of functions
# convention = all upper case with underscore
# examples:

SCHOOL = "USC"
COURSE_NUM = 115

#---------------------------DEFINE FUNCITONS----------------------------#

# function: 
# parameter 1: str
# parameter 2: int
# return value: 
# side effect: 

#-----------------------------------------------------------------------#

# function: vote
# parameter 1: name is a string(str)
# parameter 2: age is an int with a default of 18
# return value: a string with a message saying wheter the person can vote
# side effect: None

def vote(name, age=18):
  # create a variable for the return value
  # msg is a local variable that only exists in this function
  msg = name + ", you can vote!"
  if age < 18:
    msg = name + ", you are " + str(age) + " and not old enough to vote."
  # return keyword exits a function and instructs Python to continue executing the main program
  return msg

# function: sortList
# parameter: itemList is a list of strings
# return value: None
#side effect: sorts the list
def sortList(itemList):
  #list.sort()
  # lists are mutable
  itemList.sort()
  
# function: addItem
# parameter 1: elementList is a list
# parameter 2: newItem
# return value: None
# side effect: adding newItem to elementList
def addItem(elementList, newItem):
  elementList.append(newItem)
  
  
  
# main is the starting point of the program
def main():
  print("List Example")
  # create a list
  food = ["chicken parm", "pizza", "rolled tacos"]
  print(food)
  print("call sortList")
  sortList(food)
  print(food)
  print("call addItem")
  addItem(food, "burger")
  
  # vote test
  print("\Calling vote function")
  results = vote("Dasean", 25)
  print(results)
  
main()


