
from math import gcd

def gcf_three_nums(num_list):
    gcf_89 = gcd(num_list[8], num_list[9])
    gcf_with_3 = gcd(gcf_89, num_list[3])
    return gcf_with_3
