
def find_original_set(sets):
    # Create a set from all the elements in the given sets
    merged_set = set()
    for s in sets:
        merged_set |= s

    # Initialize a variable to keep track of the smallest set

    smallest_set = None

    # Iterate over each of the given sets and check if it is a subset of the smallest set found so far

    for s in sets:

        if smallest_set is None or s <= smallest_set:
            smallest_set = s

    return smallest_set
