#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    del new_list[idx]
    return new_list
