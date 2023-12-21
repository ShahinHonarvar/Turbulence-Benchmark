
from math import gcd

def gcf_three_nums(nums):
    gcf = gcd(nums[14], nums[21])
    gcf = gcd(gcf, nums[17])
    return gcf
