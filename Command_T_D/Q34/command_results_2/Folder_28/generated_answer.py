def find_original_set(s):
    res = set()
    for e in s:
        res |= e
    return res
