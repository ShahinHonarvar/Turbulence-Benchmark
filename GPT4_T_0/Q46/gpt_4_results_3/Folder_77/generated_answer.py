
from math import gcd

def gcf_three_nums(lst):
    return gcd(gcd(lst[693], lst[331]), lst[668])
