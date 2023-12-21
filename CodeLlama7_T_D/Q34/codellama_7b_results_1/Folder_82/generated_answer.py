
def find_original_set(sets):
    # Initialize the smallest set as the first element in the given list of sets
    smallest_set = sets[0]

    for i in range(1, len(sets)):
        # For each subsequent set, check if it is a subset of the current smallest set

        if not sets[i] <= smallest_set:

            # If it is not a subset, update the smallest set to be the current set

            smallest_set = sets[i]

    return smallest_set
