
from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 758:
        return "The list is too short!"
    return gcd(gcd(lst[637], lst[411]), lst[757])
