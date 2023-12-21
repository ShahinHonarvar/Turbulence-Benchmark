
from math import gcd

def gcf_three_nums(number_list):
    return gcd(gcd(number_list[99], number_list[63]), number_list[74])
