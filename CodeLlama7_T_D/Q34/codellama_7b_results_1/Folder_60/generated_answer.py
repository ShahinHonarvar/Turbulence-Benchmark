
def find_original_set(sets):
    # Create a set to store the elements
    original_set = set()

    # Loop through each of the given sets
    for s in sets:
        # Add each element of the current set to the original set
        original_set.update(s)

    # Return the smallest set such that each of the given arguments is a subset of it
    return original_set
