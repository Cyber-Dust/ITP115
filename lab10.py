# Dasean Volk, dvolk@usc.edu
# Fall 2021, ITP 115
# Section: Boba
# Lab 10

# function: read_file
# parameter: file_name w a default value of story.txt
# return value: dictionary where keys are words (strings) and values are lists with line #'s (int)
def read_file(file_name="story.txt"):
    # create a dictionary
    words_dict = {}

    # open file
    file_in = open(file_name, "r")

    # create a var for line number
    line_num = 1
    # read the file ovbj and loop thru each line
    for line in file_in:
        line = line.strip()
        line_list = line.split() # whitespace
        # line_list = a list of words
    # loop thru each word in the line
        for word in line_list:
            # lower the word
            word = word.lower()
            # get rid of punctuation
            word = word.strip(".,;:?'")

            # add word to dictionary
            if word in words_dict:
                    # update the value by appending the line number
                words_dict[word].append(line_num)
            else: # not in dict
                # add the word to the dict
                 # dict[key]
                words_dict[word] = [line_num]
            # after the 'for word' loop
            # update the line #
        line_num += 1

    file_in.close()

    # return dictionary
    return words_dict

# function: sort_keys
# parameter: dictionary
# return value: a list of sorted keys from dictionary
def sort_keys(dictionary):
    keys = dictionary.keys()
    keys_list = list(keys)
    keys_list.sort()
    return keys_list

def main():
    story_dict = read_file()
    story_keys = sort_keys(story_dict)
    print("Here's the concordance.")
    # use the list of sorted keys for printing
    for key in story_keys:
        print(key + ":", story_dict[key])

main()
