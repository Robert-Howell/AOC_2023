# Import the regex libary, we use this to parse each string for the digits
import re

# This dict will be used later to replace words with digits
num_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


# This function finds all the digits in a string, and returns a string that has the very first and very last digit
def number_finder(num_string):
    new_num = re.findall(r'\d+', num_string)
    return new_num[0][0] + new_num[-1][-1]


# This function is for the second portion. 
# It is not elegant, it loops through the dict and replaces words with digits
def string_cleaner(dirty_string):
    for word, number in num_dict.items():
        dirty_string = dirty_string.replace(word, word + number + word)
    return dirty_string


# This function calculates the total for the first portion of the challenge
def first_part_total(data):
    total = 0
    for str_fragment in data:
        total += int(number_finder(str_fragment))
    return total


# This function calculates the total for the second portion of the challenge
def second_part_total(dirty_data):
    second_total = 0
    for dirty_string in dirty_data:
        second_total += int(number_finder(string_cleaner(dirty_string)))
    return second_total


# This opens the input file and converts it into a list for us to use
with open("dayone_input.txt", "r") as file:
    original_data = [x.strip("\n") for x in file]

# Finally, calculate the totals 
print(first_part_total(original_data), second_part_total(original_data))


# The regex portion could be accomplished with loops going forwards and backwards through the string, 
# finding the first digit, and concatinating them together. Using regex puts the onus of that work 
# onto the library and fits the Python ethos of 'let someone else do the work'
