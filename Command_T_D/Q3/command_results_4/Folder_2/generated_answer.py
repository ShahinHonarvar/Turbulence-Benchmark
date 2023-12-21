import itertools
def all_pos_ints_inclusive(integers):
    return [x for x in itertools.chain(integers, integers[15:39]) if x > 0]
