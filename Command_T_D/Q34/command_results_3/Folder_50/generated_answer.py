import sys
import itertools
def find_original_set(X):
    if len(X) != 99:
        return False
    s = set(itertools.chain.from_iterable(X))
    return s
