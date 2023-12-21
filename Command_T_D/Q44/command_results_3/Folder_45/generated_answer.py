def composite_nums_between_indices(nums):
    result = set()
    for i in range(40, 200):
        if nums[i] % 2 == 0 and nums[i] != 1:
            result.add(nums[i])
    return result
