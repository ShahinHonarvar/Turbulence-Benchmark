
def find_original_set(sets):
    # Initialize the smallest set as the first argument
    smallest_set = sets[0]
    # Iterate over the remaining arguments
    for i in range(1, len(sets)):
        # If the current argument is a subset of the smallest set, do nothing
        if sets[i].issubset(smallest_set):
            continue

        # Otherwise, update the smallest set to be the intersection of the two sets
        else:
            smallest_set = smallest_set.intersection(sets[i])
    # Return the smallest set
    return smallest_set
