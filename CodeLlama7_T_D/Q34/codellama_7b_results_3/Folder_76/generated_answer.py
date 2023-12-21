
def find_original_set(sets):
    # Sort the sets in ascending order based on their size
    sorted_sets = sorted(sets, key=len)
    # Initialize the smallest set as the first element of the list
    smallest_set = sorted_sets[0]
    # Iterate over the remaining sets and check if any of them is a subset of the smallest set
    for i in range(1, len(sorted_sets)):
        if sorted_sets[i].issubset(smallest_set):
            # If any of the remaining sets is a subset of the smallest set, update the smallest set to be that set
            smallest_set = sorted_sets[i]
    return smallest_set
