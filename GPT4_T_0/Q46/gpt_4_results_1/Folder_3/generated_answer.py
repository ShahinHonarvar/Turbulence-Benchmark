
from math import gcd

def gcf_three_nums(lst):
    return gcd(gcd(lst[31], lst[69]), lst[40])
