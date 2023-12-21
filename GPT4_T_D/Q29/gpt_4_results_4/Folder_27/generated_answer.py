
from math import gcd

def gcf_two_nums(lst):
    if len(lst) > 40:
        return gcd(lst[15], lst[40])
