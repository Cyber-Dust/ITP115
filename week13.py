# Week 13
# Boba Class

# OOP = object-oriented programming
# define a class (blueprint or template) - only define once
# crete objects from the class
# classes are made up of attributes (var) and behaviors (methods)
# methods are functions defined inside of a class

# class: Movie
# required attributes: title, year
# attributes: genre, length/runtime, cast, rating
class Movie:
    def __init__(self, title, year):
        # create attributes
        self.title = title
        self.year = year
        self.genre = ""
        self.length = 0 # in min
        self.rating = "NR"
        
    def __str__(self):
        # must return a string
        info = self.title + " (" + str(self.year) + ")"
        if self.genre:
            info += "\n\tGenre: " + self.genre
        if self.rating != "NR":
            info += "\n\tRating: " + self.rating
            
        return info
      
def main():
  print("It's Movie Time!")
  # create movie objects
  
  print("Dasean's favorite movie")
  dasean = Movie("Drive", 2011)
  dasean.genre = "Crime Drama"
  dasean.rating = "R"
  print(dasean)
  
main()
