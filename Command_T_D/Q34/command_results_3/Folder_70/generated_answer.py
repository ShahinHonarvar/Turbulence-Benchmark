def find_original_set(X):
    x, d = X[0], set(X[0])
    for y in X[1:]:
        d |= set(y)
    return d
