
def find_original_set(sets):
    # Initialize an empty set
    original_set = set()

    # Iterate over the given sets and add their elements to the original set
    for s in sets:
        original_set |= s

    return original_set
