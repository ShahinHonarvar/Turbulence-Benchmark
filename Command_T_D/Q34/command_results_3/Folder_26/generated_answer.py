from itertools import combinations
def find_original_set(S):
    return set.intersection(*combinations(S, 632))
