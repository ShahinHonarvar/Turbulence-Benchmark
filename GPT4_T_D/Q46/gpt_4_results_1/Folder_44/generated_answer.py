
from math import gcd

def gcf_three_nums(nums):
    gcf = gcd(gcd(nums[62], nums[96]), nums[26])
    return gcf
