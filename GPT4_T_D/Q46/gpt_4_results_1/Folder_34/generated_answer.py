
from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 54:
        return "List is too short"
    else:
        gcf = gcd(gcd(lst[53], lst[23]), lst[45])
        return gcf
