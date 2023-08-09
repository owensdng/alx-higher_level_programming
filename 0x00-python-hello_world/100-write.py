#!/usr/bin/python3

# This Python script demonstrates writing an error message to the standard error stream
# and then exiting with a non-zero status code.

import sys

# Write an error message to the standard error stream
sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")

# Exit the script with a non-zero status code (indicating an error)
sys.exit(1)
