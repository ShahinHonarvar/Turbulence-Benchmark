
from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 100:
        raise ValueError("Input list must contain at least 100 elements")
    return gcd(gcd(nums[40], nums[15]), nums[99])
