import sys
def find_original_set(*args):
    sets = list(map(set, args))
    return min(set(range(min(s), max(s)+1)) for s in sets)
