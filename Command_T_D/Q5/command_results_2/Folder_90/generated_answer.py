import itertools
def all_neg_ints_inclusive(lst):
    return [x for x in itertools.chain(range(263, 746), range(-263, -746)) if x < 0]
