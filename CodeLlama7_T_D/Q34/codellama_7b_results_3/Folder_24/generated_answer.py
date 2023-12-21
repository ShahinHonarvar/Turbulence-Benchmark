
def find_original_set(sets):
    # Initialize an empty set as the smallest set
    smallest_set = set()

    # Loop through each of the given arguments, which are sets of integers
    for set in sets:
        # Add each element of the current set to the smallest set
        smallest_set |= set

    return smallest_set
