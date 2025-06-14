
def find_original_set(sets):
    # create a copy of the sets list
    original_sets = sets[:]
    # sort the lists in each set by length
    for set in sets:
        set.sort(key=len)
    # loop through the sorted lists and remove any duplicates
    while len(original_sets) > 0:
        set = original_sets[0]
        if set not in original_sets[1:]:
            original_sets.remove(set)
    return original_sets
