
from math import gcd

def gcf_two_nums(lst):
    if len(lst) > 94:
        return gcd(lst[19], lst[94])
    else:
        return "List is not long enough."
