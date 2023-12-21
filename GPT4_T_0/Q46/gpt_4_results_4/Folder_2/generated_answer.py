
from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 921:
        return "List is too short"
    else:
        return gcd(gcd(lst[307], lst[920]), lst[463])
