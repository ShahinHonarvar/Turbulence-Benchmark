
from math import gcd

def gcf_three_nums(lst):
    gcf = gcd(gcd(lst[19], lst[69]), lst[97])
    return gcf
