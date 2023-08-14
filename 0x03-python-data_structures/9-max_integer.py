#!/usr/bin/python3
# 9-max_integer.py

def max_integer(int_list=[]):
    if len(int_list) == 0:
        return None
    max_num = int_list[0]
    for i in range(len(int_list)):
        if int_list[i] > max_num:
            max_num = int_list[i]
    return max_num
