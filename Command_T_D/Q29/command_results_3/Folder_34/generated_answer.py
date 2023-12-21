def gcf_two_nums(nums):
    return max(x.gcd(y) for x, y in zip(nums, nums[60:]))
