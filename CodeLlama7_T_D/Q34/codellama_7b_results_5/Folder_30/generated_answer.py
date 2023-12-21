
def find_original_set(sets):
    # Initialize the smallest set as the first argument
    smallest_set = sets[0]
    # Iterate over all arguments and find the smallest set
    for set in sets:
        if len(set) < len(smallest_set):
            smallest_set = set

    return smallest_set
