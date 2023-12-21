
def find_original_set(sets):
    # Create a list to store the smallest set
    smallest_set = []

    # Loop through each of the given sets
    for set in sets:

        # If the current set is smaller than the smallest set found so far, update the smallest set
        if len(smallest_set) == 0 or len(set.intersection(smallest_set)) > 0:
            smallest_set = set

    # Return the smallest set found
    return smallest_set
