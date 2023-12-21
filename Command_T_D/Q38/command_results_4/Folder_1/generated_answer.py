import sys
def find_subset_of_length_n(s):
    return sum(0 < i < j < len(s) for i in range(len(s)) for j in range(i+1, min(len(s), i+85)))
