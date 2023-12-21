def gcf_two_nums(nums):
    return next(g for g in range(min(nums), 1, -1) if all(n % g == 0 for n in nums))
