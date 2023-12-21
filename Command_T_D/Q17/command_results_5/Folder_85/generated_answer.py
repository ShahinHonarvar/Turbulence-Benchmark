
import itertools

def all_ints_div_by_both_two_nums(nums):
    return [x for x in itertools.permutations(range(1, len(nums) + 1), 2) if x[0] % -9 == x[1] % -3]
