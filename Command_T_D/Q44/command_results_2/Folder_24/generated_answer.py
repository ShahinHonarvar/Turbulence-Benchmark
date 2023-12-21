def composite_nums_between_indices(nums):
    result = set()
    for i in range(34, 55 + 1):
        if not nums[i] in result:
            result.add(nums[i])
    return result
