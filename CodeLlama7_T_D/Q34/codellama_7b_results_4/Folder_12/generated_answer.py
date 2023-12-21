
def find_original_set(sets):
    # Initialize the smallest set as the first element in the list of given sets
    smallest_set = sets[0]

    # Iterate over each set and check if it is a subset of the smallest set

    for i in range(1, len(sets)):
        if not sets[i].issubset(smallest_set):
            # If the current set is not a subset of the smallest set, then update the smallest set to be the current set
            smallest_set = sets[i]

    return smallest_set
