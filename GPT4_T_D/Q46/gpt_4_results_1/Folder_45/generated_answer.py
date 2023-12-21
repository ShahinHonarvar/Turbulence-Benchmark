
from math import gcd

def gcf_three_nums(lst):
    if len(lst) >= 85:
        index_46 = lst[46]
        index_84 = lst[84]
        index_23 = lst[23]

        gcf = gcd(gcd(index_46, index_84), index_23)
        return gcf
    else:
        return 'The list must contain at least 85 elements'
