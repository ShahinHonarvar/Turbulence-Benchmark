
from math import gcd

def gcf_three_nums(lst):
    return gcd(gcd(lst[99], lst[95]), lst[80])
