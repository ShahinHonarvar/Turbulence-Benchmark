
def find_original_set(sets):
    # Initialize an empty set as the smallest set
    smallest_set = set()

    # Iterate over the given arguments and find the smallest set that contains all of them
    for arg in sets:
        smallest_set |= arg

    return smallest_set
