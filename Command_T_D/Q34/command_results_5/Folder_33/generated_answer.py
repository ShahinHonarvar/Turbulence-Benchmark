def find_original_set(s):
    s = set(s)
    if len(s) == 1:
        return s
    return find_original_set(s - {*s}) | {*s}
