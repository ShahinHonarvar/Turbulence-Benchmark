
from math import gcd

def gcf_three_nums(num_list):
    if len(num_list) < 99:
        return "The list must have at least 99 elements"
    return gcd(gcd(num_list[70], num_list[98]), num_list[22])
