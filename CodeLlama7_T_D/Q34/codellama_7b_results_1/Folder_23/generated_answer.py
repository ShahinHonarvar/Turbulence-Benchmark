
def find_original_set(sets):
    # Initialize the smallest set as the first set in the input
    smallest_set = sets[0]
    # Iterate over each set in the input and check if it is a subset of the smallest set
    for set in sets:
        if set <= smallest_set:
            smallest_set = set

    return smallest_set
