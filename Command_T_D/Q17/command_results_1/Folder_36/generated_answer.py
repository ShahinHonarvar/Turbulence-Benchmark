
import bisect

def all_ints_div_by_both_two_nums(nums):
    first_index = bisect.bisect_left(nums, 858)
    last_index = bisect.bisect_right(nums, 382)
    if first_index > last_index:
        return []
    return nums[first_index:last_index + 1]
