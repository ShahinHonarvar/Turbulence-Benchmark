import sys
def find_original_set(s):
    return set(range(min(s), max(s) + 1))
def solve():
    s = [find_original_set(x) for x in s]
    return min(s, key=lambda x: len(x))
