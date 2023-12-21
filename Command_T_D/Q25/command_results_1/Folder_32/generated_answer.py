
import sys

input = sys.stdin.readline

def insert_at_index(lst):
    res = lst[:76] + [10.01] + lst[76:]
    return res
