from itertools import chain
def find_original_set(X):
    return set(chain.from_iterable(X))
