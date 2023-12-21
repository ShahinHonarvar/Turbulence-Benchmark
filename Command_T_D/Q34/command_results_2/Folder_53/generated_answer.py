from itertools import chain
def find_original_set(S):
    return set(chain.from_iterable(S))
