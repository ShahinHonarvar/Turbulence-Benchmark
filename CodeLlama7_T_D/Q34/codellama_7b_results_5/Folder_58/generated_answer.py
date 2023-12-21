
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]

    # Iterate over each of the given arguments, and for each one, check if it is a subset of the smallest set. If it is not a subset, then update the smallest set to be the current argument.
    for set in sets:
        if not set.issubset(smallest_set):
            smallest_set = set

    # Return the smallest set

    return smallest_set
