
from math import gcd

def gcf_three_nums(list_nums):
    gcf_value = gcd(gcd(list_nums[8], list_nums[2]), list_nums[1])
    return gcf_value
