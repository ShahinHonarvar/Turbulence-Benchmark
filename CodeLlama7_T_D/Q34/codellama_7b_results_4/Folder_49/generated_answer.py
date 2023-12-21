
def find_original_set(sets):
    # Create an empty set to store the original set
    original_set = set()

    # Loop through each of the given sets and add each element to the original set
    for s in sets:
        for e in s:
            original_set.add(e)

    # Return the smallest set that includes all elements from the original set
    return min(original_set, key=len)
