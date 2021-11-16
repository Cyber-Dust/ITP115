# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# LAB 6
# Week 6 Notes

# .append()
ice_cream = ["vanilla", "chocolate", "strawberry"]
print(ice_cream)
ice_cream.append("mint") # appends to the end
print(ice_cream)
ice_cream.append("The Tonight Dough")

# .insert()
ice_cream.insert(0, "cookies & cream") # adds cookies and cream at the 0 index
print(ice_cream)

# .sort()
print("\nsort")
ice_cream.sort() # sorts with "The Tonight Dough" first b/c capital before lowercase
print(ice_cream)

# .count()
print("\ncount")
num = ice_cream.count("co")
print("num =", num)
num_mint = ice_cream.count("mint")
print("num_mint =", num_mint)
if "mint" in ice_cream:
    position = ice_cream.index("mint")
    print("mint is at index", position)

# remove - using a value
print("\nremove using a value")
ice_cream.remove("mint")


print("\nremove based on an index")
first_item = ice_cream.pop(0)
print("first item =", first_item)
print(ice_cream)

# del is a reserved word in Python
del ice_cream[0]
print(ice_cream)

#--------------------------------------LAB 6---------------------------------------------#

# ANAGRAMS AND PALINDROMES

# anagram
# get 2 words from user
word1 = input("Enter word #1: \n > ")
word2 = input("Enter word #2: \n > ")

# change the words to lower case
# strings are immutable
word1 = word1.lower()
word2 = word2.lower()

# remove whitespace from beginning and end
word1 = word1.strip()
word2 = word2.strip()

# anagram = all letters are the same
# convert words to lists, alphabetize, & compare
list1 = list(word1)
list2 = list(word2)
list1.sort()
list2.sort()

# compare lists
if list1 == list2:
    print("the words ARE anagrams.")
else:
    print("the words are NOT anagrams.")

# palindrome
# get a phrase from the user
phrase = input("Enter a phrase: \n > ")

# convert to all lowercase
phrase = phrase.lower()

# remove spaces using str.replace(find_str, replace_str)
phrase = phrase.replace(" ", "") # how does this happen? Q for OH

# convert string to a list
phrase_list = list(phrase)

# reverse the list
phrase_list.reverse()

# convert the list into a a string
# new_str = sep.join(list)
sep = "" # empty string
phrase_reverse = sep.join(phrase_list)

# compare the 2 strings
if phrase == phrase_reverse:
    print("the phrase IS a palindrome!")
else:
    print("the phrase is NOT a palindrome!")
