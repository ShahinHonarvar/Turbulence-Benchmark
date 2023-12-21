from itertools import combinations
def find_original_set(sets):
    return min(set(c) for c in combinations(range(1, len(sets)+1), 2))
