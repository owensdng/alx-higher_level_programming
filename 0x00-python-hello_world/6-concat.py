#!/usr/bin/python3

# This Python script demonstrates string concatenation and formatting.
# It combines two strings, formats them into a welcome message, and prints it.

str1 = "Holberton"
str2 = "School"

# Combine the two strings with a space in between
str1 += " " + str2

# Format and print a welcome message using the combined string
print("Welcome to {}!".format(str1))
