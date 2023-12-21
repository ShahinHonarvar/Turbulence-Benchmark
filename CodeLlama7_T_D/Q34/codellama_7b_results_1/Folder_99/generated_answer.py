
def find_original_set(sets):
    # Create an empty set to store the smallest subset
    smallest_subset = set()

    # Loop through each set and add its elements to the smallest subset
    for s in sets:
        smallest_subset |= s

    # Return the smallest subset
    return smallest_subset
