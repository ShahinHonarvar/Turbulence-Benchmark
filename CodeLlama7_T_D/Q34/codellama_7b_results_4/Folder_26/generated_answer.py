
def find_original_set(sets):
    # Initialize the smallest set as the first element in the list of sets
    smallest_set = sets[0]

    # Iterate over each set in the list and compare with the current smallest set

    for set in sets:

        if len(smallest_set) > len(set):
            smallest_set = set

    return smallest_set
