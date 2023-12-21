from itertools import chain
def find_original_set(s):
    return sorted(set(chain.from_iterable(s)))
