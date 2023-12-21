import itertools
def identical_elements(x, y):
    return set(itertools.zip_longest(x, y, fillvalue=None))
