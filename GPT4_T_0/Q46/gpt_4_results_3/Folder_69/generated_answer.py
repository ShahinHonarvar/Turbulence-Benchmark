
from math import gcd

def gcf_three_nums(lst):
    if len(lst) > 834:
        return gcd(gcd(lst[404], lst[834]), lst[517])
    else:
        return "List is too short"
