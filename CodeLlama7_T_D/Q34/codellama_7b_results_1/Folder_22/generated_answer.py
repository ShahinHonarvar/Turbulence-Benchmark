
def find_original_set(sets):
    # Initialize an empty set
    original_set = set()

    # Iterate over the input sets
    for s in sets:
        # Add each element of the current set to the original set
        original_set.update(s)

    # Return the smallest possible set
    return min(original_set, key=len)
