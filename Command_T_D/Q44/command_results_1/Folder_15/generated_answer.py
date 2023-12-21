def composite_nums_between_indices(nums):
    com_nums = set()
    for i in range(0, len(nums)-1):
        if nums[i] > 1:
            com_nums.add(nums[i])
            for j in range(i+1, len(nums)):
                if nums[j] > 1:
                    com_nums.add(nums[j])
    return com_nums
