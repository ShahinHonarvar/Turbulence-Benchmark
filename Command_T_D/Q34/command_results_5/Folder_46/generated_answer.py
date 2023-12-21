import itertools
def find_original_set(S):
    # create the sets from the sets
    A = set(sum(set(x) for x in S))
    # create the sets from the sets
    B = set(sum(set(y) for y in S))
    # return the union of A and B
    return A | B
