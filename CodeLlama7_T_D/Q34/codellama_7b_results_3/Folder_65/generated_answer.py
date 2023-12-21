
def find_original_set(sets):
    # Find the smallest set that contains all the given sets
    min_set = None
    for set in sets:
        if min_set is None:
            min_set = set
        else:
            min_set = min_set.union(set)
    return min_set
