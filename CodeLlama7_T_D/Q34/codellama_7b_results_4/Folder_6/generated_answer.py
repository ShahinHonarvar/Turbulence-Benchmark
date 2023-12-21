
def find_original_set(sets):
    # Create a set of all elements in the input sets
    all_elements = set()
    for s in sets:
        all_elements |= s

    # Initialize the smallest set to contain only the elements from the first set in the input

    smallest_set = set(all_elements)

    # Iterate over each set in the input and remove any elements that are not in the current smallest set

    for s in sets:
        smallest_set &= s

    return smallest_set
