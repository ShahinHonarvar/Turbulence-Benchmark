
def find_original_set(sets):
    # Initialize the smallest set as the first set in the input list
    smallest_set = sets[0]
    # Iterate over each set in the input list
    for i in range(1, len(sets)):
        # If the current set is smaller than the smallest set, update the smallest set
        if len(sets[i]) < len(smallest_set):
            smallest_set = sets[i]
    return smallest_set
