
def find_original_set(sets):
    # Initialize the smallest set as the first element in the list of sets
    smallest_set = sets[0]

    # Iterate over each of the given arguments and check if it is a subset of the smallest set

    for i in range(1, len(sets)):
        current_set = sets[i]

        if len(current_set) < len(smallest_set):
            smallest_set = current_set

    return smallest_set
