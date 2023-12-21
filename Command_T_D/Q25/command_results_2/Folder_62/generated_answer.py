
import sys

input = sys.stdin.readline

def insert_at_index(lst):
    return lst[:35] + [90, 76] + lst[35:-1] + lst[36:]
