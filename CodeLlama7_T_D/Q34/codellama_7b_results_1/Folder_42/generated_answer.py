
def find_original_set(sets):
    # Initialize the smallest set as the first element of the input list
    smallest_set = sets[0]

    # Iterate over each set in the input list
    for set in sets:

        # If the current set is smaller than the smallest set, update the smallest set
        if len(set.intersection(smallest_set)) < len(set):
            smallest_set = set

    # Return the smallest set
    return smallest_set
