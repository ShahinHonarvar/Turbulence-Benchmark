
def find_original_set(sets):
    # Initialize the smallest set as the first set in the input list
    smallest_set = sets[0]

    # Iterate over the remaining sets and update the smallest set if necessary

    for i in range(1, len(sets)):
        current_set = sets[i]
        if len(current_set) < len(smallest_set):
            smallest_set = current_set

    # Return the smallest set found

    return smallest_set
