def find_original_set(x):
    x = set(x)
    return min(x, key=len)
