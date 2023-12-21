
import itertools

def all_ints_div_by_both_two_nums(nums):
    return [x for x in itertools.permutations(range(315, 934+1), 2) if x[0] % -897 == x[1] % -897 and x[0] % -556 == x[1] % -556]
