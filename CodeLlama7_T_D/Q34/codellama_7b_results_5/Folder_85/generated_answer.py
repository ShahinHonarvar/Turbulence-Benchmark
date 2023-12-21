
def find_original_set(sets):
    # Sort the sets in ascending order based on their length
    sorted_sets = sorted(sets, key=len)
    # Initialize the smallest set as the first element of the sorted list
    smallest_set = sorted_sets[0]
    # Iterate over each set and check if it is a subset of the smallest set
    for i in range(1, len(sorted_sets)):
        if sorted_sets[i].issubset(smallest_set):
            # If the current set is a subset of the smallest set, update the smallest set to be the current set
            smallest_set = sorted_sets[i]
    return smallest_set
