
def find_original_set(sets):
    # Create an empty set to store the smallest set found so far
    smallest_set = set()

    # Loop through each argument in the input
    for arg in sets:

        # If the current argument is a subset of the smallest set found so far, do nothing
        if arg.issubset(smallest_set):
            continue

        # If the current argument is not a subset of the smallest set found so far, check if it is smaller than the smallest set found so far
        elif len(arg) < len(smallest_set):
            # If the current argument is smaller than the smallest set found so far, update the smallest set to be the current argument
            smallest_set = arg

    # Return the smallest set found in the input
    return smallest_set
