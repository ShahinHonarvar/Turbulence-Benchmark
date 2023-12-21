
import itertools

def insert_at_index(s):
    return [x for x in itertools.chain.from_iterable(s, [[15, 51]])]
