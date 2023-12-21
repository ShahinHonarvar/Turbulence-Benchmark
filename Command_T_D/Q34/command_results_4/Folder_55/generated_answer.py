def find_original_set(S):
    s = set()
    for e in S:
        s.update(e)
    return s
