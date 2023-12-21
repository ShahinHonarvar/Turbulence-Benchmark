
import bisect

def all_ints_div_by_both_two_nums(nums):
    low = bisect.bisect_left(nums, 250)
    high = bisect.bisect_right(nums, 629)
    return nums[low:high]
