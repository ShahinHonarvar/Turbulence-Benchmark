import itertools
def find_original_set(S):
    # Some sets are singletons, which can be handled by
    # making them the elements of the final set.
    # Other sets are larger.
    # The smallest set that contains all the other sets
    # will contain at least one element from each set,
    # so we can take the union of the sets to get the
    # smallest set.
    return set.union(*S)
