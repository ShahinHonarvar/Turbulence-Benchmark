
def find_original_set(sets):
    # Initialize the smallest set with the first argument
    smallest_set = sets[0]
    # Loop through each of the given arguments
    for set in sets:
        # If the current set is smaller than the smallest set, update the smallest set
        if len(smallest_set) > len(set):
            smallest_set = set

    return smallest_set
