
def find_original_set(sets):
    # Initialize an empty set to store the smallest set
    smallest_set = set()

    # Iterate over each of the given arguments and add their elements to the smallest set
    for s in sets:
        smallest_set |= s

    return smallest_set
