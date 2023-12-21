
from math import gcd

def gcf_three_nums(nums):
    a, b, c = nums[252], nums[149], nums[564]
    return gcd(gcd(a, b), c)
