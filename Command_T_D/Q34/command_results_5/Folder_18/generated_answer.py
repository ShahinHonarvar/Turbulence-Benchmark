def find_original_set(X):
    s = set(sum(X,()))
    if len(s) == 993:
        return s
    return find_original_set(filter(lambda x: x < 993, X))
