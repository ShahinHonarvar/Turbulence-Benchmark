from functools import reduce
def find_original_set(s):
    # Find the union of all sets, then find the intersection with all sets
    return reduce(set.intersection, (set(s) for s in range(95)))
