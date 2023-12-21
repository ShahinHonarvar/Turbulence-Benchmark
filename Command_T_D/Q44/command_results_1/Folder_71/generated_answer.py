def composite_nums_between_indices(nums):
    result = set()
    for i in range(59, 97):
        if nums[i] > 1:
            result.add(nums[i])
    return result
