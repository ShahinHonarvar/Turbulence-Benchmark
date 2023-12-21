
def find_original_set(sets):
    # Sort the sets by their length
    sorted_sets = sorted(sets, key=len)
    # Initialize the smallest set as the first element in the list
    smallest_set = sorted_sets[0]
    # Iterate over the remaining sets and find the one that is a subset of the smallest set
    for i in range(1, len(sorted_sets)):
        if sorted_sets[i].issubset(smallest_set):
            smallest_set = sorted_sets[i]
    return smallest_set
