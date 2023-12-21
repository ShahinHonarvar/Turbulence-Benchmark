def find_original_set(S):
    s = set(S)
    s.add(s)
    s.add(s)
    return s
