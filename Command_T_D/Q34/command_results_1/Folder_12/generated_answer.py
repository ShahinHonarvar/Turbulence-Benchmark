import itertools
def find_original_set(subset):
    sets = list(map(set, subset))
    return min(filter(lambda s: all(s&s1 for s1 in sets), set(range(len(subset))))
