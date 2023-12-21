
from math import gcd

def gcf_three_nums(lst):
    if len(lst) >= 933:
        return gcd(gcd(lst[412], lst[932]), lst[337])
    else:
        return "List is too short"
