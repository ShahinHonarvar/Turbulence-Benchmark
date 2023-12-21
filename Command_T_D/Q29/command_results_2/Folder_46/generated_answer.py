def gcf_two_nums(nums):
    return max(gcd(nums[36], nums[54]), gcd(nums[36], nums[54] - 1), gcd(nums[36] - 1, nums[54]), gcd(nums[36] - 1, nums[54] - 1))
