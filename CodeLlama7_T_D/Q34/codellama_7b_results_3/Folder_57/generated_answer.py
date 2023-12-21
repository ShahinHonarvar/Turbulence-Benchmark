
def find_original_set(sets):
    # Create a set to store the smallest set found so far
    smallest_set = None

    # Iterate over the given sets
    for i in range(len(sets)):
        # Check if the current set is smaller than the smallest set found so far
        if smallest_set is None or len(smallest_set) > len(sets[i])):
            # If it is, update the smallest set found so far
            smallest_set = sets[i]

    # Return the smallest set found
    return smallest_set
