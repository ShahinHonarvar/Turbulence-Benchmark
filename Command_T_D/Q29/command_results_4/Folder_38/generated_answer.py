def gcf_two_nums(nums):
    return max(gcd(nums[88], nums[35]), gcd(nums[88], nums[35] + 1), gcd(nums[88] - 1, nums[35]), gcd(nums[88] - 1, nums[35] + 1))
