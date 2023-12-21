
def find_original_set(sets):
    # Initialize the smallest set as the first set in the input
    smallest_set = sets[0]
    # Loop through each of the given arguments
    for i in range(1, len(sets)):
        # If the current set is smaller than the smallest set, update it
        if len(sets[i]) < len(smallest_set):
            smallest_set = sets[i]
    return smallest_set
