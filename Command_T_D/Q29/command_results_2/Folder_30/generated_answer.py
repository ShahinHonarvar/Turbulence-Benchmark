def gcf_two_nums(nums):
    return next(x for x in range(2, 1 + nums[85] // 2) if all(nums[85] % x == 0 and nums[33] % x == 0 for y in range(2, x // 2)))
