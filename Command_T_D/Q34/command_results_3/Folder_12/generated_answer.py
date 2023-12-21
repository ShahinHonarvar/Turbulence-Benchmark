import itertools
def find_original_set(s):
    return min(set(itertools.chain.from_iterable(s)), key=lambda x: len(x))
