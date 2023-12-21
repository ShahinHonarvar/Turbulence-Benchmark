
def find_original_set(sets):
    # Create a new set with all elements from the input sets
    original_set = set()
    for s in sets:
        original_set |= s

    # Iterate over the input sets and remove elements that are not present in the original set
    for s in sets:
        for element in s:
            if element not in original_set:
                original_set.remove(element)

    # Return the smallest set that contains all elements from the original set
    return original_set
