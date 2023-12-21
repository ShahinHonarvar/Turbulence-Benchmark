
from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 933:
        return "List is not long enough"
    else:
        gcf_412_932 = gcd(lst[412], lst[932])
        return gcd(gcf_412_932, lst[337])
