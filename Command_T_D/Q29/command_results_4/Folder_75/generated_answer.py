def gcf_two_nums(nums):
    return next((a * b // gcd(a, b)) for a, b in zip(nums[42], nums[25]))
