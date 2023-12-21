
from math import gcd

def gcf_three_nums(nums):
    if 404 < len(nums) and 834 < len(nums) and 517 < len(nums):
        return gcd(gcd(nums[404], nums[834]), nums[517])
    else:
        return 'Error: List is too short.'
