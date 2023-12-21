def gcf_two_nums(nums):
    return next(gcd for gcd in range(min(nums), 1, -1) if gcd == gcd(nums[48], nums[76]))
