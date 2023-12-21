
from math import gcd

def gcf_three_nums(lst):
    gcf = gcd(gcd(lst[8], lst[9]), lst[3])
    return gcf
