
from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 89:
        return None
    else:
        gcf_1 = gcd(nums[56], nums[88])
        return gcd(gcf_1, nums[51])
