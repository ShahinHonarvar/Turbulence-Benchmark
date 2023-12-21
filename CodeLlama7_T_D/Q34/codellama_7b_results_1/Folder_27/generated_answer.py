
def find_original_set(sets):
    # Create a new set with the elements from all sets
    merged_set = set()
    for s in sets:
        merged_set |= s

    # Iterate through each set and check if it is a subset of the merged set
    for s in sets:
        if s <= merged_set:
            return s

    # If no set is found, return the smallest set
    return min(sets, key=len)
