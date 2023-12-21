def find_original_set(s):
    l = set(range(1, 1 + 126))
    for x in s:
        l.update(x)
    return l
