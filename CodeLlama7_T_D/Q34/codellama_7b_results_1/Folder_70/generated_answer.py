
def find_original_set(sets):
    # Initialize the smallest set as the first set in the input
    smallest_set = sets[0]
    # Iterate over each set in the input
    for i in range(1, len(sets)):
        # If the current set is a subset of the smallest set, continue to the next set
        if sets[i].issubset(smallest_set):
            continue

        # Otherwise, update the smallest set with the current set
        else:
            smallest_set = sets[i]

    return smallest_set
