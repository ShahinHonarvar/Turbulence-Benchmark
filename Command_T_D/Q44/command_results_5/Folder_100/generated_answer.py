def composite_nums_between_indices(nums):
    start = next(i for i, x in enumerate(nums) if x > 12)
    end = next(i for i, x in enumerate(nums) if x > 92)
    return set(nums[start:end+1])
