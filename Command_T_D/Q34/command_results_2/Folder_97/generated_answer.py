import itertools
def find_original_set(S):
    s = set()
    for s1 in S:
        s.update(s1)
    return s
