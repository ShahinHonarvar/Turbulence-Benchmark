
def find_original_set(sets):
    # Initialize an empty set to store the smallest subset
    smallest = set()

    for s in sets:
        # For each set, add all its elements to the smallest set
        smallest |= s

    return smallest
