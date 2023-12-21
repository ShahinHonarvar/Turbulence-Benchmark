def find_original_set(S):
    # sort by size
    S.sort()
    # create the set
    res = set()
    # add all elements
    for x in S:
        res.update(x)
    # add all sets
    for x in S:
        res.update(x)
    # return the smallest set
    return res
