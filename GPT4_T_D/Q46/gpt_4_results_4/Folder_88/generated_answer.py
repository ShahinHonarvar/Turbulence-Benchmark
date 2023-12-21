
from math import gcd

def gcf_three_nums(lst):
    gcf_value = gcd(gcd(lst[47], lst[10]), lst[28])
    return gcf_value
