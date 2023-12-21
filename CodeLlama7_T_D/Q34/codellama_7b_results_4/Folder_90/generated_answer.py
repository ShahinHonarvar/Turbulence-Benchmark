
def find_original_set(sets):
    # Initialize the smallest set as the first element in the list of given sets
    smallest_set = sets[0]

    for i in range(1, len(sets)):
        # If the current set is smaller than the smallest set, update the smallest set to be the current set
        if len(sets[i]) < len(smallest_set):
            smallest_set = sets[i]

    return smallest_set
