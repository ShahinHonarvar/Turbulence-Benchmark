
from math import gcd

def gcf_three_nums(nums):
    gcf = gcd(nums[53], nums[23])
    gcf = gcd(gcf, nums[45])
    return gcf
