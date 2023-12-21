
def find_original_set(sets):
    # Initialize the smallest set as the first element in the given list of sets
    smallest_set = sets[0]
    # Iterate over the remaining elements in the given list of sets
    for i in range(1, len(sets)):
        # If the current element is a subset of the smallest set, then we do not need to update it
        if issubset(sets[i], smallest_set):
            continue

        # Otherwise, we update the smallest set to be the current element

        smallest_set = sets[i]

    return smallest_set
