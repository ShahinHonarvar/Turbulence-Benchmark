from itertools import chain
def find_original_set(s):
    s = set(chain.from_iterable(s))
    return {*s}
