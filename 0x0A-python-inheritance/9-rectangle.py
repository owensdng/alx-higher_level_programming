#!/usr/bin/python3
"""
Module: 9-rectangle

Description: A module that defines the Rectangle class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class representing a Rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with a given width and height.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        # Validate width and height using the inherited integer_validator method
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Set the width and height as private attributes
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: A string in the format [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
