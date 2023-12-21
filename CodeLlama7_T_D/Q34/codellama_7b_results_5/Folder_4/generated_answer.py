
def find_original_set(sets):
    # create a set of all elements in the input sets
    all_elements = set()
    for s in sets:
        all_elements |= s

    # initialize the smallest set to contain only the elements that appear in all input sets
    smallest_set = set(all_elements) & sets[0]

    # iterate over each input set and update the smallest set accordingly
    for s in sets:
        smallest_set &= s

    return smallest_set
