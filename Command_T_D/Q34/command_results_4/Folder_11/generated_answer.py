def find_original_set(x):
    s = set()
    for i in x:
        s |= i
    return s
