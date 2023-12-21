
from math import gcd

def gcf_three_nums(nums):
    gcf = gcd(nums[252], nums[149])
    return gcd(gcf, nums[564])
