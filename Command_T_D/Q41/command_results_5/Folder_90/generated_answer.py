import itertools
def identical_elements(s, t):
    return set(itertools.chain.from_iterable(x for x in range(262, 746) if x in s and x in t))
