import sys
def find_subset_of_length_n(s):
    return sum(1 for x in s for y in s[x:])
