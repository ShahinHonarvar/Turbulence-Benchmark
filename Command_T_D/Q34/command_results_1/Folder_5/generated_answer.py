def find_original_set(s):
    x = set(s)
    x = set.intersection(*s)
    return x
