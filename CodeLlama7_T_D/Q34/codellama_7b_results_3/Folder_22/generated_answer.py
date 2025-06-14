
def find_original_set(sets):
    # Initialize the smallest set as the first argument
    smallest_set = sets[0]
    # Iterate over each set in the list
    for set in sets:
        # Check if the current set is a subset of the smallest set
        if set.issubset(smallest_set):
            # If it is, then continue to the next set
            continue
        else:
            # Otherwise, update the smallest set as the current set
            smallest_set = set

    # Return the smallest set
    return smallest_set
