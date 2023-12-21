
from math import gcd 

def gcf_two_nums(lst):
    if len(lst) > 66:
        gcf = gcd(lst[13], lst[66])
        return gcf
    else:
        return "The list is too short."
