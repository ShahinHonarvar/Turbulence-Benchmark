
def find_original_set(sets):
    # Initialize the smallest set with the first element
    smallest_set = sets[0]
    # Iterate over all given sets and update the smallest set if necessary
    for set in sets:
        if len(set) < len(smallest_set):
            smallest_set = set

    # Return the smallest set
    return smallest_set
