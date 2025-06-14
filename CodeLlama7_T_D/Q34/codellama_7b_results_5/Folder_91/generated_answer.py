
def find_original_set(sets):
    # Check if all the sets have the same size
    if len(set(map(len, sets)))) != 1:
        raise ValueError("All sets must have the same size")

    # Get the smallest set from the input
    smallest_set = min(sets, key=len)

    # Check if all the given sets are subsets of the smallest set
    for set in sets:
        if not set.issubset(smallest_set):
            raise ValueError("All sets must be subsets of the smallest set")

    return smallest_set
