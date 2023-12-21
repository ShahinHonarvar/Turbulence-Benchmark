
def find_original_set(sets):
    # Initialize the smallest set as the first set in the input list
    smallest_set = sets[0]

    # Iterate through each of the given arguments
    for i in range(1, len(sets)):
        # If the current set is a subset of the smallest set, do nothing
        if sets[i] <= smallest_set:
            continue

        # Otherwise, update the smallest set to be the current set
        else:
            smallest_set = sets[i]

    # Return the smallest set found
    return smallest_set
