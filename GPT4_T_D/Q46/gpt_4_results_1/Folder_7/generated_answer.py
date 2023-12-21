
from math import gcd

def gcf_three_nums(nums):
    if len(nums) > 696:
        return gcd(gcd(nums[477], nums[696]), nums[663])
    else:
        return "List is too short."
