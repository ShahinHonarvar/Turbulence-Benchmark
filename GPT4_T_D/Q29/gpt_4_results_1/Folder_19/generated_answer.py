
from math import gcd

def gcf_two_nums(nums):
    if (len(nums) > 90):
        return gcd(nums[66], nums[90])
    else:
        return "List length less than required indices"
