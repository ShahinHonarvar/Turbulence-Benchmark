
import itertools

def all_ints_div_by_both_two_nums(lst):
    return [x for x in itertools.drop(lst[56:88], 1) if x % -59 == x % -79]
