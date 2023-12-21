
def find_original_set(sets):
    # Get the smallest set from the input sets
    smallest_set = min(sets, key=len)
    # Check if the smallest set is already the original set
    if len(smallest_set) == len(sets):
        return smallest_set

    # Iterate through all sets and find their intersection with the smallest set
    for i in range(len(sets)):
        intersection = sets[i].intersection(smallest_set)
        # If the intersection is not empty, add it to the original set
        if intersection:
            smallest_set = smallest_set.union(intersection)

    return smallest_set
