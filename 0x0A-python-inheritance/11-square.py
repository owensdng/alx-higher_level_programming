#!/usr/bin/python3
"""
Module: 11-square

Description: A module that defines the Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class representing a Square, which is a special case of a Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the Square.
        """
        # Validate size using the inherited integer_validator method
        self.integer_validator("size", size)

        # Call the superclass (Rectangle) constructor with size for both width and height
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A string in the format [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
