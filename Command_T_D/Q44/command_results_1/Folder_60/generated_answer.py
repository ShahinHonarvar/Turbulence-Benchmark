def composite_nums_between_indices(nums):
    result = set()
    for i in range(29, 51+1):
        if nums[i] > 1 and nums[i] != 2 and nums[i] != 3:
            result.add(nums[i])
    return result
