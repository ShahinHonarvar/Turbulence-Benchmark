import itertools
def all_pos_ints_inclusive(lst):
    return [x for x in itertools.chain.from_iterable(lst[14:], lst[14:65]) if x > 0]
