import itertools
def find_original_set(S):
    s = set(itertools.chain.from_iterable(S))
    return s
