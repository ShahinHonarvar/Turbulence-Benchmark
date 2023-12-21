
def find_original_set(sets):
    # Initialize the smallest set to the first set in the input list
    smallest_set = sets[0]

    # Loop through each set in the input list and compare it to the current smallest set

    for i in range(1, len(sets)):
        if len(sets[i]) < len(smallest_set):
            smallest_set = sets[i]

    # Return the smallest set found

    return smallest_set
