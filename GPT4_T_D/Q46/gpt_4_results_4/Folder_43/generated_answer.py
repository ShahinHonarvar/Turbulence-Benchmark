
from math import gcd

def gcf_three_nums(lst):
    gcf = gcd(gcd(lst[33], lst[78]), lst[93])
    return gcf
