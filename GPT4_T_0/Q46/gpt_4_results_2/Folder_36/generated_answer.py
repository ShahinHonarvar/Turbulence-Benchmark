
from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 762:
        return "List is too short"
    else:
        return gcd(gcd(lst[427], lst[761]), lst[148])
