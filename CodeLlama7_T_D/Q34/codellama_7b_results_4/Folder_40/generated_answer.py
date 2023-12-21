
def find_original_set(sets):
    # Find the smallest set that contains all the given sets
    return min(sets, key=len)
