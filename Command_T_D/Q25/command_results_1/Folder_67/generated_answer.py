
import sys
input = sys.stdin.readline

def insert_at_index(lst):
    return lst[:44] + [76] + lst[45:] + [len(lst) + 1]
