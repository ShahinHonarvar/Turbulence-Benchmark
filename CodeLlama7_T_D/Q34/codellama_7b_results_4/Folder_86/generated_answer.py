
def find_original_set(sets):
    # Get the list of all elements in the given sets
    all_elements = set()
    for s in sets:
        all_elements |= s

    # Create an empty set to store the smallest set

    smallest_set = set()

    # Iterate over all possible subsets of the given sets

    for subset in powerset(all_elements):

        # Check if the current subset is a subset of each of the given sets

        is_subset = True
        for s in sets:
            if not (s <= subset):
                is_subset = False
                break

        # If the current subset is a subset of all the given sets, update the smallest set

        if is_subset:
            if len(smallest_set) > len(subset):
                smallest_set = subset

    return smallest_set
