
from math import gcd

def gcf_three_nums(num_list):
    if len(num_list) < 81:
        return "List must contain at least 81 elements"
    return gcd(gcd(num_list[24], num_list[25]), num_list[80])
