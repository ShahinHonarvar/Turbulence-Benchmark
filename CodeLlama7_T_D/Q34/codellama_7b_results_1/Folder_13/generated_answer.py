
def find_original_set(sets):
    # Check if all the sets have the same size
    if len(set([len(s) for s in sets])) != 1:
        raise ValueError("All the sets must have the same size")

    # Initialize the smallest set as the first set
    smallest_set = sets[0]

    # Iterate over the remaining sets and update the smallest set if necessary
    for s in sets[1:]:
        if len(s) < len(smallest_set):
            smallest_set = s

    return smallest_set
