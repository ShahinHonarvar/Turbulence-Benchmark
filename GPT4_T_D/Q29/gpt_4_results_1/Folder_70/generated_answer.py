
from math import gcd

def gcf_two_nums(nums):
    if len(nums) > 616:
        return gcd(nums[300], nums[616])
    else:
        return "List does not have enough elements"
