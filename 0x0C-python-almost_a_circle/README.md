# Almost a circle

I used my Python skills to code three connected classes to represent rectangles and squares, along with unit tests using the unittest module.

The three classes involved utilize the following Python tools:

Import
Exceptions
Private attributes
Getter/setter
Class/static methods
Inheritance
File I/O
args/kwargs
JSON and CSV serialization/deserialization
Unittesting
Tests
I wrote the following test files in the tests/test_models directory:

test_base.py
test_rectangle.py
test_square.py
Classes
Base
The Base class represents the base class for all other classes in the project. It includes the following:

A private class attribute __nb_objects = 0.
A public instance attribute id.
A class constructor __init__() that increments __nb_objects and assigns its value to the public instance attribute id if id is not provided.
A static method to_json_string() that returns the JSON string serialization of a list of dictionaries.
A class method save_to_file() that writes the JSON serialization of a list of objects to a file.
A static method from_json_string() that returns a list of objects deserialized from a JSON string.
A class method create() that instantiates an object with provided attributes.
A class method load_from_file() that returns a list of objects instantiated from a JSON file.
A class method save_to_file_csv() that writes the CSV serialization of a list of objects to a file.
A class method load_from_file_csv() that returns a list of objects instantiated from a CSV file.
A static method draw() that draws Rectangle and Square instances in a GUI window using the turtle module.
Rectangle
The Rectangle class represents a rectangle and inherits from the Base class. It includes the following:

Private instance attributes __width, __height, __x, and __y. Each private instance attribute features its own getter/setter.
A class constructor __init__() that validates the values of width, height, x, and y.
A public method area() that returns the area of the Rectangle instance.
A public method display() that prints the Rectangle instance to stdout using the # character.
An overwrite of the __str__() method to print a Rectangle instance in the format [Rectangle] (<id>) <x>/<y>.
A public method update() that updates an instance of a Rectangle with the given attributes.
A public method to_dictionary() that returns the dictionary representation of a Rectangle instance.
Square
The Square class represents a square and inherits from the Rectangle class. It includes the following:

A class constructor __init__() that assigns the value of size to both the width and height of the Rectangle superclass.
An overwrite of the __str__() method to print a Square instance in the format [Square] (<id>) <x>/<y>.
A public method update() that updates an instance of a Square with the given attributes.
A public method to_dictionary() that returns the dictionary representation of a Square instance.
Usage
To use the Rectangle and Square classes, simply import them into your project and create new instances of the classes. You can then set the attributes of the shapes and call their methods.

For example, the following code creates a new Rectangle instance with a width of 10, a height of 2, and an x and y coordinate of 0:

Python
from models.rectangle import Rectangle

rectangle = Rectangle(10, 2)
