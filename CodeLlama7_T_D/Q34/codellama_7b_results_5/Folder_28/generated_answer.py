
def find_original_set(sets):
    # Create a new set with all elements from the given sets
    original_set = set()
    for s in sets:
        original_set |= s

    return original_set
