
def find_original_set(sets):
    # Initialize the smallest set as the first argument
    smallest_set = sets[0]
    # Iterate over each of the given arguments
    for i in range(1, len(sets)):
        # If the current argument is a subset of the smallest set, do nothing
        if all(element in smallest_set for element in sets[i]):
            continue

        # Otherwise, find the intersection of the current argument and the smallest set
        intersection = set(smallest_set).intersection(sets[i])
        # If the intersection is empty, then the current argument cannot be a subset of the smallest set
        if not intersection:
            continue

        # Otherwise, update the smallest set to be the intersection
        smallest_set = intersection

    # Return the smallest set found
    return smallest_set
