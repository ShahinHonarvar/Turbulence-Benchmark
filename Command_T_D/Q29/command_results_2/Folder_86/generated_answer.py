def gcf_two_nums(nums):
    return next(g for g in range(1, max(nums) // 2 + 1) if all(num % g == 0 for num in nums))
