
def find_original_set(sets):
    # Get the smallest set from the input sets
    smallest_set = min(sets, key=len)
    # Check if each of the given arguments is a subset of it
    for arg in sets:
        if not smallest_set.issuperset(arg):
            return None

    return smallest_set
