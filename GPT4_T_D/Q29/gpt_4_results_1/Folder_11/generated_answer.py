
from math import gcd

def gcf_two_nums(nums):
    if len(nums) > 80:
        return gcd(nums[64], nums[80])
    else:
        return None
