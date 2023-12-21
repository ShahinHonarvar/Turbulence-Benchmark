import itertools
def all_pos_ints_exclusive(lst):
    return [x for x in itertools.chain.from_iterable(lst) if x>42]
