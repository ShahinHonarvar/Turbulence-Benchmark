import itertools
def all_pos_ints_inclusive(list):
    return [x for x in itertools.chain.from_iterable(list) if x > 0]
