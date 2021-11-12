# Dasean Volk, dvolk@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 9
# Description:


# Define the getLanguages(fileName) function.
# o Parameter: fileName is a string containing the name of a CSV file to read from
# and it has a default value of "languages.csv"
# o Return value: a list of strings representing the languages in the header row

def get_languages(file_name="languages.csv"):
    # open the file
    languages = open(file_name, "r")
    header = languages.readline()
    languages.close()
    return header

# Define the getTranslationLanguage(langList) function.
# o Parameter: langList is a list of the languages
# o Return value: a string for the language to translate words into

def get_translation_language(lang_list):
    lang_list = ["Danish", "Dutch", "Finnish", "French", "German", "Indonesian", "Italian",
                "Japanese", "Latin", "Norwegian", "Portuguese", "Spanish", "Swahili", "Swedish"]
    print("Translate English words to one of the following languages:\n", lang_list)
    lang = input("Enter a language: ").lower()
    if lang != lang_list:
        print("This program does not support", lang)
        lang = input("Enter a language: ").lower()
    return lang.capitalize()

# Define the readFile(langList, langStr, fileName) function.
# o Parameter 1: langList is a list of the languages
# o Parameter 2: langStr is a string of containing the name of a language and it has
# a default value of "English"
# o Parameter 3: fileName is a string containing the name of a CSV file to read from
# and it has a default value of "languages.csv"
# o Return value: a list of words in the language identified by the langStr parameter

def read_file(lang_list, lang_str, file_name="languages.csv"):
    lang_str = []
    fin = open(file_name, "r")
    header_line = fin.readline()
    for line in fin:
        line = line.strip()
    data_list = line.split(",")
    print(data_list)
    fin.close()

# Define the createResultsFile(language) function.
# o Parameter: language is a string containing the name of the language for
# translation
# o Return value: None


def create_results_file(language):
    name_file = language + ".txt"
    out_file = open(name_file, "w")
    for translation in language:
        print("Words translated from English to", language)
        print(translation, file=out_file)
    out_file.close()

# Define the translateWords(englishList, translationList, language) function.
# o Parameter 1: englishList is a list of words in English
# o Parameter 2: translationList is a list of words in another language (not English)
# o Parameter 3: language is a string containing the language of the words in the
# translationList
# o Return value: none

# def translate_words(english_list, translation_list, language):
    



# 
# def main():
#     print("Language Translator")





















# def get_languages():
#     file_in = open("languages.csv", "r")
#     for line in file_in:
#         word = line.strip()
#     print(word)
#     file_in.close()
#
# def get_translation_language(lang_list):
#     lang_list = ["Danish", "Dutch", "Finnish", "French", "German", "Indonesian", "Italian",
#           "Japanese", "Latin", "Norwegian", "Portuguese", "Spanish", "Swahili", "Swedish"]
#     print("Translate English words to one of the following languages:\n"
#           "Danish Dutch Finnish French German Indonesian Italian\n"
#           "Japanese Latin Norwegian Portuguese Spanish Swahili Swedish")
#     lang = input("Enter a language: ")
#     if lang != lang_list:
#         print("This program does not support", lang)
#         lang = input("Enter a language: ")
#
# def read_file(lang_list, lang_str, file_name="languages.csv"):
#     list = []
#     fin = open(file_name, "r")
#     header_line = fin.readline()
#     for line in fin:
#         line = line.strip()
#     data_list = line.split(",")
#     print(data_list)
#     fin.close()
#
# def create_results(language):
#     # create variable for results txt file
#     language = ""
#     name_file = language + ".txt"
#     out_file = open(name_file, "w")
#     for file in language:
#         print("Words translated from English to", language)
#
# def translate_words(english_list, translation_list, language):
#     english_list = ""
