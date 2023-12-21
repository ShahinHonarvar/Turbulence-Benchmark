def composite_nums_between_indices(nums):
    return set(nums) & set(range(min(nums), max(nums) + 1))
