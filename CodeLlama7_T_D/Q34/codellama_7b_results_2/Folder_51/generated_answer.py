
def find_original_set(sets):
    # initialize the smallest set as the first set in the input
    smallest_set = sets[0]
    # loop through each set in the input and compare it to the smallest set found so far
    for set in sets:
        # if the current set is smaller than the smallest set found so far, update the smallest set
        if len(set) < len(smallest_set):
            smallest_set = set

    return smallest_set
