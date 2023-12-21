
import sys
input = sys.stdin.readline

def insert_at_index(lst):
    lst = lst[:4] + [7] + lst[4:]
    return lst
