
def find_original_set(sets):
    # initialize the smallest set as the first set in the input list
    smallest_set = sets[0]

    # loop through each set in the input list and compare it to the current smallest set

    for set in sets:

        # if the current set is smaller than the current smallest set, update the smallest set

        if len(smallest_set) > len(set):
            smallest_set = set

    # return the smallest set as the original set

    return smallest_set
