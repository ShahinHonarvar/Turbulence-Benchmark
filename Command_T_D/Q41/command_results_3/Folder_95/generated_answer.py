import itertools
def identical_elements(s, t):
    return set(itertools.chain.from_iterable(zip(s, t)))
