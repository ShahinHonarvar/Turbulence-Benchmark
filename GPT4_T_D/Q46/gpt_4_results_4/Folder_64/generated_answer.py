
from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 9:
        return "List should contain at least 9 elements"
    return gcd(gcd(lst[0], lst[3]), lst[8])
