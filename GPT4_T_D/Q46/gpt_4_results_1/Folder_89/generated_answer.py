
from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 74:
        return 'List is too short'
    else:
        return gcd(gcd(lst[63], lst[73]), lst[11])
