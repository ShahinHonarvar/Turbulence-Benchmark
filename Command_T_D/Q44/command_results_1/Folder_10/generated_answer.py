def composite_nums_between_indices(nums):
    com_nums = set()
    for i in range(37, 51):
        if i not in nums:
            continue
        if nums[i] % 2 == 0 and nums[i] % 3 == 0 and nums[i] % 5 == 0 and nums[i] % 7 == 0:
            com_nums.add(nums[i])
    return com_nums
