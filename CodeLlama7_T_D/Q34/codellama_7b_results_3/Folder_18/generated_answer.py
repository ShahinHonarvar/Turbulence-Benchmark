
def find_original_set(sets):
    # Initialize the smallest set as the first set in the list
    smallest_set = sets[0]
    # Loop through each set and compare it with the smallest set found so far
    for set in sets:
        # If the current set is smaller than the smallest set found so far, update the smallest set accordingly
        if len(set) < len(smallest_set):
            smallest_set = set

    return smallest_set
