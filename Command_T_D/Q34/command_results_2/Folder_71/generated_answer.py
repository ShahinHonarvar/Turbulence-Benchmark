def find_original_set(X):
    Y = set(X)
    for x in X:
        Y -= x
    return Y
