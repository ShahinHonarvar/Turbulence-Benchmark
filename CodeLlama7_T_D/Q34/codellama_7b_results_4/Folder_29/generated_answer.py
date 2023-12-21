
def find_original_set(sets):
    # create an empty set to store the original sets
    original_sets = set()

    # loop through each of the given arguments
    for argument in sets:

        # add each of the elements from the current argument to the original_sets set
        original_sets.update(argument)

    # return the smallest set such that each of the given arguments is a subset of it
    return min(original_sets, key=len)
