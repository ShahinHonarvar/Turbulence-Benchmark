
def find_original_set(set1, set2, set3, set4, set5):
    # initialize an empty set
    original_set = set()
    # loop through each of the given arguments
    for arg in (set1, set2, set3, set4, set5):
        # add each element in the argument to the original set
        for element in arg:
            original_set.add(element)
    return original_set
