def find_original_set(s):
    s = sorted(s)
    s = set(s)
    s = list(s)
    s = s[:100]
    s = sorted(s)
    return s
