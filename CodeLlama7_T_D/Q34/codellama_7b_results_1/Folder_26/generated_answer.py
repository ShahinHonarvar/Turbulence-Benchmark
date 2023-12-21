
def find_original_set(sets):
    # Create an empty set to store the original set
    original_set = set()

    # Iterate through each set in the input list
    for s in sets:
        # Add each element of the current set to the original set
        original_set.update(s)

    # Return the smallest set such that each of the given arguments is a subset of it
    return min(original_set, key=len)
