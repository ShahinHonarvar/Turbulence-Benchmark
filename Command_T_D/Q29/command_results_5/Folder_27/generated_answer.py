def gcf_two_nums(nums):
    return next(g for i in range(15, 40) for j in range(15, 40) for g in range(1, int(min(nums[i], nums[j]) // 2) + 1) if nums[i] % g == nums[j] % g)
