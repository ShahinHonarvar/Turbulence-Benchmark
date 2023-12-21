
from math import gcd

def gcf_three_nums(nums):
    if len(nums) > 99:
        return gcd(gcd(nums[40], nums[15]), nums[99])
    else:
        return "List does not have enough elements"
