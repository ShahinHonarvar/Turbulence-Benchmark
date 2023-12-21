
def find_original_set(sets):
    # Create a set of all elements in the given sets
    all_elements = set()
    for s in sets:
        all_elements |= s

    # Initialize the smallest set as the first set

    smallest_set = sets[0]

    # Iterate over each element in the largest set and check if it is a subset of the current smallest set

    for e in all_elements:
        if e not in smallest_set:
            break

    # If the current element is not in the smallest set, then we need to update the smallest set

    if e not in smallest_set:
        smallest_set = smallest_set | {e}

    return smallest_set
