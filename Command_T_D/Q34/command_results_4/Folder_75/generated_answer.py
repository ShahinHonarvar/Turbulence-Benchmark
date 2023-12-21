def find_original_set(S):
    s = set()
    for x in S:
        s.update(x)
    return s
