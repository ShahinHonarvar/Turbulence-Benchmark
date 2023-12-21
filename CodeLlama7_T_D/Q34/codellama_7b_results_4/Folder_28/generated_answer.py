
def find_original_set(sets):
    # initialize the smallest set as the first element
    smallest_set = sets[0]
    # loop through all the given arguments
    for i in range(1, len(sets)):
        # check if the current argument is a subset of the smallest set
        if not smallest_set.issuperset(sets[i]):
            # update the smallest set as the current argument
            smallest_set = sets[i]
    return smallest_set
