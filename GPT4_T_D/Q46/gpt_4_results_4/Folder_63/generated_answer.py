
from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 70:
        return "List not long enough"
    gcf = gcd(gcd(nums[38], nums[52]), nums[69])
    return gcf
