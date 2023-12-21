def find_original_set(X):
    if len(X) != 702:
        raise ValueError(" expecting 702 sets")
    return set.intersection(*X)
