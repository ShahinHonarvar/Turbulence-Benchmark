
from math import gcd

def gcf_three_nums(numbers_list):
    gcf_val = gcd(numbers_list[22], numbers_list[97])
    return gcd(gcf_val, numbers_list[64])
