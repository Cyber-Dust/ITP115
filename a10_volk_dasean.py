# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 10
# Description:

# ------------------------------------WELCOME TO THE MUSIC LIBRARY GENERATOR----------------------------------------- #

# The program uses a .dat file with a list of albums by Adele, the Beatles, and The Who. First, a display menu appears
# which allows you to choose to display the library or the artists, add an album/artist to the library, delete an
# album or delete an artist. Lastly, the program allows you to generate a random playlist. Once g is chosen for
# exit, the program saves your altered library to a new file (make sure to put .dat at the end of your new file name).
# Boom: You have curated, mangled and generated a file of musicians and their albums, all using python dictionaries.

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
          "\n   a) Display library"
          "\n   b) Display artists"
          "\n   c) Add an artist/album"
          "\n   d) Delete an album"
          "\n   e) Delete an artist"
          "\n   f) Generate a random playlist"
          "\n   g) Exit")


# Define the displayLibrary(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: None


def display_library(dictionary):
    # ctrl + alt + l to auto indent
    for key in dictionary:
        print("Artist:", key, "\n   Albums:  ")
        value = dictionary[key]
        for keys in value:
            print("    ", keys)
        # need to get the [] removed from the values and display them horizontally?


# Define the displayArtists(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: None
# o Print out the artists in the music library


def display_artists(dictionary):
    print("Artists: ")
    for i in dictionary:
        print("  ", i)
        
        
# Define the addAlbum(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: None
# o Get input from the user for the name of the artist and the name of the album
# that they want to add.


def add_album(dictionary):
    new_artist = input("Enter Artist: ").title()
    new_album = input("Enter Album: ").title()
    # if artists is in dictionary, add album to the existing list of albums
    if new_artist in dictionary:
        if new_album not in dictionary:
            dictionary[new_artist].append(new_album)
    #     if new_album in artists:
    #     if new_album in artists: # how do I NOT add something?
    # elif new_artist not in artists:
    elif new_artist not in dictionary:
        dictionary[new_artist] = [new_album]
        # along with the new value
    # print(dictionary)
    # if the album exists, then do not add it
    # if artist is not in the dictionary. add a new key (artists), add new value(list containing the album)


# Define the deleteAlbum(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: a boolean value - True if an album was successfully deleted, or
# False if the album was not successfully deleted


def delete_album(dictionary):
    artist = input("Enter artist: ").title()
    album = input("Enter album: ").title()
    if artist in dictionary:
        for key in dictionary:
            value = dictionary[key]
            if album in value:
                dictionary[artist].remove(album)
                return True
    elif artist not in dictionary or album not in dictionary:
        return False


# Define the deleteArtist(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: a boolean value - True if an artist was successfully deleted, or False
# if the artist was not successfully deleted


def delete_artist(dictionary):
    artist = input("Enter artist to delete: ").title()
    if artist in dictionary:
        del dictionary[artist]
        return True
    elif artist not in dictionary:
        return False


def generate_random_playlist(dictionary):
    print("Here is your random playlist:")
    for key in dictionary:
        # add "   " for space accuracy (tab)
        print("   " + random.choice(dictionary[key]), "by", key)


def main():
    library = "musicLibrary.dat"
    music_library = MusicLibraryHelper.loadLibrary(library)
    # do while loop to display menu until you exit
    music_generator = True
    while music_generator:
        print()
        display_menu()
        new_game = input("Choice: ").lower()
        if new_game == "a":
            display_library(music_library)
        elif new_game == "b":
            display_artists(music_library)
        elif new_game == "c":
            add_album(music_library)
        elif new_game == "d":
            delete_one = delete_album(music_library)
            if delete_one:
                print("Delete album success")
            else:
                print("Delete album failed")
        elif new_game == "e":
            delete = delete_artist(music_library)
            if delete:
                print("Delete artist success")
            else:
                print("Delete artist failed")
        elif new_game == "f":
            generate_random_playlist(music_library)
        elif new_game == "g":
            music_generator = False
            new_library = input("Enter music library filename: ")
            MusicLibraryHelper.saveLibrary(new_library, music_library)
            print("Saved music library to", new_library)
            # UNCOMMENT below to view your new library since you are not allowed to see it in the .dat file:
            # new = MusicLibraryHelper.loadLibrary(new_library)
            # print(new)
        else:
            print("Invalid entry")


main()
