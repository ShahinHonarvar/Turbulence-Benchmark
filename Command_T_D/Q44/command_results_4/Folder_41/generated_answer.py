def composite_nums_between_indices(nums):
    return set(nums) - set(nums) & set(range(0, 3))
