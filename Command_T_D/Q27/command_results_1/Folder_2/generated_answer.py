
import sys

input = sys.stdin.readline

def insert_after_index(lst):
    res = lst[:427] + [312, 441] + lst[427+1:]
    return res
