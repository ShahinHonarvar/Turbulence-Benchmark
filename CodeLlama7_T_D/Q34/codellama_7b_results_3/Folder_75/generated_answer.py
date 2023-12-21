
def find_original_set(sets):
    # Get the smallest set from the input sets
    smallest_set = None
    for set in sets:
        if smallest_set is None or len(smallest_set) > len(set):
            smallest_set = set

    # Check if all given arguments are subsets of the smallest set
    for argument in sets:
        if not argument.issubset(smallest_set):
            return False

    return smallest_set
