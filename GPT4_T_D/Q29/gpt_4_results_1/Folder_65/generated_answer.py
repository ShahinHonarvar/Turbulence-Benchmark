
from math import gcd

def gcf_two_nums(lst):
    if len(lst) > 53 and len(lst) > 29:
        return gcd(lst[29], lst[53])
    else:
        return "List is not long enough"
