def find_original_set(X):
    s = set(X)
    for x in X:
        s &= x
    return s
