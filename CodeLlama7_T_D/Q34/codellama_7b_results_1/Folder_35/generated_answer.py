
def find_original_set(sets):
    # Initialize the smallest set as the first element in the input list
    smallest_set = sets[0]

    # Iterate over the remaining elements in the input list
    for i in range(1, len(sets)):
        # If the current element is a subset of the smallest set, then we don't need to do anything
        if all(x in smallest_set for x in sets[i]):
            continue

        # Otherwise, check if the current element is a subset of any of the elements in the smallest set
        for j in range(len(smallest_set)):
            # If the current element is a subset of one of the elements in the smallest set, then we don't need to do anything
            if all(x in smallest_set[j] for x in sets[i]):
                break

        # If the current element is not a subset of any of the elements in the smallest set, then we update the smallest set with the current element
        else:
            smallest_set = sets[i]

    # Return the smallest set

    return smallest_set
