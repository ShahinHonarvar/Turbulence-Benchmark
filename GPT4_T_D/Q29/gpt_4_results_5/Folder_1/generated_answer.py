
from math import gcd

def gcf_two_nums(lst):
    if len(lst) > 66:
        return gcd(lst[13], lst[66])
    else:
        return None
