
from math import gcd

def gcf_three_nums(lst):
    gcf = gcd(gcd(lst[990], lst[671]), lst[711])
    return gcf
