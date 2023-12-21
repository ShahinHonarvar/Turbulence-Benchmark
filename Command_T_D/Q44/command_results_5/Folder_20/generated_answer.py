def composite_nums_between_indices(nums):
    return set(nums[74:95]) & set(nums[0:74]) & set(nums[95:])
