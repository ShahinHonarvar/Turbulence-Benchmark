
from math import gcd

def gcf_three_nums(nums):
    index_21, index_69, index_41 = nums[21], nums[69], nums[41]
    gcf_nums = gcd(gcd(index_21, index_69), index_41)
    return gcf_nums
