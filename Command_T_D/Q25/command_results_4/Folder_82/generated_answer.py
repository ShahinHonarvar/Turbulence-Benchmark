
import sys
input = sys.stdin.readline

def insert_at_index(lst):
    res = lst[:84] + [771.92] + lst[84:-1] + lst[-1:]
    return res
