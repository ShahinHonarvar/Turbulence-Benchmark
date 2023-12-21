def find_original_set(S):
    s = set()
    for s1 in S:
        s = set.intersection(s, s1)
    return s
