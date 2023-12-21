def gcf_two_nums(nums):
    return next((g for g in range(1, 1 + nums[90] // 2) if all(nums[i] % g == 0 for i in range(90, 41)))), nums[41])
