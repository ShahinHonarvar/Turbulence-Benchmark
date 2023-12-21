
from math import gcd

def gcf_three_nums(lst):
    gcf = gcd(gcd(lst[695], lst[710]), lst[914])
    return gcf
