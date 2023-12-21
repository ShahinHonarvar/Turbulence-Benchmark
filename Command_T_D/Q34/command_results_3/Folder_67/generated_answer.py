from itertools import chain
def find_original_set(s):
    s = list(chain.from_iterable(s))
    s = set(s)
    s = sorted(s)
    return s
