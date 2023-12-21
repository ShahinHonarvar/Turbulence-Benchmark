import bisect
def composite_nums_between_indices(nums):
    return set(nums[bisect.bisect_left(nums, 12) : bisect.bisect_right(nums, 92)])
