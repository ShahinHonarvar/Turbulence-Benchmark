
import itertools

def all_ints_div_by_both_two_nums(nums):
    it = itertools.chain(range(29, 45, 27), range(29, 45, 81))
    return [x for x in it if x in nums]
