"""
This little program helps to learn the coversion
between numbers and roman numbers
Author: Paolo Maria Guardiani
"""

import os
import random

roman_unit = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
roman_tens = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
roman_hundreds = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
roman_thousands = ["M", "MM", "MMM"]

# for i in range(100):  # this clear the screen! this is not my idea!
#     print("\n")

score = 0
test_number = 0
selected_level = 0

# List of colors and how to use it thanks to: 
# https://stackoverflow.com/questions/19731053/change-shell-print-color-in-python-3-3-2
# the ANSI codes are stored in variables, making them easier to use
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"

game_over = False

def change_number(number):
    unit = 0
    tens = 0
    hundreds = 0
    thousands = 0

    first_roman_letter = ""
    second_roman_letter = ""
    third_roman_letter = ""
    fourth_roman_letter = ""

    result = ""

    if number > 999:
        thousands = number // 1000
        hundreds = number - (thousands * 1000)
        hundreds = hundreds // 100
        tens = number - (thousands * 1000) - (hundreds * 100)
        tens = tens // 10
        unit = number - (thousands * 1000) - (hundreds * 100) - (tens * 10)
        first_roman_letter = roman_thousands[thousands - 1]
        if (hundreds != 0):
            second_roman_letter = roman_hundreds[hundreds - 1]
        if (tens != 0):
            third_roman_letter = roman_tens[tens - 1]
        if (unit != 0):
            fourth_roman_letter = roman_unit[unit - 1]
        result = first_roman_letter + second_roman_letter + third_roman_letter + fourth_roman_letter
    elif (number >= 100) and (number <= 999):
        hundreds = number // 100
        tens = number - (hundreds * 100)
        tens = tens // 10
        unit = number - (hundreds * 100) - (tens * 10)
        second_roman_letter = roman_hundreds[hundreds - 1]
        if (tens != 0):
            third_roman_letter = roman_tens[tens - 1]
        if (unit != 0):
            fourth_roman_letter = roman_unit[unit - 1]
        result = second_roman_letter + third_roman_letter + fourth_roman_letter
    elif (number >= 10) and (number <= 99):
        tens = number // 10
        unit = number - (tens * 10)
        first_roman_letter = roman_thousands[thousands - 1]
        third_roman_letter = roman_tens[tens - 1]
        if (unit != 0):
            fourth_roman_letter = roman_unit[unit - 1]
        result = third_roman_letter + fourth_roman_letter
    else:
        unit = number
        if (unit != 0):
            fourth_roman_letter = roman_unit[unit - 1]
        result = fourth_roman_letter
    
    return result

def generate_number(level):
    if level == 1: 
        sorted_number = random.randint(1, 10)
    elif level == 2:
        sorted_number = random.randint(10, 100)
    elif selected_level == 3:
        sorted_number = random.randint(100, 999)
    elif selected_level == 4:
        sorted_number = random.randint(1000, 3999)
    return sorted_number 


print("Welcome to the game Conversion to Roman Numerals")
print("Select the level of the game:")
print("1 - Basic: from 1 to 10")
print("2 - Esasy: from 10 to 100")
print("3 - Difficult: from 100 to 999")
print("4 - Very Difficult: from 1000 to 3999")
print("\n0 - Quit the game\n")

selection = False

while(selection == False):
    selected_level = int(input("- - - > "))
    if selected_level == 1: 
        selection = True
    elif selected_level == 2:
        selection = True
    elif selected_level == 3:
        selection = True
    elif selected_level == 4:
        selection = True
    elif selected_level == 0:
        correct_selection = True
        game_over = True
        print("OK, By By!")
    else:
        print("Please, enter a valid number")

if (game_over == False):
    for i in range(10):      
        test_number += 1
        os.system('cls')  # 'cls' on Windows; 'clear' on linux
        sorted_number = generate_number(selected_level)
        print(f"{white}***************************************************")   
        print(f"Convert this number ---> {sorted_number} <--- in roman numbers: ")
        user_number = input().upper()

        roman_number = change_number(sorted_number)

        if user_number == roman_number:
            print(f"{bright_green}Great, your conversion, {roman_number}, is correct!")
            score += 1
        else:
            print(f"{bright_red}I am sorry, the conversion is: {roman_number}")
            score += 0
        actuale_score = (10 * score) / test_number
        print(f"Test number {test_number}/10 - - - Score: {round(actuale_score, 2)}")
        print(f"{white}***************************************************")

        print("\nPlease, press any key to continue ... ")
        input()
        os.system('cls')  # 'cls' on Windows; 'clear' on linux

if test_number > 0: # so the game has started:
    print("These are the results:")
    print(f"You have done {test_number} test. Your score is: {round(actuale_score, 2)}")