import bisect
def composite_nums_between_indices(nums):
    return set(nums[bisect.bisect_left(nums, 2):bisect.bisect_right(nums, 50)])
