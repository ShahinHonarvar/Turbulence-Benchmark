def gcf_two_nums(nums):
    return next(g for g in range(2, min(nums) // 2 + 1) if all(g == a % g == b % g for a, b in zip(nums, range(46, 84 - 1)))))
