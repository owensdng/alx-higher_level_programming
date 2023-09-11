#!/usr/bin/python3
"""
Module: 3-is_kind_of_class

Description: A module that defines the function is_kind_of_class.
"""

def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if it is an instance of a class
    that inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        True if obj is an instance of a_class or inherited from it; otherwise, False.
    """
    return isinstance(obj, a_class)

if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
