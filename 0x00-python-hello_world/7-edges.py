#!/usr/bin/python3

# This Python script demonstrates string slicing to extract portions of a word.
# It extracts and prints the first 3 letters, last 2 letters, and the middle portion of a word.

word = "Holberton"

# Extract the first 3 letters
word_first_3 = word[:3]

# Extract the last 2 letters
word_last_2 = word[-2:]

# Extract the middle portion (excluding the first and last characters)
middle_word = word[1:-1]

# Print the extracted portions
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
