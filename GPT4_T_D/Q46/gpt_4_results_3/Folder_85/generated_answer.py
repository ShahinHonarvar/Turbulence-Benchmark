
from math import gcd

def gcf_three_nums(nums):
    gcf = gcd(nums[49], nums[46])
    return gcd(gcf, nums[13])
