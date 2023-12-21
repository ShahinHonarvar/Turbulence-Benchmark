
import itertools

def all_ints_div_by_both_two_nums(lst):
    return [x for x in range(56, 89) if all(x%d==0 for d in (-59, -79))]
