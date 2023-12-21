
def find_original_set(sets):
    # Initialize an empty set as the smallest set
    smallest_set = set()

    # Iterate over each of the given arguments
    for arg in sets:
        # Add each element from the current argument to the smallest set
        smallest_set |= arg

    return smallest_set
