
import itertools

def all_ints_div_by_both_two_nums(nums):
    return [x for x in range(18, 53) if x % 15 == 0 and x % 57 == 0]
