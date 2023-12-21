
def find_original_set(sets):
    # Initialize an empty set
    original_set = set()

    # Iterate over the given sets
    for s in sets:
        # Add each element of the current set to the original set
        for elem in s:
            original_set.add(elem)

    # Return the smallest possible original set
    return original_set
