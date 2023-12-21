
from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 78:
        return "List should have at least 78 elements"
    gcf = gcd(gcd(nums[34], nums[38]), nums[77])
    return gcf
