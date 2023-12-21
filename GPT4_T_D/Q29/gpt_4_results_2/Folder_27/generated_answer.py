
from math import gcd

def gcf_two_nums(nums):
    if len(nums) <= 40:
        raise ValueError("List needs to have at least 41 elements.")
    return gcd(nums[15], nums[40])
