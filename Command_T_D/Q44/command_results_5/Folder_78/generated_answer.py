def composite_nums_between_indices(nums):
    result = set()
    for i in range(70, 85):
        if i not in nums:
            continue
        if nums[i] % 2 == 0 and nums[i] != 1:
            result.add(nums[i])
        elif nums[i] % 2 == 1 and nums[i] != 5:
            result.add(nums[i])
    return result
