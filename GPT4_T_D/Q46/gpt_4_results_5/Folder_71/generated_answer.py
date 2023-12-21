
from math import gcd

def gcf_three_nums(lst):
    gcf = gcd(gcd(lst[24], lst[45]), lst[38])
    return gcf
