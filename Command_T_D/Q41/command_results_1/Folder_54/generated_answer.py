import itertools
def identical_elements(A, B):
    return set(itertools.chain.from_iterable(zip(A, B)))
