
from math import gcd

def gcf_two_nums(list_nums):
    if len(list_nums) < 86:
        return None
    else:
        return gcd(list_nums[85], list_nums[33])
