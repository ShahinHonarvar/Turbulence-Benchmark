from itertools import chain
def find_original_set(s):
    return {*chain.from_iterable(s)}
