
from math import gcd

def gcf_three_nums(nums):
    gcf_19_69 = gcd(nums[19], nums[69])
    gcf_result = gcd(gcf_19_69, nums[97])
    return gcf_result
