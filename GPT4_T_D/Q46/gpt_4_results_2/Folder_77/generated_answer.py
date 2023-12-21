
from math import gcd

def gcf_three_nums(lst):
    gcf_val = gcd(gcd(lst[693], lst[331]), lst[668])
    return gcf_val
