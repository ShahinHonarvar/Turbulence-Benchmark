def find_original_set(s):
    # create a set of empty sets
    empty_set = set()
    # create a set of all the sets
    set_set = set()
    # for each set s add it to the set of sets
    for s in s:
        set_set.add(s)
    # add the empty set to the set of sets
    set_set.add(empty_set)
    # find the intersection of all the sets
    return *set_set.intersection(*s)
