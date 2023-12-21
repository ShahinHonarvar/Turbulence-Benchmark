
def find_original_set(set1, set2, set3):
    # Create an empty set to store the original sets
    original_sets = set()

    # Add each of the given arguments to the original sets
    for arg in (set1, set2, set3):
        original_sets.add(arg)

    # Return the smallest set from the original sets
    return min(original_sets, key=len)
