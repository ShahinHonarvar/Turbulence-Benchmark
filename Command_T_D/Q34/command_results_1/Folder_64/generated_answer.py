def find_original_set(s1, s2, s3, s4, s5, s6, s7):
    # sort all sets in ascending order
    sets = sorted(s1, s2, s3, s4, s5, s6, s7)
    # create a list of all unique elements in the sets
    elements = set()
    for s in sets:
        elements.update(s)
    # return the smallest set such that each of the given arguments is a subset of it
    return elements
