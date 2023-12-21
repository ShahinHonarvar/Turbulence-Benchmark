def gcf_two_nums(nums):
    return max(nums[0] // gcd(nums[0], nums[9]), nums[9] // gcd(nums[0], nums[9]))
