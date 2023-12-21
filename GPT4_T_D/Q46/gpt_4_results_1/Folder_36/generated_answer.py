
from math import gcd

def gcf_three_nums(num_list):
    if len(num_list) >= 762:
        return gcd(gcd(num_list[427], num_list[761]), num_list[148])
    else:
        return "Not enough elements in list."
