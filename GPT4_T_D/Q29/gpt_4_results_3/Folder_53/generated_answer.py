
import math

def gcf_two_nums(nums):
    if len(nums) <= max(28, 67):
        raise ValueError("The list must contain at least 68 elements.")
    return math.gcd(nums[28], nums[67])
