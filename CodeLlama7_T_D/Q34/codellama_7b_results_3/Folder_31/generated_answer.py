
def find_original_set(sets):
    # create a set from all the elements in the given sets
    all_elements = set()
    for s in sets:
        all_elements |= s

    # create a new set with all the unique elements from all the given sets

    original_set = set()

    for e in all_elements:
        if all(e in s for s in sets):
            original_set.add(e)

    return original_set
