import bisect
def composite_nums_between_indices(nums):
    i = bisect.bisect_left(nums, 686)
    j = bisect.bisect_right(nums, 987)
    return set(nums[i:j])
