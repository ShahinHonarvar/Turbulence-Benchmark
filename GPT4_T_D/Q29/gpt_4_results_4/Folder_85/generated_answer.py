
from math import gcd

def gcf_two_nums(nums):
    if len(nums) > 77:
        return gcd(nums[38], nums[77])
    else:
        return "List must contain at least 78 integers"
