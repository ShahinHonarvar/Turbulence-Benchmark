
def find_original_set(sets):
    # Create a set of all elements in the given sets
    all_elements = set()
    for s in sets:
        all_elements |= s

    # Initialize the smallest set to be the first set in the input list

    smallest_set = sets[0]

    # Loop through each of the given sets and find the smallest set that contains all elements from the current set

    for i in range(1, len(sets)):

        current_set = sets[i]

        # If the current set is a subset of the smallest set, then we do not need to update the smallest set

        if current_set <= smallest_set:
            continue


        # Otherwise, we need to check if the current set contains all elements from the smallest set

        elif all_elements - current_set == smallest_set:
            smallest_set = current_set

    return smallest_set
