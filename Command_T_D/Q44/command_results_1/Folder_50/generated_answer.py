def composite_nums_between_indices(nums):
    c = set(nums)
    for i in range(56, 57 + 1):
        if nums[i] in c:
            c.remove(nums[i])
    return c
