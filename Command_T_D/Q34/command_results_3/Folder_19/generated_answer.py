import sys
def find_original_set(s):
    lst = set(s)
    for i in range(len(lst)):
        lst -= set(s[i])
    return lst
