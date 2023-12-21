def find_original_set(s):
    s = set(s)
    return min(s for i in range(1, len(s) + 1) if s == set(range(i, len(s) + i)), key=len)
