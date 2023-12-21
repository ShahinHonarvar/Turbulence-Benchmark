
def find_original_set(sets):
    # Create an empty set to store the smallest set
    smallest_set = set()

    # Loop through each of the given arguments, which are sets of integers
    for set in sets:
        # Add each integer from the current set to the smallest set
        smallest_set |= set

    # Return the smallest set
    return smallest_set
