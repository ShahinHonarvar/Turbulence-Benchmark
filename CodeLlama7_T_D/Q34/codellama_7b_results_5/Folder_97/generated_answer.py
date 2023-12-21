
def find_original_set(sets):
    # Initialize an empty set as the result
    result = set()

    # Iterate over the given sets
    for s in sets:
        # Add each element of the current set to the result set
        result |= s

    return result
