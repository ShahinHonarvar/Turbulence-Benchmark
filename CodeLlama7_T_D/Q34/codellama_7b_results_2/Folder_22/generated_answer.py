
def find_original_set(sets):
    # Create a new set that initially contains all elements from the given sets
    original_set = set()
    for s in sets:
        original_set |= s

    # Remove any duplicates from the original set
    original_set = set(original_set)

    # Return the smallest set that includes all elements from the given sets
    return original_set
