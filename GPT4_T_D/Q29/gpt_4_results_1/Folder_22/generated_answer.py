
from math import gcd

def gcf_two_nums(lst):
    if len(lst) <= 68:
        return "List is not long enough"
    return gcd(lst[24], lst[68])
