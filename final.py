# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Final Project
# tasks.py
# Description:

# interface, tasks and main module will be uploaded on:
# January 6, 2022

# import interface
import interface

# Define the createListOfParks() function.
# • Parameter: fileName is the name of the CSV file to read and it has a default
# value of "national_parks.csv"
# • Return value: a list of dictionary objects where the keys are the strings from
# the header row and the values are the information from the rest of the CSV
# file



def create_list_of_parks(file_name):
    list = []
    fin = open(file_name, "r")
    header = fin.readline()
    header = header.strip()
    for line in header:
        line = line.strip()
        parks_list = line.split(",")

    print(header)

# def get_date(data_str):

def display_menu(menu_dict):
    interface.get_menu_dict()


def main():
    parks = "national_parks.csv"
    display_menu(menu_dict=interface)
    create_list_of_parks(parks)

main()




# def get_date(data_str, ):
