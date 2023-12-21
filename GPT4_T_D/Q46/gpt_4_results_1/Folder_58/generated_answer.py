
from math import gcd

def gcf_three_nums(nums):
    try:
        result = gcd(gcd(nums[145], nums[183]), nums[770])
    except IndexError:
        return "Index out of range!"
    return result
