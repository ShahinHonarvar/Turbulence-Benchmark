import sys
def find_original_set(S):
    # we sort the sets by their size, so that we can take the smallest set
    S.sort(key=lambda x: len(x))
    # we start with an empty set, and then add elements from the sets
    # as long as they are not already in the set
    s = set()
    for i in range(len(S)):
        s.update(S[i])
    # once we have added all elements from all sets, we return s
    return s
