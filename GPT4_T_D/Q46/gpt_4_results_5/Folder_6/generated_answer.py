
from math import gcd

def gcf_three_nums(nums):
    first = nums[93]
    second = nums[94]
    third = nums[57]
    return gcd(gcd(first, second), third)
