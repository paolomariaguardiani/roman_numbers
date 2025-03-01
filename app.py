import random

roman_unit = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
roman_tens = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
roman_hundreds = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
roman_thousands = ["M", "MM", "MMM"]

for i in range(100):  # this clear the screen! this is not my idea!
    print("\n")

sorted_number = random.randint(1, 3999)
print(sorted_number)


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


print(f"Convert this number ---> {sorted_number} in roman numbers: ")
user_number = input().upper()

roman_number = change_number(sorted_number)

if user_number == roman_number:
    print(f"\nGreat, your conversion, {roman_number}, is correct\n\n")
else:
    print(f"\nI am sorry, the conversion is: {roman_number}\n\n")

