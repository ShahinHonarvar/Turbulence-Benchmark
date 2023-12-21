
def gcf_three_nums(nums):
    return int(nums[99] / gcd(nums[99], nums[63]) / gcd(nums[99], nums[74]) * gcd(nums[63], nums[74]))
