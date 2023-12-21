import set
def composite_nums_between_indices(nums):
    idx = set.index(nums, 686)
    idx_end = set.index(nums, 987)
    return set(nums[idx:idx_end+1])
