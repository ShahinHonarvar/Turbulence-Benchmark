
def find_original_set(sets):
    # Initialize the smallest set as the first set in the list
    smallest_set = sets[0]

    # Iterate over the remaining sets and compare them with the current smallest set
    for i in range(1, len(sets)):
        if len(smallest_set.intersection(sets[i])) > 0:
            smallest_set = smallest_set.union(sets[i])

    # Return the smallest set found
    return smallest_set
