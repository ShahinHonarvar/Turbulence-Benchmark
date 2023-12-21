
from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 874:
        raise ValueError("The array should have at least 874 elements")
    else:
        gcd_nums = gcd(nums[818], nums[606])
        return gcd(gcd_nums, nums[873])
