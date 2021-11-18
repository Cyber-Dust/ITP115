# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 10
# Description:

# import music library helper file
import MusicLibraryHelper

# import random module
import random


# Define the displayMenu() function.
# o Parameter: None
# o Return value: None
# o Print out the menu options to the user:
def display_menu():
    print("Manage Your Music Library"
          "\na) Display library"
          "\nb) Display artists"
          "\nc) Add an artist/album"
          "\nd) Delete an album"
          "\ne) Delete an artist"
          "\nf) Generate a random playlist"
          "\ng) Exit")


# Define the displayLibrary(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: None
def display_library(dictionary="musicLibrary.dat"):
    library = MusicLibraryHelper.loadLibrary(dictionary)
    # ctrl + alt + l to auto indent
    for key in library:
        print("Artist:", key, "\n   Albums:  ")
        value = library[key]
        for keys in value:
            print("    ", keys)
        # need to get the [] removed from the values and display them horizontally?


# Define the displayArtists(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: None
# o Print out the artists in the music library
def display_artists(dictionary="musicLibrary.dat"):
    artists = MusicLibraryHelper.loadLibrary(dictionary)
    print("Artists: ")
    for i in artists:
        print("  ", i)

def main():
    display_menu()
    input("Choice: ")


display_library()
display_artists()
