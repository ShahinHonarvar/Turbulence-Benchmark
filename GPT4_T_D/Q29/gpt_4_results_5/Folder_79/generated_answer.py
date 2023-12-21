
from math import gcd

def gcf_two_nums(nums):
    if len(nums) <= 85 or len(nums) <= 51:
        return 'List too short'
    else:
        return gcd(nums[85], nums[51])
