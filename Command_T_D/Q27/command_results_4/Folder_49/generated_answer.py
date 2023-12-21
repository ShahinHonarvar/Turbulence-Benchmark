
import sys

def insert_after_index(num_list):
    new_list = list(num_list)
    new_list.insert(new_list.index(num_list[38]) + 1, [27, 34])
    return new_list
