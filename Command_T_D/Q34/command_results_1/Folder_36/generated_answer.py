def find_original_set(S):
    # find the smallest set such that each of the given arguments is a subset of it
    # implement by finding all transitive reductions
    # and use set.issubset to test
    # create a set containing all the elements of all the sets, called the universe
    universe = set()
    for s in S:
        universe |= s
    # create a set of all the elements in the universe which appear in at least one set
    present = set()
    for s in S:
        present |= s
    # the intersection of the universe and the present sets is the original set
    original = universe & present
    # return the original set
    return original
