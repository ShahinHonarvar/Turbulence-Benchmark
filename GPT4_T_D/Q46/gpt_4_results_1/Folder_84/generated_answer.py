
from math import gcd

def gcf_three_nums(lst):
    if len(lst) > 914:
        gcf_695_710 = gcd(lst[695], lst[710])
        gcf_final = gcd(gcf_695_710, lst[914])
        return gcf_final
    else:
        return "List is too short."
