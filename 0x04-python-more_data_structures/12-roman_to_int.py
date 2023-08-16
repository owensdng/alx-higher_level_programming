#!/usr/bin/python3
def calculate_subtraction(numbers):
    subtraction_value = 0
    max_number = max(numbers)

    for n in numbers:
        if max_number > n:
            subtraction_value += n

    return (max_number - subtraction_value)


def convert_roman_to_integer(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral_keys = list(roman_numerals.keys())

    total = 0
    last_value = 0
    numeral_list = [0]

    for char in roman_string:
        for numeral in numeral_keys:
            if numeral == char:
                if roman_numerals.get(char) <= last_value:
                    total += calculate_subtraction(numeral_list)
                    numeral_list = [roman_numerals.get(char)]
                else:
                    numeral_list.append(roman_numerals.get(char))

                last_value = roman_numerals.get(char)

    total += calculate_subtraction(numeral_list)

    return total
