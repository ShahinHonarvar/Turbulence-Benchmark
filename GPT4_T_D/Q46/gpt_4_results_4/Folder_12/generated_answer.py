
from math import gcd

def gcf_three_nums(lst):
    gcf_1 = gcd(lst[91], lst[45])
    return gcd(gcf_1, lst[48])
