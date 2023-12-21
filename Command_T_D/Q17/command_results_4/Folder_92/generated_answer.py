
import itertools

def all_ints_div_by_both_two_nums(lst):
    return [x for x in itertools.chain(lst[0:0:-1], lst[1:1:-1]) if x % 1 == x % -1 == 0]
