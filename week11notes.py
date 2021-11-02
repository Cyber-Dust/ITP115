# Dasean Volk, dvolk@usc.edu
# Week 11
# Section: Boba
# Files

# Read a text file

# Reading is a 3-step process
# 1. open the file returns a file object (new variable type)
# 2. read data from the file (strings, line by line)
# 3. close the file object

# function: read_file
# parameter: file_name is a string that is the name of the file to read
# return value: none
# read names and then print out in the following format: last, first

import random


def read_file(filename):
    file_in = open(filename, "r")
    for line in file_in:
    # line is a string
    # remove the new line at the end
        line = line.strip()
        # print(line)

        # print the name: last, first
        # list = str.split(sep)
        # .split() default is whitespace
        items = line.split(", ")
        print(items)
    file_in.close()

# funciton: read_movie_data
# parameter: file_name with a default value of FavoriteStreamingMovies.csv
# return value: a list of movies recommended by students
# creates a list of movies recommended by students
def read_movie_data(filename="FavoriteStreamingMovies.csv"):
    file_obj = open(filename, "r")
    # header row
    file_obj.readline()

    # create and empty list
    movies = []
    for line in file_obj:
        line = line.strip() # get rid of \n
        data = line.split(",")
        teacher = data[4]
        teacher = teacher.strip("\"")
        print("teacher =", teacher)
        if teacher == "Trina Gregory":
            movie = data[5]
            print("movie =", movie)
            movie = movie.strip("\"") # includes the movies with the ""
            if movie not in movies:
                movies.append(movie)

    file_obj.close()
    return movies

def main():
    film = read_movie_data()
    print(film)
    for title in film: # prints recommended movies in a row
        print(title)
    print()
    random_movie = random.choice(film)
    print("Your recommended movie is", random_movie)
    print()
    read_file("names.txt")

main()


# saving a CSV
# right click on link and click "save link as"
