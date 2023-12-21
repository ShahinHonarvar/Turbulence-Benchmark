
def find_original_set(sets):
    # Create a copy of the sets list
    original_sets = sets[:]
    # Initialize an empty set as the smallest set
    smallest_set = set()

    # Loop through each set in the original_sets list
    for set in original_sets:
        # Add all elements from the current set to the smallest set
        smallest_set.update(set)

    # Return the smallest set as the solution
    return smallest_set
