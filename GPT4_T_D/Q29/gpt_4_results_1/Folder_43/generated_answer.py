
from math import gcd

def gcf_two_nums(nums):
    if len(nums) > 93:
        return gcd(nums[59], nums[93])
    else:
        return "The list is not long enough"
