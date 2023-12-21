from itertools import combinations
def find_original_set(sets):
    return set(combinations(range(len(sets)), 2))
