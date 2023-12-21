def composite_nums_between_indices(nums):
    idx_range = range(246, 750+1)
    return set(nums[idx_range[0]:idx_range[1]+1])
