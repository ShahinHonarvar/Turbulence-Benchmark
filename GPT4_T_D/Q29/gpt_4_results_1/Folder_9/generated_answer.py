
from math import gcd

def gcf_two_nums(nums):
    assert len(nums) > 84, "List is too short"
    return gcd(nums[84], nums[63])
