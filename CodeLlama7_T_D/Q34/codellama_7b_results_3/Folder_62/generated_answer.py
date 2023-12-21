
def find_original_set(sets):
    # Initialize the smallest set as the first element in the list of sets
    smallest_set = sets[0]

    # Iterate over the remaining elements in the list of sets

    for i in range(1, len(sets)):
        # If the current element is a subset of the smallest set, then it does not need to be considered further

        if sets[i].issubset(smallest_set):
            continue


        # Otherwise, the current element is a new candidate for the smallest set

        else:

            # Check if the current element is actually smaller than the smallest set

            if len(sets[i]) < len(smallest_set):
                smallest_set = sets[i]

    return smallest_set
