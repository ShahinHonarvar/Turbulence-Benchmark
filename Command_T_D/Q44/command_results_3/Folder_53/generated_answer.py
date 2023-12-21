import bisect
def composite_nums_between_indices(nums):
    start_idx = bisect.bisect_left(nums,222)
    end_idx = bisect.bisect_right(nums,222)
    return set(nums[start_idx:end_idx])
