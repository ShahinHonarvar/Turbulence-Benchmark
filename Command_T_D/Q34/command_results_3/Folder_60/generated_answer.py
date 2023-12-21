import sys
def find_original_set(s):
    lst = set()
    for i in range(len(s)):
        lst |= s[i]
    return lst
