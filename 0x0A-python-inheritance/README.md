Project Overview
I will learn about Python class inheritance in this project. I will learn the differences between super- and sub-classes while practicing inheritance, defining classes with multiple base classes, and overriding inherited methods and attributes.

Tasks
0. Lookup

I will write a function that returns a list of available attributes and methods of an object.
1. My list

I will write a Python class MyList that inherits from list. It will include:
A public instance method def print_sorted(self): that prints the list in ascending sorted order (assumes all list elements are ints).
2. Exact same object

I will write a Python function that returns True if an object is exactly an instance of a specified class; otherwise False.
3. Same class or inherit from

I will write a Python function that returns True if an object is an instance or inherited instance of a specified class; otherwise False.
4. Only sub class of

I will write a Python function that returns True if an object is an inherited instance (either directly or indirectly) from a specified class; otherwise False.
5. Geometry module

I will write an empty Python class BaseGeometry.
6. Improve Geometry

I will write a Python class BaseGeometry. It will build on 5-base_geometry.py: ./5-base_geometry.py with:
A public instance method def area(self): that raises an Exception with the message area() is not implemented.
7. Integer validator

I will write a Python class BaseGeometry. It will build on 6-base_geometry.py: ./6-base_geometry.py with:
A public instance method def integer_validator(self, name, value): that validates the parameter value.
It assumes the parameter name is always a string.
The parameter value must be an int, otherwise, a TypeError exception is raised with the message <name> must be an integer.
The parameter value must be greater than 0, otherwise, a ValueError exception is raised with the message <value> must be greater than 0.
8. Rectangle

I will write a Python class Rectangle that inherits from BaseGeometry (7-base_geometry.py: ./7-base_geometry.py). It will include:
Private attributes width and height - validated with integer_validator.
Instantiation with width and height: def __init__(self, width, height):
9. Full rectangle

I will write a Python class Rectangle that inherits from BaseGeometry (7-base_geometry.py: ./7-base_geometry.py). It will build on 8-rectangle.py: ./8-rectangle.py with:
Implementation of the method area().
A special method __str__ to print Rectangles in the format [Rectangle] <width>/<height>.
10. Square #1

I will write a Python class Square that inherits from Rectangle (9-rectangle.py: ./9-rectangle.py). It will include:
Private attribute size - validated with integer_validator.
Instantiation with size: def __init__(self, size):.
Implementation of the area() method.
11. Square #2

I will write a Python class Square that inherits from Rectangle (9-rectangle.py: ./9-rectangle.py). It will build on 10-square.py: ./10-square.py with:
A special method __str__ to print squares in the format [Square] <width>/<height>.
12. My integer

I will write a Python class MyInt that inherits from int. It will include:
Inversion of the == and `
