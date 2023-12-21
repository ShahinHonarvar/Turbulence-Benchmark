def find_original_set(X):
    return set(min(set(Y), key=len)) for Y in X
