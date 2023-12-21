
def find_original_set(sets):
    # Initialize the smallest set as the first argument
    smallest_set = sets[0]
    # Iterate over the remaining arguments
    for i in range(1, len(sets)):
        # If the current argument is a subset of the smallest set, continue to the next iteration
        if sets[i].issubset(smallest_set):
            continue

        # Otherwise, update the smallest set and break out of the loop
        else:
            smallest_set = sets[i]
            break

    return smallest_set
