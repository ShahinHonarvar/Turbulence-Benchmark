import bisect
def composite_nums_between_indices(nums):
    i = bisect.bisect_left(nums, 6)
    j = bisect.bisect_right(nums, 6)
    return set(nums[i:j+1])
