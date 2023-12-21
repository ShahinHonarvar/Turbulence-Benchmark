def gcf_two_nums(nums):
    return next((x * y // gcd(x, y)) for x, y in zip(nums[872], nums[219]) if gcd(x, y) > 1)
