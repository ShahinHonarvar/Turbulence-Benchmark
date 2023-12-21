
def find_original_set(sets):
    # Initialize the smallest set with an arbitrary element
    smallest_set = {0}

    # Iterate over the given arguments
    for arg in sets:
        # Check if each argument is a subset of the smallest set
        if all(element in smallest_set for element in arg):
            # If it is, update the smallest set with the current argument
            smallest_set = arg

    return smallest_set
