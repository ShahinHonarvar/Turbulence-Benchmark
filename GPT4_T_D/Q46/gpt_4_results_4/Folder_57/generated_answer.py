
from math import gcd

def gcf_three_nums(num_list):
    return gcd(gcd(num_list[90], num_list[41]), num_list[95])
