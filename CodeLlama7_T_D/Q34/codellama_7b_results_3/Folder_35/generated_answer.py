
def find_original_set(sets):
    # Sort the sets by their size
    sorted_sets = sorted(sets, key=len)
    # Initialize the smallest set as the first element of the list
    smallest_set = sorted_sets[0]
    # Iterate over each set and find the smallest set that contains all elements
    for i in range(1, len(sorted_sets)):
        current_set = sorted_sets[i]
        if not current_set.isdisjoint(smallest_set):
            smallest_set |= current_set
    return smallest_set
