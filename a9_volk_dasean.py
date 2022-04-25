# Dasean Volk, dvolk@usc.edu
# Assignment 9
# Description:

# ----------------------------------------------LANGUAGE TRANSLATOR-------------------------------------------------- #
# This program uses a list of languages from a .csv file and asks the user to enter a language they with to convert
# from English. Then the cpu ask the user to enter a word that they wish to translate, if the word is not in the
# english list it asks again. If there is no translation, it asks again. If there is a valid English word and
# corresponding translation, then there is a new .txt file created with all the translations.

# Define the getLanguages(fileName) function.
# o Parameter: fileName is a string containing the name of a CSV file to read from
# and it has a default value of "languages.csv"
# o Return value: a list of strings representing the languages in the header row

def get_languages(file_name="languages.csv"):
    # open the file
    languages = open(file_name, "r")
    header = languages.readline()
    header = header.strip()
    header_lang = header.split(",")
    languages.close()
    return header_lang


# Define the getTranslationLanguage(langList) function.
# o Parameter: langList is a list of the languages
# o Return value: a string for the language to translate words into

def get_translation_language(lang_list):
    list_of_lang = lang_list[1:15]
    print("Translate English words to one of the following languages:\n",
          "Danish", "Dutch", "Finnish", "French", "German", "Indonesian", "Italian\n",
          "Japanese", "Latin", "Norwegian", "Portuguese", "Spanish", "Swahili", "Swedish")
    lang = input("Enter a language: ").capitalize()
    while lang not in list_of_lang:
        print("This program does not support", lang.capitalize())
        lang = input("Enter a language: ").capitalize()
    return lang.capitalize()


# Define the readFile(langList, langStr, fileName) function.
# o Parameter 1: langList is a list of the languages
# o Parameter 2: langStr is a string of containing the name of a language and it has
# a default value of "English"
# o Parameter 3: fileName is a string containing the name of a CSV file to read from
# and it has a default value of "languages.csv"
# o Return value: a list of words in the language identified by the langStr parameter


def read_file(lang_list, lang_str="English", file_name="languages.csv"):
    # Create an empty list.
    list_of = []
    # o Open the CSV file and read the header row to skip it.
    fin = open(file_name, "r")
    header_line = fin.readline()
    # o Use the langList and langStr parameters to determine the index of the language.
    language_index = lang_list.index(lang_str)
    # o Loop through the rest of the file. Each line of data will have an extraneous new
    # line at the end
    for line in fin:
        line = line.strip()  # remove
        line = line.split(",")  # break up the line into a list of strings
        list_of.append(line[language_index])  # Get the correct word and append it to the list.
    fin.close()
    return list_of


# Define the createResultsFile(language) function.
# o Parameter: language is a string containing the name of the language for
# translation
# o Return value: None


def create_results_file(language):
    name_file = language + ".txt"
    out_file_1 = open(name_file, "w")
    print("Words translated from English to " + language, file=out_file_1)
    # print(language, file=out_file)
    out_file_1.close()


# Define the translateWords(englishList, translationList, language) function.
# o Parameter 1: englishList is a list of words in English
# o Parameter 2: translationList is a list of words in another language (not English)
# o Parameter 3: language is a string containing the language of the words in the
# translationList
# o Return value: none

def translate_words(english_list, translation_list, language):
    # open the results file
    name_file = language + ".txt"
    out_file = open(name_file, "a")
    continue_translator = "y"
    # ask user to enter an english word to translate

    while continue_translator.lower() == "y":
        enter = input("\nEnter a word to translate: ")
        if enter in english_list:
            indexed = english_list.index(enter)
            translation = translation_list[indexed] # Create these variables before looping

            if enter in english_list and translation != "-":
                print(enter, "is translated to", translation)
                print(enter, "=", translation, file=out_file) # write to the file
                continue_translator = input("Another word (y or n) ")

            elif enter in english_list and translation == "-":
                print(enter, "does not have a translation")
                continue_translator = input("Another word (y or n) ")
        elif enter not in english_list:
            print(enter, "is not in the English list")
            continue_translator = input("Another word (y or n) ")
            # put this before a valid translation, not "-"

        # if the word is not in the english list, tell the user

    print("\nTranslated words have been saved to", name_file)
    out_file.close()
# translate the word. if there is a translation, show the user
# if there is no translation, tell the user
# then ask if they want to translate the word

# ------------------------------------------------CALLING FUNCTIONS--------------------------------------------------- #


def main():
    print("Language Translator")
    display = get_languages("languages.csv")
    translate = read_file(display, lang_str="English", file_name="languages.csv")
    translated_lang = get_translation_language(display)
    trans_lang_one = read_file(display, lang_str=translated_lang, file_name="languages.csv")
    create_results_file(translated_lang)
    translate_words(translate, trans_lang_one, translated_lang)


main()


