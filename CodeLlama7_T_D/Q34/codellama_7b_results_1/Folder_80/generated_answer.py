
def find_original_set(sets):
    # Find the smallest set that contains all the given sets
    smallest = None
    for s in sets:
        if smallest is None or len(smallest) > len(s):
            smallest = s

    return smallest
