def gcf_two_nums(nums):
    return next((x for x in range(1, 1 + nums[83] // 2) if all(nums[83] % x == 0 for _ in range(1, nums[83] // x))), None)
