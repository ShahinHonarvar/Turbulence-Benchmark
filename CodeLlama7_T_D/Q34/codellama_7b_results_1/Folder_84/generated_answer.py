
def find_original_set(sets):
    # Initialize an empty set
    original_set = set()

    # Iterate over the given sets
    for s in sets:
        # Update the original set with the current set
        original_set |= s

    # Return the smallest set that contains all the given sets
    return original_set
