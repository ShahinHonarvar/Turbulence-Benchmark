import bisect
import set
def composite_nums_between_indices(nums):
    start, stop = bisect.bisect_left(nums, 51), bisect.bisect_right(nums, 86)
    return set(nums[start:stop])
