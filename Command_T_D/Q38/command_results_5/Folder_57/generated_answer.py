import sys
def find_subset_of_length_n(S):
    return sum(1 for s in range(len(S) + 1) for lst in range(s+1, s+s+1)) for s in range(1, len(S) + 1))
