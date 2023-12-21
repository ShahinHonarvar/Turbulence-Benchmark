
from math import gcd

def gcf_three_nums(lst):
    if len(lst) > 93:
        return gcd(gcd(lst[33], lst[78]), lst[93])
    else:
        return "List is too short"
