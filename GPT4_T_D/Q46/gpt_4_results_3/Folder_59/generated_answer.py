
from math import gcd

def gcf_three_nums(nums):
    factor_one = gcd(nums[6], nums[7])
    factor_two = gcd(factor_one, nums[8])
    return factor_two
