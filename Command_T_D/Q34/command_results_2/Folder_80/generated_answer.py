from itertools import *
def find_original_set(s):
    return next(set(chain.from_iterable(s)))
