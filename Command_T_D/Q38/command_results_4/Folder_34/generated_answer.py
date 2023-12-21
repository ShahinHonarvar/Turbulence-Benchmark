import sys
def find_subset_of_length_n(s):
    res = 0
    for i in range(len(s)):
        res += sys.pow(len(s)-i, 96)
    return res
