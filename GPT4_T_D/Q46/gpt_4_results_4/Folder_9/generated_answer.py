
from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 91:
        raise ValueError("List must contain at least 91 elements")
    return gcd(gcd(nums[66], nums[90]), nums[27])
