
def find_original_set(sets):
    # Check if all sets are non-empty and have the same size
    if not all([len(s) > 0 for s in sets]) or len(set(map(len, sets)))) != 1:
        raise ValueError("All sets must be non-empty and have the same size")
    # Initialize the smallest set as the first given set
    smallest_set = sets[0]
    # Iterate over each set and check if it is a subset of the smallest set
    for i in range(1, len(sets)):
        if sets[i] <= smallest_set:
            smallest_set = sets[i]
    return smallest_set
