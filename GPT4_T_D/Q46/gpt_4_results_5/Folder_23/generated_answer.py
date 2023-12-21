
from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 81:
        return "List is too short"
    else:
        gcf = gcd(gcd(lst[31], lst[25]), lst[80])
    return gcf
