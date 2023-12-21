def gcf_two_nums(nums):
    return next(g for g in range(1, min(nums) // 2) if all(n % g == 0 for n in nums))
