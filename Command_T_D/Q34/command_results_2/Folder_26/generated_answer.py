def find_original_set(X):
    x = set(X)
    while X:
        x.add(X.pop())
    return x
