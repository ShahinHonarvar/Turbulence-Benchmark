
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]

    # Iterate over each set in the input list and compare with the current smallest set

    for i in range(1, len(sets)):
        if len(smallest_set.intersection(sets[i])) > 0:
            smallest_set = smallest_set.union(sets[i])

    return smallest_set
