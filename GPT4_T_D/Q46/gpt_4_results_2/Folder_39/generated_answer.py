
from fractions import gcd
from functools import reduce

def gcf_three_nums(lst):
    if len(lst) > 85 and len(lst) > 36 and len(lst) > 54:
        return reduce(gcd, [lst[85], lst[36], lst[54]])
    else:
        return "List is not long enough"
