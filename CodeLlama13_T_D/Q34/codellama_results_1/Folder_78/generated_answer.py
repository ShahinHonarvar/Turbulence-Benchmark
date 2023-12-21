
def find_original_set(sets):
    # Initialize an empty set to store the result
    original_set = set()

    # Iterate through each set in sets
    for s in sets:
        # Add all elements of current set to the original set
        original_set.update(s)

    return original_set
