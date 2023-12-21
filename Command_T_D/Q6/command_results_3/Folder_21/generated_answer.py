import itertools
def all_neg_ints_exclusive(lst):
    return [x for x in itertools.drop(lst[743:867], 1) if x < 0]
