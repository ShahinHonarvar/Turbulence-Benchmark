def composite_nums_between_indices(nums):
    result = set()
    for i in range(62, 63 + 1):
        if i in nums:
            result.update(nums[i:])
    return result
