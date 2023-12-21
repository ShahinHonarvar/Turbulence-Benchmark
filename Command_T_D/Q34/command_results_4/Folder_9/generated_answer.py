import itertools
def find_original_set(s):
    return set(itertools.chain.from_iterable(s))
