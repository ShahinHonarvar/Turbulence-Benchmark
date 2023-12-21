
def find_original_set(sets):
    # Check if all sets are distinct and have the same size
    if len(set(map(len, sets))) != 1:
        raise ValueError("All sets must be of the same size")
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]
    # Iterate over each set and find the intersection with the smallest set
    for i in range(1, len(sets)):
        intersection = smallest_set.intersection(sets[i])
        # If the intersection is not empty, update the smallest set
        if intersection:
            smallest_set = intersection

    return smallest_set
