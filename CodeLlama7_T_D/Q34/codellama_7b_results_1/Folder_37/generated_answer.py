
def find_original_set(sets):
    # create a new set with the elements from the first set
    original_set = sets[0].copy()
    # loop through each of the given arguments and add their elements to the original set
    for i in range(1, len(sets)):
        original_set.update(sets[i])
    return original_set
