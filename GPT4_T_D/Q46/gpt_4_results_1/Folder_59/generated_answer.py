
from math import gcd

def gcf_three_nums(nums):
    gcf = gcd(gcd(nums[6], nums[7]), nums[8])
    return gcf
