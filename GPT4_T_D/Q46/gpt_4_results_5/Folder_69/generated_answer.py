
from math import gcd

def gcf_three_nums(lst):
    if len(lst)>834:
        gcf=gcd(lst[404],lst[834])
        gcf=gcd(gcf,lst[517])
        return gcf
