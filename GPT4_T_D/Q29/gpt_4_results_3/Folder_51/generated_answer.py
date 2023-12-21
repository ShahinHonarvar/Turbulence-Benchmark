
from math import gcd

def gcf_two_nums(nums):
    if len(nums) > max(46, 84):
        return gcd(nums[46], nums[84])
