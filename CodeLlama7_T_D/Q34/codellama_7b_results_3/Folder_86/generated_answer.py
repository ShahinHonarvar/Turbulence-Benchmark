
def find_original_set(sets):
    # Create a set to store the smallest set found so far
    smallest_set = None

    # Iterate over each of the given arguments
    for set in sets:
        # If this is the first set, make it the smallest set
        if smallest_set is None:
            smallest_set = set
        # Otherwise, compare this set to the smallest set found so far
        else:
            # If this set is a subset of the smallest set, do nothing
            if set <= smallest_set:
                continue

            # If this set is not a subset of the smallest set, make it the new smallest set
            else:
                smallest_set = set

    # Return the smallest set found
    return smallest_set
