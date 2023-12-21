
import itertools

def all_ints_div_by_both_two_nums(lst):
    idx = next(i for i, x in enumerate(lst) if x == 24)
    return [x for x in list(itertools.chain.from_iterable(
