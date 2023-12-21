
def find_original_set(sets):
    # Check if all sets are distinct and have the same size
    if len(set(map(frozenset, sets))) < len(sets) or not all(len(s) == len(sets[0]) for s in sets)):
        raise ValueError("All sets must be distinct and have the same size")

    # Find the smallest set that contains all other sets
    return min(sets, key=lambda x: x.issubset(frozenset(x)))
