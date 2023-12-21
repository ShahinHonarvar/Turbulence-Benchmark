import sys
def find_original_set(s):
    x = set(s)
    x.update(s)
    return x
