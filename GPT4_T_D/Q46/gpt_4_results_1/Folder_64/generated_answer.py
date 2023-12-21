
from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 9:
        return "List is too small. Need at least 9 elements."

    return gcd(gcd(nums[0], nums[8]), nums[3])
