def find_original_set(s):
    # define a set that contains all elements of the original set
    original_set = set()
    # add elements from each set to the original set
    for x in s:
        original_set.update(x)
    # return the original set
    return original_set
