
def find_original_set(sets):
    # Check if all sets are distinct
    if len(sets) != len(set(tuple(s) for s in sets))):
        raise ValueError("All sets must be distinct")
    # Initialize the smallest set to be the first set
    smallest_set = sets[0]
    # Loop through each set and find the smallest set that contains it
    for i in range(1, len(sets)):
        if not sets[i].issubset(smallest_set):
            smallest_set = smallest_set.union(sets[i])
    return smallest_set
