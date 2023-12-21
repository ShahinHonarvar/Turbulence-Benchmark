
import bisect

def all_ints_div_by_both_two_nums(nums):
    left_idx = bisect.bisect_left(nums, -553)
    right_idx = bisect.bisect_right(nums, -737)
    return nums[left_idx:right_idx+1]
