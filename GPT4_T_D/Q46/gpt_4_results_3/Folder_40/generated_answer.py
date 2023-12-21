
from math import gcd

def gcf_three_nums(lst):
    return gcd(gcd(lst[1], lst[6]), lst[8])
