
from math import gcd

def gcf_three_nums(nums):
    if len(nums) <= 693 or len(nums) <= 331 or len(nums) <= 668:
        return "Invalid list length"
    gcf = gcd(gcd(nums[693], nums[331]), nums[668])
    return gcf
