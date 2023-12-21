def gcf_two_nums(nums):
    return max(gcd(x, y) for x, y in zip(nums, nums[184:]))
