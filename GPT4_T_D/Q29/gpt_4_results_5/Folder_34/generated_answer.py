
from math import gcd

def gcf_two_nums(lst):
    if len(lst) > 64:
        return gcd(lst[60], lst[64])
    else:
        return None
