
import sys

sys.setrecursionlimit(10**6)

def insert_at_index(test_list):
    res = list(test_list)
    res.insert(32, [54, 96])
    return res
