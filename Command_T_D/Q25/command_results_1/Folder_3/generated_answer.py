
import sys

def insert_at_index(my_list):
    sys.setrecursionlimit(10**6)
    insert_at_index = my_list[:31] + [88, 51] + my_list[32:]
    return insert_at_index
