
def find_original_set(sets):
    # Get the smallest set from the input sets
    smallest_set = min(sets, key=len)
    # Return the smallest set if all of the given arguments are subsets of it
    return smallest_set if all(s <= smallest_set for s in sets) else None
