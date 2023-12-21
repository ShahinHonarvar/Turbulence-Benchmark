import itertools
def find_original_set(X):
    return set(itertools.chain.from_iterable(X))
