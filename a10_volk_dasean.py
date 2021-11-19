# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 10
# Description:

# ------------------------------------WELCOME TO THE MUSIC LIBRARY GENERATOR----------------------------------------- #

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
        artists[new_artist].append(new_album)
    #     if new_album in artists:
    #     if new_album in artists: # how do I NOT add something?
    # elif new_artist not in artists:
    elif new_artist not in artists:
        artists[new_artist] = [new_artist].append(new_album)
        # along with the new value
    print(artists)
    # if the album exists, then do not add it
    # if artist is not in the dictionary. add a new key (artists), add new value(list containing the album)

# Define the deleteAlbum(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: a boolean value - True if an album was successfully deleted, or
# False if the album was not successfully deleted


def delete_album(dictionary="musicLibrary.dat"):
    music_library = MusicLibraryHelper.loadLibrary(dictionary)
    artist = input("Enter artist: ").title()
    album = input("Enter album: ").title()
    if artist in music_library and album in music_library:
        del music_library[album]
        return True
    elif artist not in music_library and album not in music_library:
        return False
    # return true or false

# Define the deleteArtist(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: a boolean value - True if an artist was successfully deleted, or False
# if the artist was not successfully deleted


def delete_artist(dictionary="musicLibrary.dat"):
    music_library = MusicLibraryHelper.loadLibrary(dictionary)
    artist = input("Enter artist to delete: ").title()
    if artist in music_library:
        del music_library[artist]
        return True
    elif artist not in music_library:
        return False

def generate_random_playlist(dictionary="musicLibrary.dat"):
    library = MusicLibraryHelper.loadLibrary(dictionary)
    print("Here is your random playlist:")
    for key in library:
        # add "   " for space accuracy (tab)
        print("   " + random.choice(library[key]), "by", key)


def main():
    display_menu()
    new_game = input("Choice: ")
    # while new_game != "g".lower():
    if new_game == "a":
        display_library()
    elif new_game == "b":
        display_artists()
    elif new_game == "c":
        add_album()
    elif new_game == "d":
        delete_album()
        if True:
            print("Delete album success")
        elif False:
            print("Delete album failed")
    elif new_game == "e":
        delete_artist()
        if True:
            print("Delete artist success")
        elif False:
            print("Delete artist failed")
    elif new_game == "f":
        generate_random_playlist()
        # elif new_game == "g":
    # new_library = input("Enter music library filename: ")
    # MusicLibraryHelper.saveLibrary(new_library, ) # how do you do this?
    # # the dictionary representing the music library
    # print("Saved music library to ", new_library)
    else:
        print("Invalid entry")
    print()
    display_menu()
    



# display_library()
# display_artists()
# generate_random_playlist()
# add_album()
main()



