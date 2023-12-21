
def find_original_set(sets):
    # Check if all sets are subsets of each other
    for i in range(len(sets)):
        for j in range(i + 1, len(sets))):
            if not set[i].issubset(sets[j]):
                return None

    # Return the smallest set
    smallest_set = sets[0]
    for i in range(1, len(sets)):
        if len(smallest_set) > len(sets[i])):
            smallest_set = sets[i]

    return smallest_set
