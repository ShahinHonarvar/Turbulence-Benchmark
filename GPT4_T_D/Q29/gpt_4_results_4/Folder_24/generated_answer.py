
from math import gcd

def gcf_two_nums(nums):
    if len(nums) > 84:
        return gcd(nums[84], nums[21])
    else:
        return "List is too short."
