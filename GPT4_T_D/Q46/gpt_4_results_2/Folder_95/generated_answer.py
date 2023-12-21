
from math import gcd

def gcf_three_nums(lst):
    gcd_temp = gcd(lst[87], lst[20])
    gcf_result = gcd(gcd_temp, lst[36])
    return gcf_result
