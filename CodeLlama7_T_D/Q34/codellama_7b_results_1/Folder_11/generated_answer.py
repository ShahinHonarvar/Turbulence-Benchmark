
def find_original_set(sets):
    # Find the smallest set in the input
    smallest_set = min(sets, key=len)
    # Return the smallest set if it is already a subset of all other sets
    if len(smallest_set & set.union(*sets)) == len(smallest_set):
        return smallest_set

    # Otherwise, find the intersection of all sets and return it as the smallest set
    else:
        return set.intersection(*sets)
