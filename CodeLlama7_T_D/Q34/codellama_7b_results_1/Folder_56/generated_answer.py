
def find_original_set(sets):
    # Sort the sets in ascending order
    sorted_sets = sorted(sets)
    # Initialize the smallest set as the first set in the list
    smallest_set = sorted_sets[0]
    # Iterate over the remaining sets and compare them to the smallest set
    for i in range(1, len(sorted_sets)):
        if issubset(smallest_set, sorted_sets[i]):
            # If the current set is a subset of the smallest set, do nothing
            pass

        elif issubset(sorted_sets[i], smallest_set):
            # If the current set is a superset of the smallest set, replace the smallest set with the current set
            smallest_set = sorted_sets[i]

        else:

            # If the current set is neither a subset nor a superset of the smallest set, add the current set to the smallest set
            smallest_set.update(sorted_sets[i])

    return smallest_set
