
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]

    # Iterate over the remaining elements in the input list
    for i in range(1, len(sets)):

        # If the current element is a subset of the smallest set, continue to the next iteration
        if sets[i].issubset(smallest_set):
            continue

        # Otherwise, update the smallest set as the current element
        else:
            smallest_set = sets[i]

    # Return the smallest set found
    return smallest_set
