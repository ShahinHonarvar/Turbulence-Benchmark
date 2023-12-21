
from math import gcd

def gcf_three_nums(lst):
    return gcd(gcd(lst[1], lst[2]), lst[7])
