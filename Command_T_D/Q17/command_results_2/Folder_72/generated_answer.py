
import bisect

def all_ints_div_by_both_two_nums(nums):
    return nums[bisect.bisect_left(nums[38:81], -61*2):bisect.bisect_right(nums[38:81], -71*2)]
