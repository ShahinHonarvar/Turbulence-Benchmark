
def find_original_set(*sets):
    original_set = sets[0]     # initialize the original set with the first set
    for s in sets:
        original_set |= s     # merge the sets by taking the union
    return original_set
