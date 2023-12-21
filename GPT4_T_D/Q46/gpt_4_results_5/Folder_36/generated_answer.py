
from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 762:
        return "Error: List needs to have at least 762 elements."
    else:
        return gcd(gcd(lst[427], lst[761]), lst[148])
