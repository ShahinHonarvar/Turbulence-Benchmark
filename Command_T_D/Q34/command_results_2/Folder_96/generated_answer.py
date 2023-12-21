import sys
def find_original_set(X):
    s = set(X[0])
    for x in X[1:]:
        s |= set(x)
    return s
