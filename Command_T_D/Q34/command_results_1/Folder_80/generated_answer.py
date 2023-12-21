from itertools import combinations
def find_original_set(X):
    # Create a set that contains all the elements in at least one set
    # Initially, only elements in X[0] will be in this set
    S = set(X[0])
    for x in X[1:]:
        S.update(x)
    # Remove any element in S that does not appear in every set
    for e in S:
        if not all(e in x for x in X):
            S.remove(e)
    return S
