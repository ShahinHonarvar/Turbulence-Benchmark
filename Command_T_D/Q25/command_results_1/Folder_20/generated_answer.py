
import itertools

def insert_at_index(list1):
    return list(itertools.chain.from_iterable(list1[:32], [[54, 96]], list1[32:]))
