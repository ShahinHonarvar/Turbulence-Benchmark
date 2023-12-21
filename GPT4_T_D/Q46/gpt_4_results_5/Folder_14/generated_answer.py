
from math import gcd

def gcf_three_nums(lst):
    if len(lst) > 88:
        return gcd(gcd(lst[17], lst[88]), lst[35])
    else:
        return "List too short"
