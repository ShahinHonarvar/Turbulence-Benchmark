def find_original_set(s):
    s = set(s)
    s = set.intersection(*s)
    return s
