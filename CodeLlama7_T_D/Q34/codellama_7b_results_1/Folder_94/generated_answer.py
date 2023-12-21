
def find_original_set(sets):
    # Initialize the smallest set to the first element in the input sets
    smallest_set = sets[0]

    # Iterate over each set in the input and compare it to the smallest set found so far

    for current_set in sets:
        if len(current_set) < len(smallest_set):
            smallest_set = current_set

    # Return the smallest set found

    return smallest_set
