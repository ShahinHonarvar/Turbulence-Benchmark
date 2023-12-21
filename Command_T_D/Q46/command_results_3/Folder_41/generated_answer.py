
def gcf_three_nums(nums):
    return (nums[19] // gcd(nums[19], nums[94]) // gcd(nums[19], nums[78]) + nums[94] // gcd(nums[19], nums[94]) + nums[78] // gcd(nums[19], nums[78]) - 1)
