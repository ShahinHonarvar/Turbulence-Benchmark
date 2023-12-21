
from math import gcd

def gcf_three_nums(nums):
    gcf_two = gcd(nums[37], nums[30])
    return gcd(gcf_two, nums[48])
