def gcf_two_nums(nums):
    return max(gcd(nums[84], nums[63]), gcd(nums[63], nums[84]), key=lambda x: x)
