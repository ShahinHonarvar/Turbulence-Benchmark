
def find_original_set(sets):
    # Initialize the smallest set as the first set in the input
    smallest_set = sets[0]
    # Loop through each set in the input
    for set in sets:
        # If the current set is smaller than the smallest set, update the smallest set
        if len(set) < len(smallest_set):
            smallest_set = set

    return smallest_set
