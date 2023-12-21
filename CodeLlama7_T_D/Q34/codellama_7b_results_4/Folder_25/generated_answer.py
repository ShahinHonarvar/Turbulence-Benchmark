
def find_original_set(sets):
    # initialize the smallest set with the first element from each set
    smallest_set = {s for s in sets[0]}
    # iterate over the remaining elements
    for i in range(1, len(sets)):
        # if the current element is not in the smallest set, add it and update the smallest set
        if any(element not in smallest_set for element in sets[i]):
            smallest_set |= {s for s in sets[i]}
    return smallest_set
