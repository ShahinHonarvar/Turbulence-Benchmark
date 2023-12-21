
def find_original_set(sets):
    # Create a new set that contains all the elements from the given sets
    new_set = set()
    for s in sets:
        new_set |= s

    # Return the smallest subset of the new set
    return min(new_set)
