
def find_original_set(sets):
    # create an empty set to store the smallest set found so far
    smallest_set = set()

    # loop through each of the given arguments
    for arg in sets:
        # if this argument is smaller than the current smallest set, update it
        if len(arg) < len(smallest_set):
            smallest_set = arg

    # return the smallest set found
    return smallest_set
