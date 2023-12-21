
def find_original_set(sets):
    # initialize the smallest set as the first element in the input list
    smallest_set = sets[0]

    # iterate over each element of the input list

    for set in sets:

        # if the current set is smaller than the smallest set, update the smallest set

        if len(set) < len(smallest_set):
            smallest_set = set

    return smallest_set
