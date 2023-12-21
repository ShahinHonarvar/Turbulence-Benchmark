import itertools
def find_original_set(X):
    # x = list(itertools.permutations(X))
    # y = list(itertools.permutations(set(x)))
    # z = set(y)
    # return z
    return set(itertools.permutations(X))
