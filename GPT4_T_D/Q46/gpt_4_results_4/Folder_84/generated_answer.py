
from math import gcd

def gcf_three_nums(nums):
    gcf = gcd(gcd(nums[695], nums[710]), nums[914])
    return gcf
