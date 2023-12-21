def find_original_set(s):
    s = set(s)
    return min(s, key=len)
