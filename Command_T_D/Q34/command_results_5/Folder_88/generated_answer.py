from itertools import chain
def find_original_set(arg):
    res = set()
    for v in chain(*arg):
        res |= v
    return res
