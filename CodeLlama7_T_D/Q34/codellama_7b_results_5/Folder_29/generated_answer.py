
def find_original_set(sets):
    # Initialize the smallest set as the first set in the given argument
    smallest_set = sets[0]
    # Loop through each set in the given argument
    for set in sets:
        # Check if the current set is a subset of the smallest set
        if set <= smallest_set:
            # If it is, then do nothing
            pass

        else:
            # If it is not, then update the smallest set as the current set
            smallest_set = set

    # Return the smallest set as the original set
    return smallest_set
