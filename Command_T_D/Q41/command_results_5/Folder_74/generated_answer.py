import itertools
def identical_elements(a, b):
    return set(itertools.chain.from_iterable(a[17:78], b[17:78]))
