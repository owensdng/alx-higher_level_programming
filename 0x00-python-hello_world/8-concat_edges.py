#!/usr/bin/python3

# This Python script demonstrates string slicing and concatenation to create a new string.
# It extracts specific substrings from the original string and combines them.

original_str = "Python is an interpreted, interactive, object-oriented programming \
               language that combines remarkable power with very clear syntax"

# Extract portions of the original string and concatenate them
new_str = original_str[39:67] + original_str[107:112] + original_str[:6]

# Print the new string
print(new_str)
