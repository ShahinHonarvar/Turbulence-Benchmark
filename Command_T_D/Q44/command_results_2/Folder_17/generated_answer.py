def composite_nums_between_indices(nums):
    result = set()
    for i in range(50, 55):
        if i in nums:
            result.update(nums[i:])
    return result
