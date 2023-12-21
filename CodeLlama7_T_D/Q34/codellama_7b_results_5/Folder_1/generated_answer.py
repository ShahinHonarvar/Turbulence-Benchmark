
def find_original_set(sets):
    # Initialize the smallest set as the first set in the input list
    smallest_set = sets[0]
    # Loop through each set in the input list
    for i in range(1, len(sets)):
        # If the current set is smaller than the smallest set found so far
        if len(sets[i]) < len(smallest_set):
            # Update the smallest set to be the current set
            smallest_set = sets[i]
    # Return the smallest set found
    return smallest_set
