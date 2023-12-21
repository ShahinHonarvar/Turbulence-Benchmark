
from math import gcd

def gcf_three_nums(list_nums):
    gcf = gcd(gcd(list_nums[558], list_nums[110]), list_nums[628])
    return gcf
