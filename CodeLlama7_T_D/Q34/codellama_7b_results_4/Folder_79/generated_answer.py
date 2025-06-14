
def find_original_set(sets):
    # Create an empty set to store the smallest set
    smallest_set = set()

    # Iterate through each of the given sets and add their elements to the smallest set
    for s in sets:
        smallest_set |= s

    return smallest_set
