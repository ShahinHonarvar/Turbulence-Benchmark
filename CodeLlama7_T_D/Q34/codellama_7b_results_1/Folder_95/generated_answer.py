
def find_original_set(sets):
    # Create a copy of the input sets
    original_sets = sets[:]
    # Initialize an empty set as the smallest set
    smallest_set = set()

    # Loop through each set in the input
    for set in sets:

        # If the current set is smaller than the smallest set found so far, make it the new smallest set
        if len(set) < len(smallest_set):
            smallest_set = set

    # Return the smallest set found
    return smallest_set
