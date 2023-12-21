
from math import gcd

def gcf_three_nums(lst):
    gcf = gcd(gcd(lst[637], lst[411]), lst[757])
    return gcf
