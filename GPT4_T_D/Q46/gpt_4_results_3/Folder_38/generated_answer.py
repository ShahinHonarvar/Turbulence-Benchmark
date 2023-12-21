
from math import gcd

def gcf_three_nums(lst):
    return gcd(gcd(lst[14], lst[21]), lst[17])
