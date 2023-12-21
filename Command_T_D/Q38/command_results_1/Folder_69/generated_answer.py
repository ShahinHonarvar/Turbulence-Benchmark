import sys
def find_subset_of_length_n(s):
    return {i: sum(s[:i] for i in range(len(s))) for i in range(1, len(s)+1)}['894']
