import itertools
def identical_elements(x, y):
    return set(itertools.chain.from_iterable(zip(x, y)))
