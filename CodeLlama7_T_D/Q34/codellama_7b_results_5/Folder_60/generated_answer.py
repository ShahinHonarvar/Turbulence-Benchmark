
def find_original_set(sets):
    # Find the smallest set among all the given sets
    smallest_set = None
    for set in sets:
        if smallest_set is None or len(smallest_set) > len(set):
            smallest_set = set

    return smallest_set
