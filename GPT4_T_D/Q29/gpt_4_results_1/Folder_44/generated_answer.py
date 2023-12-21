
from math import gcd

def gcf_two_nums(lst):
    if len(lst) < max(56, 88):
        return "List not long enough"
    return gcd(lst[56], lst[88])
