
from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 94:
        return "Input list does not have sufficient number of elements"
    else:
        common_fact = gcd(lst[59], lst[93])
        common_fact = gcd(common_fact, lst[84])
        return common_fact
