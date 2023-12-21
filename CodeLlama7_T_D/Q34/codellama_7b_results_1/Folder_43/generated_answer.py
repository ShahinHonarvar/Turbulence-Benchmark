
def find_original_set(sets):
    # Initialize the smallest set as the first set in the list
    smallest_set = sets[0]

    # Loop through each set in the list and compare it to the smallest set
    for set in sets:

        # If the current set is smaller than the smallest set, update the smallest set
        if len(set) < len(smallest_set):
            smallest_set = set

    # Return the smallest set found
    return smallest_set
