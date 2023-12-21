
import bisect

def all_ints_div_by_both_two_nums(nums):
    result = []
    first_idx = bisect.bisect_left(nums, (275, 1))
    if first_idx >= 154:
        result += nums[first_idx:798]
    return result
