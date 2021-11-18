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


# Define the addAlbum(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: None
# o Get input from the user for the name of the artist and the name of the album
# that they want to add.
def add_album(dictionary="musicLibrary.dat"):
    artists = MusicLibraryHelper.loadLibrary(dictionary)
    new_artist = input("Enter Artist: ").title()
    new_album = input("Enter Album: ").title()
    # if artists is in dictionary, add album to the existing list of albums
    if new_artist in artists:
        artists.append(new_album)
    #     if new_album in artists:
    # elif new_artist not in artists:
    print(artists)
    # if the album exists, then do not add it
    # if artist is not in the dictionary. add a new key (artists), add new value(list containing the album)


def generate_random_playlist(dictionary="musicLibrary.dat"):
    library = MusicLibraryHelper.loadLibrary(dictionary)
    print("Here is your random playlist: \n")
    for key in library:
        print(random.choice(library[key]), "by", key)


def main():
    new_game = input("Choice: ")
    while new_game != "g".lower():
        display_menu()
        if new_game == "a":
            display_library()
        elif new_game == "b":
            display_artists()
        # elif new_game == "c":
        #     add_album()
        # elif new_game == "d":
        # elif new_game == "e":
        elif new_game == "f":
            generate_random_playlist()
        # elif new_game == "g":
    # new_library = input("Enter music library filename: ") 
    # new_library = MusicLibraryHelper.saveLibrary(new_library) # how do you do this? 
    # # the dictionary representing the music library
    # print("Saved music library to ", new_library)


display_library()
display_artists()
generate_random_playlist()
add_album()
