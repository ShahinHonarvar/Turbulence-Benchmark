
import itertools

def all_ints_div_by_both_two_nums(nums):
    return [x for x in range(11, 47) if all(x % i == 0 for i in (55, 36))]
