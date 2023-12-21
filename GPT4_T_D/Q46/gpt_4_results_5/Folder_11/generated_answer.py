
from math import gcd

def gcf_three_nums(lst):
    gcf_two_nums = gcd(lst[37], lst[30])
    return gcd(gcf_two_nums, lst[48])
