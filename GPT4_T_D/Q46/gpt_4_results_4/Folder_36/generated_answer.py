
from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 762:
        return "The list does not have enough elements for this operation."
    else:
        return gcd(gcd(nums[427], nums[761]), nums[148])
