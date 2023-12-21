def find_original_set(S):
    s = set(S)
    return s | s.union(S)
