
import bisect

def all_ints_div_by_both_two_nums(nums):
    return bisect.bisect_left(nums, 88*2) + bisect.bisect_left(nums, 58*2)
