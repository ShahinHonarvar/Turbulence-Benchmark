def find_original_set(X):
    return set(sorted(set(sum(x for x in X), key=lambda x: x)))
