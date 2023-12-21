
def find_original_set(sets):
    # Find the smallest set that contains all the given sets
    smallest_set = None
    for set in sets:
        if smallest_set is None:
            smallest_set = set
        else:
            smallest_set = smallest_set.union(set)
    return smallest_set
