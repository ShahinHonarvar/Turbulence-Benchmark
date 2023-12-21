
def find_original_set(sets):
    # Initialize the smallest set with the first argument
    smallest_set = sets[0]
    # Loop through the remaining arguments and compare them with the current smallest set
    for i in range(1, len(sets)):
        # If the current argument is a subset of the smallest set, continue to the next iteration
        if sets[i].issubset(smallest_set):
            continue

        # Otherwise, update the smallest set with the current argument
        smallest_set = sets[i]

    # Return the smallest set
    return smallest_set
