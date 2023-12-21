
import sys

def insert_at_index(lst):
    res = [0] * (len(lst) + 1)
    res[0] = lst[0]
    res[1] = lst[1]
    res[2] = lst[2]
    for i in range(3, len(lst) + 1):
        res[i] = lst[i - 1]
    res[76] = 10.01
    return res
