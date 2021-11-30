
# Dasean Volk, dvolk@usc.edu
# Fall 2021, ITP115
# Section: Boba
# Final Project

# ----------------------------------------------WELCOME TO THE FINAL-------------------------------------------------- #

# use the "nationalparks.csv"
# .csv files = comma serperated values

# finish this by december 10

# Parameter: fileName is the name of the CSV file to read and it has a default
# value of "national_parks.csv"
# • Return value: a list of dictionary objects where the keys are the strings from
# the header row and the values are the information from the rest of the CSV file

def create_list_of_parks(file_name):
    list = []
    fin = open(file_name, "r")
    header = fin.readline()
    print(header)

def main():
    parks = "national_parks.csv"
    create_list_of_parks(parks)

main()
