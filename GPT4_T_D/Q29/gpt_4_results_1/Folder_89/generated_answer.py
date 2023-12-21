
from math import gcd

def gcf_two_nums(lst):
    if len(lst) > 37 and len(lst) > 30:
        return gcd(lst[37], lst[30])
    return "The list is too short"
